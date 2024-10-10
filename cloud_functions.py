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
    # This is for local testing only
    import flask
    import werkzeug.serving

    app = flask.Flask(__name__)
    app.add_url_rule("/", "index", process_pubsub, methods=["GET", "POST"])

    port = int(os.environ.get("PORT", 8080))
    werkzeug.serving.run_simple("localhost", port, app, use_reloader=True)