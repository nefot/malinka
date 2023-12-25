# from speach_synthesis import SoundProcessor
import requests
from horseclients.setting import HOST, PORT, API
from horseclients.speach_recognition import Recognition
from speach_synthesis import SpeachGeneration


def get_text(query: str) -> dict | str:
    try:
        resp = requests.post(f"http://{HOST}:{PORT}/invoke", json={"query": query})
        print(resp)
        return resp.json()['response']
    except requests.exceptions.ConnectTimeout:
        return 'Нет соединения с сервером'


def startup(name) -> print:
    len_line = 60
    print('\n', '-' * int((len_line / 2) - int(len(name) / 2) - 1) + ' ' + name + ' ' + '-' * int(
        (len_line / 2) - int(len(name) / 2) - 1),
          '\n')


if __name__ == '__main__':
    SD = SpeachGeneration(API)
    REC = Recognition(API)
    startup('HORSE CLIENT')
    while True:
        text = REC.run()[0]
        if text is None: continue
        print('[Пользователь]', text)
        response = get_text(text)
        n = SD.synthesize(response)
    startup('EXIT')
