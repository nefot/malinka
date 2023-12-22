import requests
import setting
from main import run
from service import *
from recognition import Recognition
from speach_synthesis import SoundProcessor
from setting import PORT, HOST

def sensor_active():
    return True


def get_text(response):

    res = requests.get(f"http://{HOST}:{PORT}/invoke")

    URL = f"http://{HOST}:{PORT}/invoke"

    PARAMS = {'query': response}

    r = requests.get(url=URL, params=PARAMS)




if __name__ == '__main__':
    print('\n___________________________________________________________\n')
    SP = SoundProcessor()
    delete_bd()
    bd_create()


    while True:
        while sensor_active():
            test = Recognition(setting.API)

            try:
                text = test.run()[0]
                print("ПОЛЬЗОВАТЕЛЬ: ", text)
            except TypeError:
                continue

            if text is not None:
                print('[text], ', text)
                response = get_text(text)
                print('[response], ', response)
                print("\033[32 {}" .format(response))

                print(response)
                if text:
                    SP.process_and_play_audio(" . " + " .... " + response)
