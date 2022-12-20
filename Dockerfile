FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install python-multipart
RUN pip install -r requirements.txt
CMD ["python", "main.py"]