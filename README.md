# 📚 WordScope

**WordScope** — это веб-приложение для анализа английского текста.  
Загрузите `.txt` файл, и система покажет, сколько раз каждое слово встречается в тексте.  
Кроме того, вы можете просматривать **популярные английские слова** с фильтрацией по частям речи и получать их определения и примеры использования.

---

![Главная страница WordScope](https://raw.githubusercontent.com/kripersi/WordScope/refs/heads/kripersi/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-16%20213227.png)

![Анализ текста](https://raw.githubusercontent.com/kripersi/WordScope/refs/heads/kripersi/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-16%20213258.png)

![Таблица популярных слов](https://raw.githubusercontent.com/kripersi/WordScope/refs/heads/kripersi/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-16%20213242.png)

## 🌐 Основные страницы

### 🏠 Главная страница
Общее описание проекта и навигация по разделам.

### 📊 Анализ текста
- Загрузка `.txt` файла.  
- Подсчет частоты употребления слов.  
- Отображение таблицы с результатами анализа.  
- Возможность поиска и сортировки слов.

### 🔤 Популярные английские слова
- Таблица часто используемых английских слов.  
- Фильтрация по частям речи (существительные, глаголы, прилагательные и т.д.).  
- Возможность поиска и получения примеров использования.

---

## 🚀 Возможности

✅ Загрузка текстовых файлов  
✅ Частотный анализ слов  
✅ Поиск определений и примеров  
✅ Фильтрация по частям речи  
✅ Динамическое взаимодействие без перезагрузки (через AJAX)  

---

## 🛠️ Технологии

**Backend:**  
- 🐍 Django  
- ⚙️ SQLAlchemy  
- 🐘 PostgreSQL  

**Frontend:**  
- 🌐 HTML, CSS, JavaScript  
- ⚡ AJAX (для динамической работы без перезагрузки страницы)  

---

## ⚙️ Установка и запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/kripersi/WordScope.git
cd WordScope

# 2. Создаём и активируем виртуальное окружение
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Применяем миграции
python manage.py migrate

# 5. Запускаем сервер
python manage.py runserver
