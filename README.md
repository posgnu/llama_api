# LLaMA
## Run API server
Create `pyllama_data` directory and download the model weight into it. 

Install dependencies
```sh
pip install -r requirements.txt
```

Install pyllama
```sh
pip install pyllama
```

Run api server
```sh
uvicorn main:app
```

Test api server
```sh
python test.py
```
