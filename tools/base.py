import time
import requests

def retry_request(func, retries=3, delay=2):
    last_exception = None

    for attempt in range(retries):
        try:
            return func()
        except requests.RequestException as e:
            last_exception = e
            time.sleep(delay)

    return {"error": str(last_exception)}
