from datetime import datetime

def datestring():
    return datetime.now().strftime('%Y-%m-%dT%H-%M-%SZ')
