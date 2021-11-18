from __future__ import annotations
from flask import Flask, jsonify, request
import boto3
import requests
app = Flask(__name__)


client = boto3.client(
    service_name='ses',
    region_name='us-east-1',
    aws_access_key_id="AKIA5ORGZAXP52WYWZ4J",
    aws_secret_access_key="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"
)

@app.route("/send", methods=["POST"])
def send():
    address = request.json.get("address")
    data = requests.get("https://cat-fact.herokuapp.com/facts/random")
    catFact = data.json()["text"]

    if address is None or address == "":
        return {"error": "Please input an email address!"}, 404
    if "@" not in address :
        return {"error": "Please input a valid email address!"}, 400


    response = client.send_email(
        Source='catfacts@csci390.com',
        Destination={
            'ToAddresses': [address]
        },
        Message={
            'Subject': {
                'Data': 'Awesome cat fact for you!',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': catFact,
                    'Charset': 'UTF-8'
                    }      
            }
        }
     
    )
    
    return {}, 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)


