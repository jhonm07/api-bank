FROM python:3.8-slim
WORKDIR /app
COPY ./app /app
RUN pip install -r requirements.txt
RUN pytest test_app.py
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
