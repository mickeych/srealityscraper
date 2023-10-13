FROM python:latest
WORKDIR /displayserver
COPY . .
RUN pip install flask
RUN pip install psycopg2
EXPOSE 8080
ENTRYPOINT [ "python" ]

CMD ["displayserver.py" ]