import os
import toml


def load_config(file_path):
    with open(file_path, "r") as config_file:
        config = toml.load(config_file)
    return config["general"]


def get_config_value(config_data, key):
    return config_data.get(key, None)


YANDEX_API_KEY = os.environ.get('YANDEX_API_KEY')
YANDEX_FOLDER_ID = os.environ.get('YANDEX_FOLDER_ID')
CONNECTION_STRING = os.environ.get('CONNECTION_STRING')

config_data = load_config("../config.toml")

config_params = [
    "RATE", "CHUNK", "SAMPLE_RATE", "CHUNK_SIZE", "INVALID_ELEMENTS",
    "VOICE", "EMOTION", "SPEED", "MAX_PAUSE_BETWEEN_WORDS_HINT_MS",
    "TYPE", "PORT", "HOST"
]
RATE, CHUNK, SAMPLE_RATE, CHUNK_SIZE, \
    INVALID_ELEMENTS, VOICE, EMOTION, SPEED, MAX_PAUSE_BETWEEN_WORDS_HINT_MS, \
    TYPE, PORT, HOST = [get_config_value(config_data, param) for param in config_params]

del config_data, config_params
