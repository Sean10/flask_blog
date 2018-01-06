from flask import Blueprint, redirect,request
import requests

client = Blueprint('client', __name__)

client_id = 'admin'
#users[client_id] = ''
redirect_uri = "http://localhost:5000/client/passport"

@client.route('/login', methods=['GET', 'POST'])
def login():
    uri = 'http://localhost:5000/oauth?response_type=code&client_id=%s&redirect_uri=%s' % (client_id, redirect_uri)
    return redirect(uri)

# 这里的redirect_uri是什么呢
@client.route('/passport', methods=['GET', 'POST'])
def passport():
    code = request.args.get('code')
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)
    return redirect(uri)