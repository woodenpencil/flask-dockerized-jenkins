FROM python:3.6
COPY .  /app
WORKDIR /app

RUN pip3 install -r requirements.txt
# make port 8000 available to the world outside
EXPOSE 8000

CMD ["./src/index.py"]
