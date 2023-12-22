import os
import sqlite3

import numpy as np
import wave
import pandas as pd


from setting import CHUNK_SIZE



def bd_create():
    """
    Создает базу данных с Excel файла
    :return: ничего не возвращает
    """
    conn = sqlite3.connect('horse_database.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
        '''
    )
    cursor.close()
    # Загрузка данных из Excel
    df = pd.read_excel('bd.xlsx')
    df = df.apply(lambda x: x.lower() if isinstance(x, str) else x)

    # Загрузка данных в базу данных SQLite
    df.to_sql('my_table', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()


def delete_bd():
    if os.path.exists('horse_database.db'):
        os.remove('horse_database.db')
    else:
        pass


def remove_empty_elements(input_list):
    processed_list = [element for element in input_list if element.strip() != '']
    return processed_list


def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        out_yellow(f'[{func.__name__}] Время выполнения: {end - start} секунд.')
        return return_value

    return wrapper

def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))



class Charisma:
    def __init__(self, audio: bytes):
        self.audio = audio

    def merge_wav_and_bytes(self, wav_file_path, bytes_data):
        # Чтение данных из WAV-файла
        with wave.open(wav_file_path, 'rb') as wf:
            wav_data = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
        wav_bytes = wav_data.tobytes()

        # Объединение данных
        merged_bytes = bytes_data + wav_bytes

        return merged_bytes

    def add_neighing(self):
        return self.merge_wav_and_bytes(wav_file_path="frrrrrrr3.wav", bytes_data=self.audio)
