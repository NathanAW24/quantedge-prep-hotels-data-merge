# FastAPI template

# Setup Environment
Run this one by one, from project root
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Run uvicorn app
Run it from `src` dir, the code is mostly inside the `app`.
```
uvicorn app.main:app --reload
```