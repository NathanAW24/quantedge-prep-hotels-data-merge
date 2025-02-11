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

# FOR SHORT
The main logic is in `src/app/services/mergeHotels.py`, this is where the APIs written in `src/app/utils/fetchSupplier.py` are fetched from, then the merging logic is done.