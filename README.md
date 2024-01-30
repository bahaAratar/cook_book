# Приложение "Поварская Книга"
## Описание
Небольшое приложение на Django для управления поварской книгой. Позволяет добавлять продукты, создавать рецепты и отслеживать количество использования продуктов.

## Содержание
- [Технологии](#Технологии)
- [Установка](#Установка)
- [Админка](#Админка)
- [Пример создания продуктов и рецептов](#Пример-создания-продуктов-и-рецептов)
- [HTTP функции](#HTTP-функции)
- [Вывод](#Вывод)
## Технологии
- Django
- DRF
- PostgreSQL
## Установка
```sh
git clone https://github.com/bahaAratar/cook_book.git
cd cook_book
pip install requirements.txt
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py runserver
```
## Админка
Админка доступна по адресу http://localhost:8000/admin/. Здесь можно управлять продуктами и рецептами.
## Пример создания продуктов и рецептов
### Через админскую панель
### Через консоль Python:
```python
# Создаем продукты
product_tvorog = Product.objects.create(name='Творог')
product_yayco = Product.objects.create(name='Яйцо')
product_sahar = Product.objects.create(name='Сахар')
product_shokolad = Product.objects.create(name='Шоколад')

# Создаем рецепты
recipe_syrnik = Recipe.objects.create(name='Сырник')
recipe_chocolate_omelette = Recipe.objects.create(name='Шоколадный омлет')
```
## HTTP функции
```
http://localhost:8000/book/add_product_to_recipe/recipe_id/product_id/weight/
#
http://localhost:8000/book/cook_recipe/product_id/
#
http://localhost:8000/book/show_recipes_without_product/product_id/
#
```
## Вывод
Приложение "Поварская Книга" позволяет управлять продуктами и рецептами, а также выполнять различные операции через HTTP функции. Админка обеспечивает удобный интерфейс для редактирования данных. Примеры создания продуктов и рецептов через админку и консоль Python позволяют быстро настроить систему для проверки функциональности.
