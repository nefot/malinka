import requests
import setting
from bd_parser import find_answer
from recognition import Recognition
from speach_synthesis import SoundProcessor
from setting import PORT, HOST


def listen_command(text):
    return text


def send_text(text):
    return text


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
    while True:
        while sensor_active():
            test = Recognition(setting.API)
            text = test.run()[0]
            send_text(text)
            # new_text = get_text()
            # pyaudio_play_audio_function(" . " + " .... " + new_text)
            SP.process_and_play_audio(" . " + " .... " + find_answer(text, "horse_database.db"))
