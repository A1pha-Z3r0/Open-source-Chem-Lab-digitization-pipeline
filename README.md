# UNDER CONSTRUCTION PLEASE MOVE WITH CAUTION

# A digitization pipeline for a typical Biochemistry Lab

## Description
So this is a complete backend with event based arcihtecture for OCR. In this API a user can input "jpg,jpeg,png,pdfs" and this over the counter OCR will store them accordingly in mongodb after running ocr on each of them. Rigt now testing jpeg,jpeg,png. Later would move onto pdfs. 


## Setup
1. install docker
You could follow a yt tutorial like this one: https://www.youtube.com/watch?v=-EXlfSsP49A&t=331s (windows guys get a mac pls :(  )
or
this is the official docker link to help you get started: https://docs.docker.com/desktop/

2. install mongodb
```bash
brew install mongodb-community@8.0
```
Once its successfully installed you could start with project specific setup

3. Clone this repo
```bash
git clone https://github.com/A1pha-Z3r0/Open-source-Chem-Lab-digitization-pipeline.git
```

4. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```

5. Install requirements
```bash 
pip install -r requirements.txt
```

**To start the app and celery**

1. Start a rabbit-mq server on a docker container
```bash
docker run docker run --hostname rabbitmq --name rabbit-mq -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
If already has been created and stopped just do:
```bash
docker start rabbit-mq

# to stop
docker stop rabbit-mq
```
Now to log in to the server open your brave(it's 2025) and paste: http://localhost:15672

2. Start mongodb server
```bash
# make sure mongoDB is started
brew services start mongodb-community@8.0

# ADDITIONAL:
# To stop:
brew services stop mongodb-community@8.0
```

3. Run worker the celery worker
```bash
PYTHONPATH=./src celery -A celery_app worker --loglevel=INFO --queues=processing
```
4. Run celery beat
```bash
PYTHONPATH=./src celery -A celery_app beat --loglevel=info
```

6. Run fastAPI from inside src
```bash
uvicorn main:app --reload
```
```bash
# to kill port usage if its already in use
lsof -i :8000
kill -9 12345

```

## File Structure

The main src folder contains these important folders

```bash 
├── api                             # All the API routes
│   ├── file_upload_routes.py
│   └── keyword_search.py
├── main.py                         # Entry point
├── repositories                    # The DB and its functions
│   ├── db_config.py
│   └── db_utils.py
├── schemas                         # Schema Validators
│   └── validate.py
├── services                        # Main service logic for OCR
│   ├── __init__.py
│   ├── file_upload_to_db.py
│   ├── files_reader.py
│   ├── ocr_pipeline.py
│   ├── ocr.py
│   ├── task.py
│   └── test_normalize.py
└── utils                           # Genral utils for OCR
    ├── __init__.py
    ├── image_preprocess.py
    └── tensor_converter.py
```
