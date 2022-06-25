FROM python:3.8.5-alpine

# Setting work directory
WORKDIR /app

# Adding all required files to /app folder
ADD . /app

# Installing reuqired dependencies
RUN pip install -r requirements.txt


CMD ["python","app.py"]
