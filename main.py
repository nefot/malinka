import requests

import helper
from speach_synthesis import pyaudio_play_audio_function
from setting import port, host


def listen_command(text):
    return text


def get_text():
    """
    Этот метод вытаскивает данные из json файла
    :param text: json файл
    :return: текст
    """
    res = requests.get(f"http://{host}:{port}/donetext")
    return res,


if __name__ == '__main__':
    while True:
        pyaudio_play_audio_function(listen_command())
