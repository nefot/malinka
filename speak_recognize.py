import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def listen_command():
    """
    Функция распознает сообщение
    :return: текст
    """
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.2)
            audio = sr.listen(source=mic)
            try:
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            except ConnectionResetError:
                pass
        return query
    except speech_recognition.UnknownValueError:
        return ''

# import argparse
#
# import grpc
#
# import yandex.cloud.ai.stt.v3.stt_pb2 as stt_pb2
# import yandex.cloud.ai.stt.v3.stt_service_pb2_grpc as stt_service_pb2_grpc
#
# CHUNK_SIZE = 4000
#
# def gen(audio_file_name):
#     # Задайте настройки распознавания.
#     recognize_options = stt_pb2.StreamingOptions(
#         recognition_model=stt_pb2.RecognitionModelOptions(
#             audio_format=stt_pb2.AudioFormatOptions(
#                 raw_audio=stt_pb2.RawAudio(
#                     audio_encoding=stt_pb2.RawAudio.LINEAR16_PCM,
#                     sample_rate_hertz=8000,
#                     audio_channel_count=1
#                 )
#             ),
#             text_normalization=stt_pb2.TextNormalizationOptions(
#                 text_normalization=stt_pb2.TextNormalizationOptions.TEXT_NORMALIZATION_ENABLED,
#                 profanity_filter=True,
#                 literature_text=False
#             ),
#             language_restriction=stt_pb2.LanguageRestrictionOptions(
#                 restriction_type=stt_pb2.LanguageRestrictionOptions.WHITELIST,
#                 language_code=['ru-RU']
#             ),
#             audio_processing_type=stt_pb2.RecognitionModelOptions.REAL_TIME
#         )
#     )
#
#     # Отправьте сообщение с настройками распознавания.
#     yield stt_pb2.StreamingRequest(session_options=recognize_options)
#
#     # Прочитайте аудиофайл и отправьте его содержимое порциями.
#     with open(audio_file_name, 'rb') as f:
#         data = f.read(CHUNK_SIZE)
#         while data != b'':
#             yield stt_pb2.StreamingRequest(chunk=stt_pb2.AudioChunk(data=data))
#             data = f.read(CHUNK_SIZE)
#
# def run(iam_token, audio_file_name):
#     # Установите соединение с сервером.
#     cred = grpc.ssl_channel_credentials()
#     channel = grpc.secure_channel('stt.api.cloud.yandex.net:443', cred)
#     stub = stt_service_pb2_grpc.RecognizerStub(channel)
#
#     # Отправьте данные для распознавания.
#     it = stub.RecognizeStreaming(gen(audio_file_name), metadata=(
#         ('authorization', f'Bearer {iam_token}'),
#     ))
#
#     # Обработайте ответы сервера и выведите результат в консоль.
#     try:
#         for r in it:
#             event_type, alternatives = r.WhichOneof('Event'), None
#             if event_type == 'partial' and len(r.partial.alternatives) > 0:
#                 alternatives = [a.text for a in r.partial.alternatives]
#             if event_type == 'final':
#                 alternatives = [a.text for a in r.final.alternatives]
#             if event_type == 'final_refinement':
#                 alternatives = [a.text for a in r.final_refinement.normalized_text.alternatives]
#             print(f'type={event_type}, alternatives={alternatives}')
#     except grpc._channel._Rendezvous as err:
#         print(f'Error code {err._state.code}, message: {err._state.details}')
#         raise err
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--token', required=True, help='IAM token')
#     parser.add_argument('--path', required=True, help='audio file path')
#     args = parser.parse_args()
#     run(args.token, args.path)
#

# import speech_recognition
#
# sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5
#
#
# def listen_command():
#     print("listen_command")
#     """The function will return the recognized command"""
#
#     try:
#         with speech_recognition.Microphone() as mic:
#             sr.adjust_for_ambient_noise(source = mic, duration = 0.2)
#             audio = sr.listen(source = mic)
#             try:
#                 query = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()
#             except ConnectionResetError:
#                 pass
#         return query
#     except speech_recognition.UnknownValueError:
#         return ''
#
#
# def record_a
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     while True:
#      print(listen_command())
#
#
#
#
#
#
#
#


# import pyaudio
# from speechkit import  ShortAudioRecognition
# from  speak_synthesis import  session
#
# class Recognize:
#     def __init__(self):
#         self.recognizeShortAudio = ShortAudioRecognition(session)
#         self.p = pyaudio.PyAudio()
#     def speak_recognize(self):
#         """
#         Метод распознает текст с аудио
#         :return: возвращает строку с текстом
#         """
#         text = self.recognizeShortAudio.recognize(data, format='lpcm', sampleRateHertz='48000')
#         print(text)
#
#     def record_audio(self):
#         p = pyaudio.PyAudio()
#         stream = p.open(
#             format=pyaudio.paInt16,
#             channels=num_channels,
#             rate=sample_rate,
#             input=True,
#             frames_per_buffer=chunk_size
#         )
#
