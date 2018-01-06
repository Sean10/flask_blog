import time
import random
import base64

from flasky import users

def gen_token(uid):
    token = base64.b64encode((":".join([str(uid), str(random.random()), str(time.time() + 7200)])).encode('utf-8'));
    users[uid].append(token)
    return token

def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0][-1]) == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


