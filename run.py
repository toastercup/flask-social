import os

from rocket import Rocket
from social import db, app

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get('PORT', 5000))
    Rocket((os.environ.get('ADDRESS', '0.0.0.0'), port), 'wsgi', {'wsgi_app': app}).start()
