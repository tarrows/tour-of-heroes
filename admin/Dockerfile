FROM python:3-alpine3.7

ADD app /admin/app
ADD run.py /admin
ADD requirements.txt /admin

RUN cd /admin && \
  pip install -r requirements.txt && \

WORKDIR "/admin"
ENTRYPOINT ["python", "run.py"]
