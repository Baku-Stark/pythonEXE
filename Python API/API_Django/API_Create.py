# API - Lugar para disponibilizar recursos
#   1. Objetivo - Criar uma API de disponibilidade de CRUD
#   2. Objetivo - URL base - localhost

#   3. Objetivo - Endpoints
#                   - localhost/livros(GET)
#                   - localhost/livros/id (GET)
#                   - localhost/livros/id (PUT)
#                   - localhost/livros/id (DELETE)

#   4. Objetivo - Quais recursos [LIVROS]

# FRAMEWORK -> DJANGO REST
# https://www.django-rest-framework.org/

# CLONAGEM DE REPOSITÓRIO
# git clone --branch module_1 https://github.com/bobby-didcoding/drf_course.git

# AMBIENTE VIRTUAL -> python -m venv venv
# .\venv\Scripts\activate.bat

# PIP INSTALL (PELO ARQUIVO)
# pip install -r backend\requirements.txt

# django-admin startproject drf_course backend
# copy env.template .env

# =========================== MODULE 2
# python manage.py startapp core

# python manage.py makemigrations
# python manage.py migrate

# python manage.py runserver
#  - http://127.0.0.1:8000/
# =========================== MODULE 2

# =========================== MODULE 3
# drf_course\backend\utils
# drf_course\backend\core\serializers.py

# python manage.py makemigrations
# python manage.py migrate

# [---DOCKER]
# docker-compose up -d --build
# =========================== MODULE 3

# =========================== MODULE 4
# python manage.py test

# [ABRIR O POWER SHELL]
#  - python manage.py shell
#       from core.models import Contact
#       c = Contact.objects.last()
# =========================== MODULE 4

# =========================== MODULE 5
# python manage.py startapp ecommerce

# PEGANDO O TOKEN DO Django Rest
    # INSERIR NO [/drf_course/settings.py]

# python manage.py makemigrations
# python manage.py migrate

# CRIAR [/drf_course/signals.py]

# python manage.py createsuperuser
# =========================== MODULE 5

# =========================== MODULE 6
# CRIAR [serializers.py]
# python manage.py makemigrations
# python manage.py migrate
# =========================== MODULE 6

# =========================== MODULE 7
# python manage.py makemigrations
# python manage.py migrate
# =========================== MODULE 7

# =========================== MODULE 8
# INSERIR CÓDIGO [/ecommerce/tests.py]
# python manage.py test
# =========================== MODULE 8