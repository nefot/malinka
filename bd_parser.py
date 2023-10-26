import random
import sqlite3
import pandas as pd


def remove_empty_elements(input_list):
    processed_list = [element for element in input_list if element.strip() != '']
    return processed_list


def connect_bd():
    conn = sqlite3.connect('horse_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    cursor.close()
    # Загрузка данных из Excel
    df = pd.read_excel('bd.xlsx')

    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    print(df)
    # Загрузка данных в базу данных SQLite
    df.to_sql('my_table', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()


connect_bd()


# Функция для поиска ответа на вопрос в базе данных
def find_answer(question, database_path):
    try:
        # Устанавливаем соединение с базой данных
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Выполняем SQL-запрос для поиска ответа на вопрос
        query = "SELECT answer FROM my_table WHERE LOWER(question) LIKE '%' || LOWER(?) || '%'"

        cursor.execute(query, (question.lower(),))

        # Получаем результат запроса
        result = cursor.fetchone()

        # Закрываем соединение с базой данных
        conn.close()

        if result:
            list = remove_empty_elements(result[0].split(";"))
            return list[random.randint(0, len(list) - 1)]  # Возвращаем найденный ответ
        else:
            question = question.capitalize()

            return find_answer(question, database_path)
    except RecursionError:
        print(question)
        return "Задайте вопрос корректнее"


# Задаем путь к базе данных
database_path = "horse_database.db"

# Задаем вопрос, который мы ищем
search_question = "Где выход?"

# Вызываем функцию поиска ответа
answer = find_answer(search_question, database_path)

# Выводим результат
print(f"Ответ на вопрос '{search_question}': {answer}")
