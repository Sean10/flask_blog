import time
import random
import base64

from flasky import users, auth_code

def gen_token(uid):
    token = base64.b64encode((":".join([str(uid), str(random.random()), str(time.time() + 7200)])).encode('utf-8'));
    users[uid].append(token)
    return token

def verify_token(token):
    _token = base64.b64decode(token).decode()
    if not users.get(_token.split(':')[0][-1]) == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


def gen_auth_code(uri):
    code = random.randint(0, 10000)
    auth_code[code] = uri
    return code