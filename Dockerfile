FROM python:3.7-slim

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
COPY mining_bot/ /app
WORKDIR /app
CMD ["python", "-u', "main.py"]