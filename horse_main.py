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

    # importing the requests library


    # api-endpoint
    URL = f"http://{HOST}:{PORT}/invoke"

    # location given here
    location = "delhi technological university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'query': response}

    # sending get request and saving the response as response object
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
                response = get_text(text)
                print("\033[32 {}" .format(response))

                print(response)
                if text:
                    SP.process_and_play_audio(" . " + " .... " + response)
