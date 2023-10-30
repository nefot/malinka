import requests
import setting
from recognition import Recognition

test = Recognition(setting.API)
text = test.run()[0]
# URL сервера
server_url = "http://127.0.0.1:5000"  # Замените на фактический URL сервера

# Данные для отправки на сервер
data_to_send = {"question": test.run()[0]}

# Отправляем POST-запрос на сервер
response = requests.post(f"{server_url}/", json=data_to_send)

if response.status_code == 200:
    # Получаем ответ от сервера
    response_data = response.json()

    # Проверяем, что ответ содержит поле "question"
    if "question" in response_data:
        print("Ответ:", response_data["question"])
    else:
        print("Поле 'question' отсутствует в ответе.")
else:
    print("Не удалось выполнить запрос.")

# import requests
# import setting
# from bd_parser import find_answer
# from recognition import Recognition
# from speach_synthesis import SoundProcessor
# from setting import PORT, HOST
#
#
# def listen_command(text):
#     return text
#
#
# def send_text(text):
#     return text
#
#
# def sensor_active():
#     return True
#
#
# def get_text():
#     """
#     Этот метод вытаскивает данные из json файла
#     :param text: json файл
#     :return: текст
#     """
#     res = requests.get(f"http://{HOST}:{PORT}/donetext")
#     return res,
#
#
# if __name__ == '__main__':
#
#     SP = SoundProcessor()
#     while True:
#         while sensor_active():
#             test = Recognition(setting.API)
#             text = test.run()[0]
#             send_text(text)
#             # new_text = get_text()
#             # pyaudio_play_audio_function(" . " + " .... " + new_text)
#             SP.process_and_play_audio(" . " + " .... " + find_answer(text, "horse_database.db"))
