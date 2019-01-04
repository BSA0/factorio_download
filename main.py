from download_file import download_file
from getting_versions import getting_versions
import json
import threading

const = json.load(open(r"settings.json"))

getting_versions(const['request_url'], const['selector'])

"""file_path, file_name = download_file(const['download_url'],
                                     const['path'],
                                     const['username'],
                                     const['token'],
                                     '0.16.51', 'alpha', 'win64')"""


# 1)Аунтификация в ЯД и загрузка на диск В ВИДЕ ФУНКЦИИ. СЕЙЧАС ТЕСТИРОВАНИЕ!!!
# TODO 2)Аунтификация в МЕГА и загрузка на диск
# TODO 3)Проверка на наличие новых версий игры
# 4)Конфиги в виде файлов
# 5)Проверка на сбои и наличие УЖЕ скачанных версий
# 6)Проверка на наличие файлов на диске
# 7)Проверка на целостность файлов(возможно)
# TODO 8)Скомпилировать программу в ехе
