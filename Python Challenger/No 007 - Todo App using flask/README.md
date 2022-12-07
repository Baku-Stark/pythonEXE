# Todo App using flask

> **REQUISITOS:**
* Criar um Todo App com Flask.
* Ambiente Virtual
    * `pip install Flask` -> [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)
    * `pip install flask_sqlalchemy` -> [Flask SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
    * `pip install to-requirements.txt` -> [to-Requirements.txt](https://pypi.org/project/to-requirements.txt/)
    * `pip install PyMySQL` -> [PyMySQL](https://pypi.org/project/PyMySQL/)
    * `pip install PyYAML` -> [PyYAML](https://pypi.org/project/PyYAML/)

> **Bibliotecas utilizadas:**
* `from flask import Flask, render_template, url_for, request, redirect`
* `from flask_sqlalchemy import SQLAlchemy`
* `from datetime import datetime`
* `from yaml import load, Loader`
* `import os`

> **Flask Static (img, js, css):**
* [Flask Static](https://flask.palletsprojects.com/en/2.2.x/tutorial/static/)
    * _Exemplo_: `{{ url_for('<pasta static>', filename='<diretório do arquivo>') }}`

> **SASS - Watch:**
* _Compressed Mode:_ `sass -w app\static\sass\style.scss app\static\css\style.css -s compressed`

#

> **YAML Document**
```yaml
runtime: python # ou outra versão de sua máquina

instance_class: F1

env_variables:
  MYSQL_USER: <user_name> # Coloque as informações do MySQL
  MYSQL_PASSWORD: <user_pw> # Coloque as informações do MySQL
  MYSQL_DB: <database_name> # Coloque as informações do MySQL
  MYSQL_HOST: <database_ip> # Coloque as informações do MySQL

handlers:
# Selecionar arquivos referentes ao HTML
#Imagens
- url: /img
  static_dir: static/img

# JavaScript
- url: /script
  static_dir: static/script

# CSS
- url: /styles
  static_dir: static/css
```

> **Pip List*:*

Package | Version
--- | ---
appdata            | 2.1.2
click              | 8.0.3
colorama           | 0.4.6
colored            | 1.4.3
Flask              | 2.2.2
Flask-SQLAlchemy   | 3.0.2
greenlet           | 2.0.1
itsdangerous       | 2.1.2
Jinja2             | 3.1.2
MarkupSafe         | 2.1.1
pip                | 22.3.1
PyMySQL            | 1.0.2
PyYAML             | 6.0
setuptools         | 63.2.0
SQLAlchemy         | 1.4.44
to-requirements.txt| 1.3.0
Werkzeug           | 2.2.2