import logging
import requests
import azure.functions as func
import uuid
import datetime
import json

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    userId = req_body.get('userId')
    userIdResponse = requests.get(f"https://serverlessohapi.azurewebsites.net/api/GetUser?userId={userId}")
    if userIdResponse.status_code == 200:
        logging.info('userId verified')
    else:
        return func.HttpResponse(
             "This user Id is not valid",
             status_code=400
        )
    productId = req_body.get('productId')
    productIdResponse = requests.get(f"https://serverlessohapi.azurewebsites.net/api/GetProduct?productId={productId}")
    if productIdResponse.status_code == 200:
        logging.info('productId verified')
    else:
        return func.HttpResponse(
             "This product Id is not valid",
             status_code=400
        )
    locationName = req_body.get('locationName')
    rating = req_body.get('rating')
    if rating in range(1,6):
        logging.info('rating within range')
    else:
        return func.HttpResponse(
             "Please supply a proper value for rating",
             status_code=400
        )
    userNotes = req_body.get('userNotes')
    id = uuid.uuid4()
    dt = datetime.datetime.utcnow()
    my_dict = {
        "id": str(id),
        "userId": str(userId),
        "productId": str(productId),
        "timestamp": str(dt),
        "locationName": str(locationName),
        "rating": str(rating),
        "userNotes": str(userNotes)
    }
    my_json = json.dumps(my_dict)
    logging.info(my_json)
    doc.set(func.Document.from_json(my_json))  
    return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
    )
