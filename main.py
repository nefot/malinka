import requests

from speak_recognize import listen_command
from speak_synthesis import TextToSpeak
from setting import port, host


def dubbing():
    pass


def listening():
    pass


def get_text():
    """
    Этот метод вытаскивает данные из json файла
    :param text: json файл
    :return: текст
    """
    res = requests.get(f"http://{host}:{port}/donetext")
    return res,


if __name__ == '__main__':
    a = TextToSpeak()
    while True:
        print(listen_command())

    #

        a.pyaudio_play_audio_function(listen_command())
