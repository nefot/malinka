import os
import sqlite3
from loger import get_logger

logger = get_logger(__name__)
import pandas as pd

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

