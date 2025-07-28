Datasets:
1. https://www.nist.gov/srd/nist-special-database-19 #handwritten forms to see where txts are and extrat text
2. http://www.iapr-tc11.org/mediawiki/index.php?title=CROHME:_Competition_on_Recognition_of_Online_Handwritten_Mathematical_Expressions # math expression
3. https://www.kaggle.com/datasets/ro101010/math-formula-detection/data # math formula
4. Chemical reactions notes for JEE 

In production: MD5 hash file is a file hash unique for its contents, so you can check if the contents are the same(integrity check)

OCR:
1. Keras-OCR
2. Doctr

### For inkml files(chrome dataste) we have to write a png extraction script to convert the ink strokes to the actual image.


STEP
1. Download dataset and get few datapoints out for fast testing (done)
2. Run libraries and udnerstand the output (done)
# Since the output is soo bad in real datasets for over-the-counter OCR have to train a model
# But I'm first proceeding with the pipeline to get everything up and running
3. How to store and what to store
   3.1 Storing in mongoDB
   3.2 What to store: 
        * doc_type : str
        * Doc : pdf,png,jpeg,jpg
        * Tensors of respective doc : np.array
        * predicted output text : str
        * predicted output doc : pdf,png,jpeg,jpg


4. FastAPI to nicely package everything.

# Tested doctr the accuracy sucks, like its really bad.

1. split a huge pdf into batches(maybe 15 pages per batch)
2. run ocr on it 



# hyperparametr tuning:
1. The number of pages on a batch
2. parallel proceessing
3. 



Important links:
1. To install hardware acceleration on mac for pytorch: https://developer.apple.com/metal/pytorch/
2. Doctr quick start: https://pypi.org/project/python-doctr/
3. OSRA for optical stuctures to smiles: https://cactus.nci.nih.gov/osra/
4. DIETR better than yolo: https://github.com/dnth/DEIMKit (https://arxiv.org/pdf/2412.04234)
5. Database Mongodb: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/

Notes:
1. Sometimes its important to clear attributes after using bc it will live as long as the instance is
2. A small observation where if we do crop an image and send it to an ocr it perfoms slightly better.