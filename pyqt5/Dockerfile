FROM python:3

ADD ../fizzbuzzMod/fizzbuzz.py /fizzbuzzMod/

ADD pyqt5fizzbuzz.py /pyqt5/

RUN pip install PyQt5

CMD [ "python", "./pyqt5/pyqt5fizzbuzz.py" ]