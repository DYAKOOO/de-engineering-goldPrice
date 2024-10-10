import functions_framework
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@functions_framework.http
def process_pubsub(request):
    """HTTP Cloud Function."""
    logger.info("Cloud Function triggered successfully!")
    return 'OK', 200

if __name__ == "__main__":
    # This is for local testing
    import os
    from flask import Flask, request
    app = Flask(__name__)
    
    @app.route("/", methods=["POST"])
    def index():
        return process_pubsub(request)
    
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)