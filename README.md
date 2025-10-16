WordScope
📚WordScope — это веб-приложение для анализа английского текста. Пользователь загружает .txt файл, после чего система показывает сколько раз слово входило в txt. Также на сайте есть вкладка "Популярных англ. слов" с фильтром по частям речи.

![Главная страница WordScope](https://raw.githubusercontent.com/kripersi/WordScope/refs/heads/kripersi/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-16%20213227.png)

![Анализ текста](https://raw.githubusercontent.com/kripersi/WordScope/refs/heads/kripersi/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-16%20213258.png)

![Таблица популярных слов](https://raw.githubusercontent.com/kripersi/WordScope/refs/heads/kripersi/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-16%20213242.png)

🚀Возможности
Загрузка текстовых файлов
Частотный анализ слов
Поиск определений и примеров
Фильтрация по частям речи

🛠️Технологии
Django (backend)
HTML, CSS, JavaScript (frontend)
SQLAlchemy и PostgreSQL
AJAX для динамического взаимодействия

Установка
bash
git clone https://github.com/kripersi/WordScope.git
cd WordScope
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Структура проекта
WordScope/ — основной Django-проект
templates/ — HTML-шаблоны
static/ — стили, скрипты, визуальные эффекты
analyzer/ — приложение для обработки текста
popular_words/ — приложение для отображения самых популярных англ. слов
core/ - главная страница(связующая)

🤝 Контакты
Автор: kripersi
Телеграм: @Marpexiz
Gmail: kripersi1123@gmail.com
