import toml


def find_toml_header_by_variable(variable_name, filename='config.toml'):
    try:
        with open(filename, 'r') as file:
            data = toml.load(file)
            for section_name, section_data in data.items():
                if variable_name in section_data:
                    return section_name
            return None
    except FileNotFoundError:
        print(f'Файл {filename} не найден.')


# Пример использования функции
# Пусть у нас есть файл config.toml с переменной "HOST" и её значением

# Проверяем наличие заголовка для переменной 'HOST'
header = find_toml_header_by_variable('CHUNK')
if header:
    print('Заголовок для переменной найден:', header)
else:
    print('Заголовок для переменной не найден.')
