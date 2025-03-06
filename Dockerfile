FROM python:3.11-slim

ENV TZ="Asia/Bangkok"

ADD requirements.txt ./

# Update pip first
RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . ./src

WORKDIR ./src

CMD ["python", "main.py"]