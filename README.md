# A digitization pipeline for a typical Biochemistry Lab

## Description
So this is a complete backend with event based arcihtecture for OCR. In this API a user can input "jpg,jpeg,png,pdfs" and this over the counter OCR will store them accordingly in mongodb after running ocr on each of them. Rigt now testing jpeg,jpeg,png. Later would move onto pdfs. 







## Setup
1. install docker
2. install mongodb
3. install celery
4. Start a rabbitmq server on docker
5. Start a celery worker: "celery -A services.task worker --loglevel=INFO"






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
