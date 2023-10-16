From python:3.8-slim
WORKDIR /weatherapp
COPY . .
RUN pip install django
EXPOSE 80
CMD python manage.py runserver 0.0.0.0:80
