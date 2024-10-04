import os
from kubernetes import client, config

def get_secret(secret_name, key):
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        # We're running in Kubernetes
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        secret = v1.read_namespaced_secret(secret_name, 'default')
        return base64.b64decode(secret.data[key]).decode('utf-8')
    else:
        # We're running locally
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv(key)

# Usage
GOLD_API_KEY = get_secret('api-secrets', 'gold-api-key')
FRED_API_KEY = get_secret('api-secrets', 'fred-api-key')
ALPHA_VANTAGE_API_KEY = get_secret('api-secrets', 'alpha-vantage-api-key')
KAFKA_PASSWORD = get_secret('kafka-secrets', 'kafka-password')