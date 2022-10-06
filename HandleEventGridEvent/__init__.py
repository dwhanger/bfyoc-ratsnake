import json
import logging
import azure.functions as func

def main(event: func.EventGridEvent,orders: bytes):
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)

    logging.info(f'Python Queue trigger function processed {len(orders)} bytes')