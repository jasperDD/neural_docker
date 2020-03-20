FROM python:3

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD [ "python3", "/workspace/wsgi.py" ]