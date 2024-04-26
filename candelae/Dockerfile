FROM python

RUN mkdir /candlelae-app
ADD . /candlelae-app

WORKDIR /candlelae-app

RUN pip install -r configs/wsgi/requirements.txt

EXPOSE 9999
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:9999"]