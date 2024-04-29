FROM python:slim
LABEL maintainer="hi@jingwang.me"
RUN python -m venv /venv
COPY . /src
workdir /src
RUN /venv/bin/pip install -r requirements.txt
RUN /venv/bin/python  manage.py makemigrations
RUN /venv/bin/python  manage.py migrate 
EXPOSE 8000
ENTRYPOINT ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

