FROM python:3.6-slim

# Создание директории в контейнере
RUN mkdir ./Less_Dir
# Копирование всегосодержимого локальной папки в папку root контейнера 
COPY . ./Less_Dir
# Задание рабочего директория
WORKDIR /Less_Dir
# Установка flask
RUN pip install flask gunicorn sklearn numpy

