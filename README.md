# School Management System

A Django-based school management system with REST API capabilities.

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Poetry (for dependency management)
- SQLite
- Poetry

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudomanoj/School-Management-System.git
   cd School-Management-System

2. **Create Virtual environment**
   ```bash
   python -m venv .venv

3. **Install requirements**
   ```bash
   pip install -r requirements.txt

4. **Go to the src folder and create .env file as like .env-sample and migrate and then run server**
   ```bash
   cd src
   python manage.py migrate
   python manage.py runserver