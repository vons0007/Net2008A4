FROM python:3.11
WORKDIR /code
COPY . .
CMD ["python", "vons0007-a4.py"]