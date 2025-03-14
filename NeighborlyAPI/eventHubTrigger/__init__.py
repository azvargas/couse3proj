import json
import logging
import azure.functions as func


#    logging.info('Function triggered to process a message: ', event.get_body())
#    logging.info('  EnqueuedTimeUtc =', event.enqueued_time)
#    logging.info('  SequenceNumber =', event.sequence_number)
#    logging.info('  Offset =', event.offset)
    
def main(event: func.EventGridEvent):

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })


    logging.info('Python EventGrid trigger processed an event: %s', result)
