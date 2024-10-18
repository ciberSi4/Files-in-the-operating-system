# Домашнее задание по теме "Файлы в операционной системе".
import os, time

directory = "."
for root, dirs, files in os.walk(directory):
    for file in os.listdir(root): # files:
        filepath = os.getcwd()
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}\n    Путь: {filepath}\n    Размер: {filesize} байт\n'
              f'    Время изменения: {formatted_time}\n    Родительская директория: {parent_dir}')