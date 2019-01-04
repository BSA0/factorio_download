from download_file import download_file
from getting_versions import getting_versions
import json
import os

if not os.path.exists(r"settings.json"):
    json_config = open(r"settings.json", 'w')
    json.dump(json.load(r"example_settings.json"), json_config)
    json_config.close()
    print('Please, configure settings.json according to the instructions')
    exit(0)

const = json.load(open(r"settings.json"))

version = getting_versions(const['request_url'], const['selector'])

if version != 'None':
    for distro in ['win64', 'osx', 'linux64']:
        file_path, file_name = download_file(const['download_url'],
                                             const['path'],
                                             const['username'],
                                             const['token'],
                                             version, 'alpha', distro)
        



# 1)Аунтификация в ЯД и загрузка на диск В ВИДЕ ФУНКЦИИ. СЕЙЧАС ТЕСТИРОВАНИЕ!!!
# TODO 2)Аунтификация в МЕГА и загрузка на диск
# TODO 3)Проверка на наличие новых версий игры
# 4)Конфиги в виде файлов
# 5)Проверка на сбои и наличие УЖЕ скачанных версий
# 6)Проверка на наличие файлов на диске
# 7)Проверка на целостность файлов(возможно)
# TODO 8)Скомпилировать программу в ехе
