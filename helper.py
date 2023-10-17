import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from set_set import constructing
import toml

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6603728925:AAEUyY9-cbtVh9grWCB6pXBDLoYVc5auoYk", parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


async def run_in_async_thread(file_path):
    async def run_file():
        process = await asyncio.create_subprocess_exec('python', file_path)
        await process.communicate()

    asyncio.create_task(run_file())


def find_toml_header_by_variable(variable_name, filename='config.toml'):
    """
    Поиск заголовка (секции) в файле TOML по имени переменной.
    @param filename: Имя файла TOML, в котором осуществляется поиск.
    @param variable_name: Имя
    переменной, для которой ищется соответствующий заголовок.
    @return Имя заголовка (секции) TOML, которому принадлежит указанная переменная.
                     Возвращает None, если заголовок не найден.
    @raise FileNotFoundError: Если файл с указанным именем не найден.
    """
    try:
        with open(filename, 'r') as file:
            data = toml.load(file)
            for section_name, section_data in data.items():
                if variable_name in section_data:
                    return section_name
            return None
    except FileNotFoundError:
        print(f'Файл {filename} не найден.')


def remove_empty_and_whitespace(arr):
    return [item for item in arr if item and item.strip()]


def update_toml_variable(variable_name, new_value, filename='config.toml'):
    """
    Функция загружает данные из TOML файла, обновляет значение переменной, сохраняет обновленные данные обратно в файл.
    @param filename: имя файла
    @param variable_name: значение переменной
    @param new_value: новое значение
    @return:
    """
    try:
        # Загрузка данных из файла
        with open(filename, 'r') as file:
            data = toml.load(file)

        # Обновление значения переменной
        data[find_toml_header_by_variable(variable_name)][variable_name] = new_value

        # Сохранение обновленных данных в файл
        with open(filename, 'w') as file:
            toml.dump(data, file)
        send(f'Переменная {variable_name} успешно обновлена.')
        del data
    except FileNotFoundError:
        send(f'Файл {filename} не найден.')


async def send(text):
    await bot.send_message(6603728925, text)


# Хэндлер на команду /start
@dp.message(Command("setting"))
async def cmd_start(message: types.Message):
    await message.answer(constructing())


@dp.message(Command("change"))
async def cmd_start(message: types.Message):
    mes = remove_empty_and_whitespace(message.text.split(" "))
    try:
        update_toml_variable(mes[1], mes[2])
    except IndexError:
        await message.answer('некорректный формат запроса, запрос должен содержать команду, имя переменной и её '
                             'значение\n  <b>/change {Имя переменной} {Новое значение}</b> ')

    except KeyError:
        await message.answer(f'Переменная с именем "{mes[1]}" не найдена')


@dp.message(Command("run"))
async def cmd_start(message: types.Message):
    await message.answer(main())
    await run_in_async_thread("./main.py")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
