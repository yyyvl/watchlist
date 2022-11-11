import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app
from gevent.pywsgi import WSGIServer

http_server = WSGIServer(("0.0.0.0", 5000), app)
http_server.serve_forever()
