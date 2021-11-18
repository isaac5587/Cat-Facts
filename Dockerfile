FROM python:3.9-alpine
WORKDIR /usr/src/app
RUN apk update && apk add ca-certificates
RUN pip install --upgrade pip
RUN pip install flask 
RUN pip install requests
RUN pip install boto3
COPY web.py ./
CMD ["python", "web.py"]
EXPOSE 5000