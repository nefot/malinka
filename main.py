import random
import sqlite3


import spacy

from nltk import ngrams

from service import benchmark
from loger import get_logger

nlp = spacy.load("ru_core_news_sm")
logger = get_logger(__name__)



def ngram_similarity(str1, str2, n=3):
    ngrams_str1 = set(ngrams(str1.lower(), n))
    ngrams_str2 = set(ngrams(str2.lower(), n))
    intersection = ngrams_str1.intersection(ngrams_str2)
    similarity = len(intersection) / float(len(ngrams_str1.union(ngrams_str2)))
    return similarity * 100

def compare_russian_strings(str1, str2):
    similarity_percentage = ngram_similarity(str1, str2)
    # print(f"Степень схожести строк: {similarity_percentage:.2f}%")
    return similarity_percentage



def levenshtein(str_1, str_2):
    return compare_russian_strings(str_1, str_2)


def conect_bd():
    conn = sqlite3.connect('horse_database.db')
    cursor = conn.cursor()
    return cursor


def get_all_question_bd(cursor):
    try:
        cursor.execute("SELECT question FROM my_table")
        rows = cursor.fetchall()
        return rows

    except sqlite3.Error as e:
        print("Ошибка SQLite:", e)


@benchmark
def get_answer(question: list, query):
    d = []
    paradigms_arr = []
    for i in question:
        for j in i:
            for g in str(j).split("\n"):
                if g:
                    d.append(levenshtein(g, query))

            paradigms_arr.append(max(d))
            d = []
    print(max(paradigms_arr), 'максимальное схожесть', query)
    return paradigms_arr.index(max(paradigms_arr))


@benchmark
def get_answer_by_rowid(row_id, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT answer FROM my_table WHERE rowid = ?", (row_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print("Ошибка SQLite:", e)
    finally:
        conn.close()


def run(text):
    cur = conect_bd()
    answer_value = get_answer_by_rowid(get_answer(get_all_question_bd(cur), text) + 1, 'horse_database.db')
    return str(answer_value).split(";")[random.randrange(len(str(answer_value).split(";")))]


if __name__ == "__main__":
    cur = conect_bd()
    while True:
        answer_value = get_answer_by_rowid(get_answer(get_all_question_bd(cur), str(input())) + 1, 'horse_database.db')
        if answer_value is not None:
            print("Значение в ячейке: ",
                  str(answer_value).split(";")[random.randrange(len(str(answer_value).split(";")))])
        else:
            print("Значение не найдено.")
