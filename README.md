# Проект Учет Сельхоз земель 

Выполнен в качестве тестового задания в компанию ОсОО Санарип Долбоор.

# Стек
<li>Django
<li>DRF
<li>GeoDjango
<li>Django Leaflet
<li>Postgres
<li>Docker


# Установка и запуск
1. Склонируйте репозиторий

2. Перейдя в директорию с проектом создайте файл .env и заполните по примеру:

```
SECRET_KEY=your_django_project_secret_key
DEBUG=1 (будет установлен в True)

POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_HOST=db
DATABASE=postgres
```

3. Чтобы запустить проект выполните:

```
docker compose up --build -d
```

4. Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin
<li>логин: admin 
<li>пароль: admin

Пароли ко всем созданным пользователям такие же как их юзернеймы

5. Доступные API урлы:
<li>http://localhost:8000/api-geo/v1/plots/ - список земель фермера
<li>http://localhost:8000/api-geo/v1/plots/id/ - детальный просмотр и изменение
<li>http://localhost:8000/api-geo/v1/cultures/ - список культур
