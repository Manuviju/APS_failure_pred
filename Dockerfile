FROM python:3.8
COPY . /app
WORKDIR /APP
RUN pip install -r requirements.txt
CMD ["python", "main.py"]