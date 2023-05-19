FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
COPY ./ .
WORKDIR ./mining_bot
CMD ["python", "-u", "main.py"]