import requests

import helper
import setting
from recognition import Recognition
from speach_synthesis import pyaudio_play_audio_function
from setting import PORT, HOST


def listen_command(text):
    return text


def send_text(text):
    return ''


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
    while True:
        while sensor_active():
            test = Recognition(setting.API)
            text = test.run()[0]
            send_text(text)
            # new_text = get_text()
            # pyaudio_play_audio_function(" . " + " .... " + new_text)

            pyaudio_play_audio_function(" . " + " .... " + text)
