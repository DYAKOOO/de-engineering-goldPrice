import functions_framework
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@functions_framework.http
def process_pubsub(request):
    """HTTP Cloud Function."""
    logger.info("Cloud Function triggered successfully!")
    return 'OK', 200

