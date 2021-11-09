# ConfigParser - ini анализатор для работы и извлечения настроек конфигр. файлов

from configparser import ConfigParser

# Задаем файл, и секцию
def config(filename='database.ini', section='postgresql'):
    # Создаем объект ConfigParser
    parser = ConfigParser()
    # Читаем файл
    parser.read(filename)

    db = {}
    # Получаем секцию postgresql, закидываем в словарь
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(filename, section))
    return db

