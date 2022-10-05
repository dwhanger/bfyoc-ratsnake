import logging
from pydoc import doc
import azure.functions as func

def main(req: func.HttpRequest, docs: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if not docs:
        logging.warning("userId not found")
        return func.HttpResponse(
            "UserID Not Found",
            status_code=400
        )
    else:
        logging.info("userId Found")
        return func.HttpResponse(
             str(dir(docs)), #.to_json()),
             status_code=200
        )
   