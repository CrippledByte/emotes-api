FROM python:3.7.13-alpine
COPY ./ /app
WORKDIR /app
RUN ls -a
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--preload", "--bind", "0.0.0.0:8000", "app:app"]
