import pyaudio

oauth_token = "y0_AgAAAABHGDDBAATuwQAAAADusd1bSZvBsJ9eSH2pDw_6yBERArU45a4"
catalog_id = "b1gluhl8h1ulmb8852j6"
id_key = "aje99j71kckucio04tlf"
API = "AQVNyUzOGjKeZLACdq8b96ibAT1WnAUPcRpx5jbX"

# Настройки потокового распознавания.
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 4096
RECORD_SECONDS = 30
WAVE_OUTPUT_FILENAME = "audio.wav"

# pyaudio_play_audio_function
sample_rate = 16000  # частота дискретизации должна совпадать при синтезе и воспроизведении
chunk_size = 400
num_channels = 1

# Настройки голоса
invalid_elements = (' ', '')  # Строки, которые игнорируются синтезатором
datas = {

    'lang': 'ru-RU',
    'voice': 'madirus',  # oksana
    'emotion': 'evil',
    'speed': '1.1',
    'format': 'lpcm',
    'sampleRateHertz': sample_rate,
}

# Настройки сети
port = "8888"
host = "127.0.0.1"
