import toml


def load_config(file_path):
    with open(file_path, "r") as config_file:
        config = toml.load(config_file)
    return config["general"]


def get_config_value(config_data, key):
    return config_data.get(key, None)


config_data = load_config("config.toml")

config_params = [
    "OAUTH_TOKEN", "CATALOG_ID", "ID_KEY", "API", "RATE",
    "CHUNK", "SAMPLE_RATE", "CHUNK_SIZE", "INVALID_ELEMENTS",
    "VOICE", "EMOTION", "SPEED", "MAX_PAUSE_BETWEEN_WORDS_HINT_MS",
    "TYPE", "PORT", "HOST"
]

OAUTH_TOKEN, CATALOG_ID, ID_KEY, API, RATE, CHUNK, SAMPLE_RATE, CHUNK_SIZE, \
    INVALID_ELEMENTS, VOICE, EMOTION, SPEED, MAX_PAUSE_BETWEEN_WORDS_HINT_MS, \
    TYPE, PORT, HOST = [get_config_value(config_data, param) for param in config_params]
