FROM python:3

ADD fizzbuzz.py /

CMD [ "python", "./fizzbuzz.py" ]