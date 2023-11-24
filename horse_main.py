import requests
import setting
from main import run
from service import *
from recognition import Recognition
from speach_synthesis import SoundProcessor
from setting import PORT, HOST


def sensor_active():
    return True


def get_text():
    """
    Этот метод вытаскивает данные из json файла
    :param text: json файл
    :return: текст
    """
    res = requests.get(f"http://{HOST}:{PORT}/donetext")
    return res,


if __name__ == '__main__':
    SP = SoundProcessor()
    delete_bd()
    bd_create()
    while True:
        while sensor_active():
            test = Recognition(setting.API)

            try:
                text = test.run()[0]
            except TypeError:
                continue

            if text is not None:
                text = run(text)
                print(text)
                if text:
                    SP.process_and_play_audio(" . " + " .... " + text)
