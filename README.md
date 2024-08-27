# Куда пойти — Москва глазами Артёма

Фронтенд для будущего сайта о самых интересных местах в Москве. Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

[Демка сайта](https://devmanorg.github.io/where-to-go-frontend/).

## Как запустить

* Скачайте код
* Перейдите в каталог проекта с файлом `index.html`
* Запустите веб-сервер
* Откройте в браузере


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Определите переменные окружения. Создайте файл `.env` в каталоге `where_to_go/` и положите туда такой код:
```sh
SECRET_KEY=h9cte7...h$6yte5...Fhchs9y
```
Данные выше приведены для примера. Создайте свой `SECRET_KEY`

В качестве веб-сервера можно использовать что угодно. Например, подойдёт даже самый простой встроенный в Python веб-сервер:

```bash
$ python -m http.server 8000
```

На карту можно посмотреть по ссылке [Карта](https://busypengu1n.pythonanywhere.com/)


В админку можно зайти по ссылке [Админка](https://busypengu1n.pythonanywhere.com/admin/)


## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

