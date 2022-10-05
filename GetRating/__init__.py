import logging
from pydoc import doc
import azure.functions as func

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if not doc:
        logging.warning("ratingId not found")
        return func.HttpResponse(
            "Rating ID Not Found",
            status_code=400
        )
    else:
        logging.info("ratingId Found")
        return func.HttpResponse(
             str(doc[0].to_json()),
             status_code=200
        )
   