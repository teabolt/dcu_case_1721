from flask import Flask, render_template, request, make_response, g
from redis import Redis
import os
import socket
import random
import json

option_a = os.getenv('OPTION_A', "Ansible")
option_b = os.getenv('OPTION_B', "Chef")
option_c = os.getenv('OPTION_C', "Puppet")
option_d = os.getenv('OPTION_B', "SaltStack")
hostname = socket.gethostname()
host = os.getenv('POLL_HOST', "0.0.0.0")
port = int(os.getenv('POLL_PORT', "80"))

redis_port = int(os.getenv("REDIS_PORT", "6379"))
redis_hostname = os.getenv("REDIS_HOST", "redis")

app = Flask(__name__)


def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host=redis_hostname, port=redis_port, db=0, socket_timeout=5)
    return g.redis


@app.route("/", methods=['POST', 'GET'])
def hello():
    # for unlimited votes
    # bring the random vote_id generation outside the if statement
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]
    
    vote = None
    if request.method == 'POST':
        redis = get_redis()
        vote = request.form['vote']
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
        hostname=hostname,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True, threaded=True)
