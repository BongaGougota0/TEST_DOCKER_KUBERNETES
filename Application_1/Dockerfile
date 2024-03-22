FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY app.py 
# RUN chmod a+x boot.sh

ENV FLASK_APP app.py
# RUN flask translate compile

EXPOSE 5000
# ENTRYPOINT ["./boot.sh"]
