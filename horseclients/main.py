# from speach_synthesis import SoundProcessor
import grpc
import requests
from grpc._channel import _MultiThreadedRendezvous

from setting import HOST, PORT, YANDEX_API_KEY
from speach_recognition import Recognition
from speach_synthesis import SpeachGeneration


def get_text(query: str) -> dict | str:
    try:
        resp = requests.post(f"http://{HOST}:{PORT}/invoke", json={"query": query})
        return resp.json()['response']
    except requests.exceptions.ConnectTimeout:
        return 'Нет соединения с сервером'


def startup(name) -> print:
    len_line = 100
    print('\n', '-' * int((len_line / 2) - int(len(name) / 2) - 1) + ' ' + name + ' ' + '-' * int(
        (len_line / 2) - int(len(name) / 2) - 1),
          '\n')


if __name__ == '__main__':
    SD = SpeachGeneration(YANDEX_API_KEY)
    REC = Recognition(YANDEX_API_KEY)
    startup('HORSE CLIENT')
    while True:
        text = REC.run()[0]
        if text is None: continue
        print('[Пользователь]', text)
        response = get_text(text)
        print('[Конь]', response)
        try:
            n = SD.synthesize(response)
        except grpc._channel._Rendezvous as e:
            if e._state.details.split(',')[0] == 'Too long text':
                print("Too long text", e._state.details)
            else:
                print("Произошла ошибка gRPC:", e)
        except Exception as e:
            print("Произошла ошибка:", e)

    startup('EXIT')
