import functions_framework
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@functions_framework.http
def process_pubsub(request):
    """HTTP Cloud Function."""
    logger.info("Cloud Function triggered successfully!")
    logger.info(f"Environment variables: {os.environ}")
    return 'OK', 200

if __name__ == "__main__":
    # This is for local testing
    import flask

    app = flask.Flask(__name__)
    app.register_blueprint(functions_framework.create_app(target_function=process_pubsub))

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)