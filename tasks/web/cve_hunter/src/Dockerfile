FROM mongo:latest

# Установка Python и Supervisor
RUN apt-get update && apt-get install -y python3 python3-pip supervisor && \
    python3 -m pip install --upgrade pip

# Установка Flask и pymongo (используйте актуальные версии)
RUN pip3 install Flask==3.0.2 pymongo==4.6.3 python-dotenv==1.0.1

# Создание каталогов для Supervisor
RUN mkdir -p /var/log/supervisor

# Копирование приложения и конфигурационных файлов в контейнер
COPY ./app /app
COPY ./loader.py /loader.py
COPY ./run.py /run.py
COPY ./.env /.env
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Открытие порта для Flask приложения
EXPOSE 8000

# Запуск Supervisor, который в свою очередь запустит MongoDB и ваше Python приложение
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
