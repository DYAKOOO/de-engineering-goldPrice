import functions_framework
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@functions_framework.http
def process_pubsub(request):
    """HTTP Cloud Function."""
    logger.info("Cloud Function triggered successfully!")
    return 'OK', 200

# This is for local testing
if __name__ == "__main__":
    from flask import Flask, request
    app = Flask(__name__)
    
    @app.route("/", methods=["POST"])
    def index():
        return process_pubsub(request)
    
    app.run(host="localhost", port=8080, debug=True)