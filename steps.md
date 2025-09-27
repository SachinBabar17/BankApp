
##############################
# Full Console Commands for Running Banking App
##############################

##############################
# Option A — PostgreSQL (Recommended)
##############################

# 1. Install PostgreSQL

## macOS
brew install postgresql
brew services start postgresql

## Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql

## Windows
# Download & install PostgreSQL:
# https://www.postgresql.org/download/windows/
# Then open pgAdmin or Command Prompt

# 2. Create Database & User
sudo -u postgres psql

# Inside PostgreSQL prompt:
CREATE DATABASE banking_db;
CREATE USER banking_user WITH PASSWORD 'your_password';
ALTER ROLE banking_user SET client_encoding TO 'utf8';
ALTER ROLE banking_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE banking_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE banking_db TO banking_user;
\q

# 3. Set Environment Variable
# Edit .env file inside your backend folder:
DATABASE_URL=postgresql://banking_user:your_password@localhost:5432/banking_db

# 4. Setup Backend
cd backend
python -m venv venv

# Activate virtual environment:
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

# 5. Run Backend
uvicorn app.main:app --reload

# Backend runs at:
# http://127.0.0.1:8000

# 6. Run Frontend
cd ../frontend
npm install
npm start

# Frontend runs at:
# http://localhost:3000


##############################
# Option B — SQLite (Easiest for First Time Testing)
##############################

# 1. Change Database URL
# Edit .env file in backend/:
DATABASE_URL=sqlite:///./banking_db.sqlite3

# 2. Setup Backend
cd backend
python -m venv venv

# Activate virtual environment:
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

# 3. Run Backend
uvicorn app.main:app --reload

# Backend runs at:
# http://127.0.0.1:8000
# This creates banking_db.sqlite3 file automatically

# 4. Run Frontend
cd ../frontend
npm install
npm start

# Frontend runs at:
# http://localhost:3000

##############################
# Tip:
# For quick testing use Option B (SQLite).
# For production or real app development use Option A (PostgreSQL).
##############################
