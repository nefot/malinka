import os
import random
import sqlite3
import pandas as pd
import openpyxl

import spacy

nlp = spacy.load("ru_core_news_sm")

from typing import AnyStr
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from loger import logger


# def find_answer(keyword):
#     print('find answer: ', keyword)
#     """
#     :param keyword: Ключевое слова
#     :return: возвращает ответ
#     """
#     # Устанавливаем соединение с базой данных
#     conn = sqlite3.connect("horse_database.db")
#     cursor = conn.cursor()
#     search_term = f'% {keyword} %'
#     query = "SELECT answer FROM my_table WHERE ' ' || LOWER(keywords) || ' ' LIKE ?;"
#     cursor.execute(query, (search_term,))
#
#     # Получаем результат запроса
#     result = cursor.fetchone()
#
#     # Закрываем соединение с базой данных
#     conn.close()
#     if result:
#         list = remove_empty_elements(result[0].split(";"))
#         return list[random.randint(0, len(list) - 1)]  # Возвращаем найденный ответ
#     else:
#         return None


def levenshtein(str_1, str_2):


    # doc1 = nlp(str_1)
    # doc2 = nlp(str_2)
    #
    # print(str_1, str_2 , doc2.similarity(doc1))
    # return doc1.similarity(doc2)

    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]
    #

# def word_shortener(text):
#     text = t ext.lower()
#     tokenizer = RegexpTokenizer(r'\w+')
#     stemmer = SnowballStemmer("russian")
#     question = tokenizer.tokenize(text)
#     WordArray = []
#     for word in question:
#         WordArray.append(stemmer.stem(word).lower())
#     return WordArray


# def assistant(question: AnyStr):
#     logger.debug('вопрос (question): [' + question + "]")
#
#
#     WordArray = word_shortener(text=question)
#     response = ''
#
#     if any(helloWord in WordArray for helloWord in helloKeyWords):
#         response += ("Здравствуйте! Я конь Василий, ваш гид по достопримечательностям Ростовской области. Задайте мне "
#                      "вопросы об интересующей вас достопримечательности, и, если я знаю о ней, то поведаю вам! Для "
#                      "завершения разговора скажите пока")
#         return response
#
#     if any(goodByeKeyWord in WordArray for goodByeKeyWord in goodByeKeyWords):
#         response += "До свидания, рад был помочь!"
#         return response
#
#     for word in WordArray:
#         if find_answer(word):
#             logger.debug("Ключевое слово: " + word)
#             return find_answer(word)
#
#

#
# def run(question):
#     try:
#         while True:
#             response = assistant(question)
#             print(f"< {response}")
#             logger.debug('ответ (response): [' + response + ']')
#             return assistant(question)
#     except Exception as e:
#         logger.error(e)
#         return assistant(question)


def conect_bd():
    conn = sqlite3.connect('horse_database.db')
    cursor = conn.cursor()
    return cursor


def get_all_question_bd(cursor):
    try:
        # Выполнение запроса для получения всех значений из столбца question
        cursor.execute("SELECT question FROM my_table")
        rows = cursor.fetchall()

        # Вывод значений на экран
        # for row in rows:
            # print(row[0])
        # print(type(rows))
        return rows

    except sqlite3.Error as e:
        print("Ошибка SQLite:", e)


def get_answer(question: list, query):
    d = []
    paradigma_arr = []
    for i in question:
        for j in i:

            for g in str(j).split("\n"):
                if g:
                    d.append(levenshtein(g, query))


            paradigma_arr.append(min(d))
            d = []

    return(paradigma_arr.index(min(paradigma_arr)))

def get_answer_by_rowid(row_id, database_path):
    # Подключение к базе данных
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        # Выполнение запроса
        cursor.execute("SELECT answer FROM my_table WHERE rowid = ?", (row_id,))
        result = cursor.fetchone()

        # Если значение найдено, вернуть его
        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print("Ошибка SQLite:", e)

    finally:
        # Закрытие соединения с базой данных
        conn.close()
def run(text):
    cur = conect_bd()
    answer_value = get_answer_by_rowid(get_answer(get_all_question_bd(cur), text) + 1, 'horse_database.db')
    return str(answer_value).split(";") [random.randrange(len(str(answer_value).split(";")))]

if __name__ == "__main__":
    cur = conect_bd()
    while True:
        answer_value = get_answer_by_rowid(get_answer(get_all_question_bd(cur), str(input()))+1, 'horse_database.db')

        if answer_value is not None:
            print("Значение в ячейке: ", str(answer_value).split(";") [random.randrange(len(str(answer_value).split(";")))])
        else:
            print("Значение не найдено.")





    # print("-" * 80)
    # while True:
    #     question = input("> ")
    #
    #     print(f"< {response}")
    #     logger.debug('ответ (response): [' + response + ']')
