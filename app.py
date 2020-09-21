from flask import Flask, request, redirect
from redis import Redis
import string
import random
import re

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def root(): 
  return 'Working!'

@app.route('/<code>')
def get_code (code): 
  if redis.exists(code): 
    url = redis.get(code)
    return redirect(url, code=302)
  else:
      return 'Code does not exist'

@app.route('/submit', methods=['POST'])
def submit(): 
  if request.method == 'POST':
    url = request.get_json().values()
    if re.match(r"^(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url):
        url_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
        if not redis.exists(url_code): 
          redis.set(url_code, url)
          return url_code 
    else: 
      return 'not a valid url'