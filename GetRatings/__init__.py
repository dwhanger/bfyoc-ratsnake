import logging
from pydoc import doc
import azure.functions as func
import json

def main(req: func.HttpRequest, docs: func.DocumentList) -> func.HttpResponse:
    userId = req.params.get('userId')
    logging.info('Python HTTP trigger function processed a request.')
    if not docs:
        logging.warning("userId not found")
        return func.HttpResponse(
            "UserID Not Found",
            status_code=400
        )
    else:
        logging.info("userId Found")
        output=[]
        for doc in docs:
            output.append(doc.to_json())
        logging.info(str(output))
        return func.HttpResponse(
            str(output),  
            status_code=200
        )