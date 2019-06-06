FROM python:alpine
WORKDIR /app
RUN apk update && apk add bash
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["hw.py"]