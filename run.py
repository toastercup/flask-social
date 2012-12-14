import os
from rocket import Rocket
from app import app
from app import db

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get('PORT', 5000))
    Rocket((os.environ.get('ADDRESS', '0.0.0.0'), port), 'wsgi', {'wsgi_app': app}).start()
