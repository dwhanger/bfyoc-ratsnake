import logging
from pydoc import doc
import azure.functions as func

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if not doc:
        logging.warning("ToDo item not found")
        return func.HttpResponse(
            "Rating ID Not Found",
            status_code=400
        )
    else:
        logging.info("Found ToDo item, Description=%s",
                     doc[0]['description'])
        return func.HttpResponse(
             str(doc[0]['description']),
             status_code=200
        )
   