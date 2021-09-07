# sample-api
Sample Rest API with 2 endpoints built with Fast API https://fastapi.tiangolo.com/

The first endpoint is a simple hello world 
```bash
localhost:8000/
```
The second is a redirect with a basic logic inside
```bash
localhost:8000/learning/${VAR}
```

# How to

Create a python environment
```bash
python3 -m venv . 
source bin/activate
pip3 install -r requirements.tx 
uvicorn main:app --reload 
```