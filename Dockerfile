FROM python:3

ADD ./fizzbuzzMod/fizzbuzz.py /fizzbuzzMod/

ADD main.py /

CMD [ "python", "./main.py" ]