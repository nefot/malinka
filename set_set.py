import tomli
def constructing():
    with open("config.toml", "rb") as f:
        toml_dict = tomli.load(f)
    print(toml_dict)


    construct = (f'--- Список настроек ---\n  \n   Настройки потокового распознавания. \n  \n '
                 f'<b>CHANNELS</b> = {toml_dict["S"]["CHANNELS"]}\n <b>RATE</b> = {toml_dict["S"]["RATE"]}\n <b>MAX_PAUSE_BETWEEN_WOR'
                 f'DS_HINT_MS</b> = {toml_dict["VOICE_SETTING"]["MAX_PAUSE_BETWEEN_WORDS_HINT_MS"]},\n <b>TYPE</b> = {toml_dict["VOICE_SETTING"]["TYPE"]}\n <b>CHUNK</b> = {toml_dict["S"]["CHUNK"]}\n '
                 f'<b>RECORD_SECONDS</b> = {toml_dict["S"]["RECORD_SECONDS"]}\n \n  pyaudio_play_audio_function \n \n '
                 f'<b>SAMPLE_RATE</b> = {toml_dict["S"]["SAMPLE_RATE"]}\n <b>CHUNK_SIZE</b> = {toml_dict["S"]["CHUNK_SIZE"]}\n <b>NUM_CHANNELS</b> = '
                 f'{toml_dict["S"]["NUM_CHANNELS"]}\n \n Настройки голоса \n \n <b>INVALID_ELEMENTS</b> = { toml_dict["VOICE_SETTING"]["INVALID_ELEMENTS"]}  \n '
                 f'<b>VOICE</b> = {toml_dict["VOICE_SETTING"]["VOICE"]}\n <b>EMOTION</b> ={toml_dict["VOICE_SETTING"]["EMOTION"]}\n <b>SPEED</b> ={toml_dict["VOICE_SETTING"]["SPEED"]}\n \n')
    return construct