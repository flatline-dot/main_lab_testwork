#### main_lab_testwork

#### Run
````python
git clone https://github.com/flatline-dot/main_lab_testwork.git
cd main_lab_testwork
python3 -m venv env
source env\bin\activate
pip install -r requirements.txt
python3 create_db.py
uvicorn app.main:app --host 0.0.0.0 --reload
````

Service on http://localhost:8000/docs
