import time
import random
import base64
import json
import hmac

from . import users, auth_code
from functools import wraps
from flask import make_response

TIMEOUT = 3600 * 2
# 新版本token生成器
def gen_token(data):
    '''
    :param uid: dict type
    :return: base64 str
    '''
    data = data.copy()
    if "salt" not in data:
        data["salt"] = str(random.random())
    if "expires" not in data:
        data["expires"] = time.time() + TIMEOUT
    payload = json.dumps(data).encode("utf-8")
    # 生成签名
    sig = _get_signature(payload)
    return encode_token_bytes(payload + sig)
    # token = base64.b64encode((":".join([str(uid), str(random.random()), str(time.time() + 7200)])).encode('utf-8'));
    # users[uid].append(token)
    # return token

# 可以在这个部分中添加,user,将验证的过程也一次实现
def verify_token(token):
    decoded_token = decode_token_bytes(token)
    payload = decoded_token[:-16]
    sig = decoded_token[-16:]
    # 生成签名
    expected_sig = _get_signature(payload)
    if sig != expected_sig:
        return {}
    data = json.loads(payload.decode("utf-8"))
    if data.get('expires') >= time.time():
        return data
    return 0

    # _token = base64.b64decode(token).decode()
    # if not users.get(_token.split(':')[0][-1]) == token:
    #     return -1
    # if float(_token.split(':')[-1]) >= time.time():
    #     return 1
    # else:
    #     return 0

def _get_signature(value):
    """
    :param value:
    :return:
    """
    return hmac.new(b'secret123456', value).digest()

def encode_token_bytes(data):
    return base64.urlsafe_b64encode(data)

def decode_token_bytes(data):
    return base64.urlsafe_b64decode(data)

def gen_auth_code(uri):
    code = random.randint(0, 10000)
    auth_code[code] = uri
    return code

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        print("hee")
        print(fun)
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        print("hee2")
        return rst
    return wrapper_fun