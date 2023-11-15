import os
import random
import sqlite3
import pandas as pd
import openpyxl

from typing import AnyStr
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from loger import logger


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
        logger.debug("База данных удалена.")
    else:
        logger.debug("База данных не существует.")


def remove_empty_elements(input_list):
    processed_list = [element for element in input_list if element.strip() != '']
    return processed_list


def find_answer(keyword):
    """
    :param keyword: Ключевое слова
    :return: возвращает ответ
    """
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect("horse_database.db")
    cursor = conn.cursor()
    search_term = f'% {keyword} %'
    query = "SELECT answer FROM my_table WHERE ' ' || LOWER(keywords) || ' ' LIKE ?;"
    cursor.execute(query, (search_term,))

    # Получаем результат запроса
    result = cursor.fetchone()

    # Закрываем соединение с базой данных
    conn.close()
    if result:
        list = remove_empty_elements(result[0].split(";"))
        return list[random.randint(0, len(list) - 1)]  # Возвращаем найденный ответ
    else:
        return None


def word_shortener(text):
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    stemmer = SnowballStemmer("russian")
    question = tokenizer.tokenize(text)
    WordArray = []
    for word in question:
        WordArray.append(stemmer.stem(word).lower())
    return WordArray


def assistant(question: AnyStr):
    logger.debug('вопрос (question): [' + question + "]")

    helloKeyWords = ['кон', "привет", "здравств"]
    goodByeKeyWords = ['пок', "проща", "забуд"]

    WordArray = word_shortener(text=question)
    response = ''

    if any(helloWord in WordArray for helloWord in helloKeyWords):
        response += ("Здравствуйте! Я конь Василий, ваш гид по достопримечательностям Ростовской области. Задайте мне "
                     "вопросы об интересующей вас достопримечательности, и, если я знаю о ней, то поведаю вам! Для "
                     "завершения разговора скажите пока")
        return response

    if any(goodByeKeyWord in WordArray for goodByeKeyWord in goodByeKeyWords):
        response += "До свидания, рад был помочь!"
        return response

    for word in WordArray:
        if find_answer(word):
            logger.debug("Ключевое слово: " + word)
            return find_answer(word)


def process_excel_file():
    input_excel_file = 'bd.xlsx'
    workbook = openpyxl.load_workbook(input_excel_file)
    worksheet = workbook.active
    max_row = worksheet.max_row
    for row in range(1, max_row + 1):
        cell = worksheet.cell(row=row, column=4)
        if cell.value:
            cell.value = " ".join(word_shortener(str(cell.value)))

    # Сохраните изменения в новом файле
    output_excel_file = 'bd.xlsx'
    workbook.save(output_excel_file)


def run(question):
    try:
        while True:
            response = assistant(question)
            print(f"< {response}")
            logger.debug('ответ (response): [' + response + ']')
            return assistant(question)
    except Exception as e:
        logger.error(e)
        return assistant(question)


if __name__ == "__main__":
    process_excel_file()
    print("-" * 80)
    while True:
        question = input("> ")
        response = assistant(question)
        print(f"< {response}")
        logger.debug('ответ (response): [' + response + ']')
