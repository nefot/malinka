import pyaudio
import yandex.cloud.ai.stt.v3.stt_pb2 as stt_pb2
import yandex.cloud.ai.stt.v3.stt_service_pb2_grpc as stt_service_pb2_grpc

OAUTH_TOKEN = "y0_AgAAAABHGDDBAATuwQAAAADusd1bSZvBsJ9eSH2pDw_6yBERArU45a4"
CATALOG_ID = "b1gluhl8h1ulmb8852j6"
ID_KEY = "aje99j71kckucio04tlf"
API = "AQVNyUzOGjKeZLACdq8b96ibAT1WnAUPcRpx5jbX"

# Настройки потокового распознавания.
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 4
RECORD_SECONDS = 30
WAVE_OUTPUT_FILENAME = "audio.wav"

# pyaudio_play_audio_function
SAMPLE_RATE = 16000  # частота дискретизации должна совпадать при синтезе и воспроизведении
CHUNK_SIZE = 400
NUM_CHANNELS = 1

# Настройки голоса
INVALID_ELEMENTS = (' ', '')  # Строки, которые игнорируются синтезатором
SPEAK_SETTING = {

    'lang': 'ru-RU',
    'voice': 'ermil',  # oksana
    'emotion': 'good',
    'speed': '1.1',
    'format': 'lpcm',
    'sampleRateHertz': SAMPLE_RATE,
}

# Настройки сети
PORT = "8888"
HOST = "127.0.0.1"

# Телеграмм бот
BOT_TOKEN = '6603728925:AAEUyY9-cbtVh9grWCB6pXBDLoYVc5auoYk'
MY_ID = 1407136430
