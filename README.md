# 🧑‍🎓 Django Student Study Portal

This is a **Django-based Student Dashboard** web application that serves as a comprehensive **Student Study Portal**. It combines multiple productivity and learning tools into a single platform to help students manage their academic activities efficiently.

## 🚀 Features

The portal includes the following 8 main sections:

1. 📓 **Notes** – Add, view, and manage personal notes.
2. 📚 **Homework** – Track and update homework assignments.
3. ✅ **To-Do** – Maintain a daily to-do list.
4. 📺 **YouTube** – Search and view educational videos directly.
5. 📖 **Wikipedia** – Fetch and display Wikipedia summaries for quick learning.
6. 📘 **Dictionary** – Get word meanings, phonetics, and examples.
7. 📚 **Books** – Search books using the Google Books API.
8. 🔄 **Conversion Tools** – Perform unit conversions (length, mass, etc.).

## 🧩 Other Features

- 🖥️ **Single Integrated Dashboard**
- 🔐 **User Authentication** (Login/Register/Logout)
- 📱 Responsive UI
- ☁️ Search APIs integrated (YouTube, Wikipedia, Dictionary, Google Books)

## 🔧 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **APIs**: YouTube, Wikipedia, Dictionary, Google Books

## Authentication

The portal features a secure login authentication system to ensure that each student has personalized access to their data and the platform's features.

## ☺️Getting Started🥳

To run this project locally, follow these steps:

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Suhani1934/student-study-portal.git
    cd student-study-portal
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Make migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an administrator account.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the portal:** Open your web browser and navigate to `http://127.0.0.1:8000/`.
