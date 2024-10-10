import functions_framework

@functions_framework.http
def process_pubsub(request):
    """HTTP Cloud Function."""
    return 'OK', 200

# No need for __main__ block in production deployment