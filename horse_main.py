import json
import requests
import setting
from main import run
from service import *
from recognition import Recognition
from speach_synthesis import SoundProcessor
from setting import PORT, HOST

def sensor_active():
    return True


def get_text(query):

    resp = requests.post(f"http://{HOST}:{PORT}/invoke", data=json.dumps({"query": query}))
    print(resp)
    return resp.json()['response']




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
