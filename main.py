from download_file import download_file
from upload_file import upload_file
from getting_versions import getting_versions
import json
import threading

constants = json.load(open(r"settings.json"))

#getting_versions(constants["request_url"])

#file_path, file_name = download_file(constants['universal_url'], constants['path'], constants['user'], constants['token'], '0.16.51', 'alpha', 'win64')

#upload_file(constants["disk_url"], constants["disk_path"], constants["disk_token"], file_path, file_name)

# 1)Аунтификация в ЯД и загрузка на диск В ВИДЕ ФУНКЦИИ. СЕЙЧАС ТЕСТИРОВАНИЕ!!!
# TODO 2)Аунтификация в МЕГА и загрузка на диск
# TODO 3)Проверка на наличие новых версий игры
# 4)Конфиги в виде файлов
# 5)Проверка на сбои и наличие УЖЕ скачанных версий
# 6)Проверка на наличие файлов на диске
# 7)Проверка на целостность файлов(возможно)
# TODO 8)Скомпилировать программу в ехе
