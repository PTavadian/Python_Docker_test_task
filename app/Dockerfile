FROM python:latest


WORKDIR /app


RUN pip install SQLAlchemy

RUN pip install psycopg2


COPY . .

CMD [ "python", "main.py" ]







