FROM python
ADD requirements.txt /code/
ADD wsgi/*.py /code/
ADD wsgi/run_app.sh /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["/bin/bash","-c","./run_app.sh"]
#EXPOSE 8000