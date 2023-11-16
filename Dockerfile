FROM python:3.10-alpine

WORKDIR /usr/local/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

COPY . .

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000" ]