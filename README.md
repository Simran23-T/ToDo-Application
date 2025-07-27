readme_content = """
# 📝 Django To-Do List App

A simple task management web application built with **Django**, allowing users to add, mark complete, and delete tasks. Styled with custom **CSS**.

---



---

## 🚀 Features

- ✅ Add new tasks  
- ✅ Mark tasks as completed  
- ✅ View pending and completed tasks separately  
- ✅ Delete tasks  
- 🎨 Styled with external CSS

---

## 🛠 Tech Stack

- Python 3.x  
- Django 5.2  
- HTML/CSS  
- SQLite (default Django DB)

---

##  Project Structure


todo_main/
│
├── todo_main/ # Project settings
│ └── settings.py
│
├── todo/ # App for task management
│ ├── migrations/
│ ├── templates/
│ │ └── home.html
│ ├── static/
│ │ └── css/
│ │ └── style.css
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── manage.py
└── db.sqlite3


---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

##2. python -m venv env
source env/bin/activate  # On Windows use `env\\Scripts\\activate`


###3. Install Dependencies
pip install django

#4. Run Migrations
python manage.py makemigrations
python manage.py migrate


#5. Start the Server
python manage.py runserver



