import pyaudio
OAUTH_TOKEN = "y0_AgAAAABHGDDBAATuwQAAAADusd1bSZvBsJ9eSH2pDw_6yBERArU45a4"
CATALOG_ID = "b1gluhl8h1ulmb8852j6"
ID_KEY = "aje99j71kckucio04tlf"
API = "AQVN28kNiTnroB63hIH6cjfOzC0WMOzebEzH6p_A"

# Настройки потокового распознавания.
FORMAT = pyaudio.paInt16
RATE = 8000
CHUNK = 4

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
PORT = "5000"
HOST = "127.0.0.1"