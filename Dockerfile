FROM python:3.11.7

WORKDIR /app

# leveraging Docker's layer caching
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
