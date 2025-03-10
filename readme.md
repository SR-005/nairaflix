# NAIRAFLIX - Theater Management System

## 📌 Overview

**NAIRAFLIX** is a **Theater Management System** designed to streamline operations such as movie display, ticket booking, and analytics. The system is developed using **Python** for the backend, **Tkinter** and **Pillow** for GUI development, and **SQL** for data storage.

## 🛠️ Features

- 🎫 **Ticket Booking System** - Book tickets for available movies (cancellation not supported).
- 🎬 **Movie Display** - View available movies with details and posters.
- 📅 **Showtime Scheduling** - Organize movie schedules efficiently.
- 👥 **User and Admin Login** - Separate access for users and administrators.
- 🖼️ **GUI Interface** - User-friendly interface built with Tkinter and Pillow (used for background images).

## 💻 Technologies Used

- **Python** - Backend logic
- **Tkinter** - GUI development
- **Pillow** - Image processing (background images)
- **SQLite/MySQL** - Database management

## 🚀 Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Tkinter (Use `pip install tk` if not pre-installed)
- Python (>=3.8)
- Required Python libraries: `tkinter`, `pillow`, `sqlite3` or `mysql-connector-python`

### Steps to Install

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/NAIRAFLIX.git
   cd NAIRAFLIX
   ```
2. **Install dependencies**
   ```bash
   pip install pillow mysql-connector-python
   ```
3. **Run the application**
   ```bash
   python main.py
   ```

## 🏗️ Database Configuration

- The system has an **inbuilt SQL query** to set up the database automatically.
- However, you need to **edit the username and password** in the query inside `main.py` before running the application.
- Locate the database connection section in `main.py` and update:
  ```python
  connection = mysql.connector.connect(
      host="localhost",
      user="your_username",
      password="your_password",
      database= #same
  )
  ```

## 📸 Screenshots

*(Add screenshots of your UI here)*

## 🤝 Contributing

Feel free to contribute to the project! You can:

- Report bugs
- Suggest new features
- Improve documentation

## 📜 License

This project is licensed under the **MIT License**.

---

### 🔗 Connect with Me

- GitHub: [yourusername](https://github.com/yourusername)
- LinkedIn: [yourprofile](https://linkedin.com/in/yourprofile)


