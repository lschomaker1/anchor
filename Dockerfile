FROM python:3.9

RUN apt-get update && apt-get install -y default-mysql-client && apt-get install -y python3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
