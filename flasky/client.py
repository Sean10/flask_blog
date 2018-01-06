from flask import Blueprint, redirect
import requests

client = Blueprint('client', __name__)

client_id = '123456'
#users[client_id] = ''
redirect_uri = "http://localhost:5000/passport"

@client.route('/login', methods=['GET', 'POST'])
def login():
    uri = 'http://localhost:5000/oauth'
    return redirect(uri)

# 这里的redirect_uri是什么呢
@client.route('/passport', methods=['GET', 'POST'])
def passport():
    code = requests.args.get('code')
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)
    return redirect(uri)