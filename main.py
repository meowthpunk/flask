from app import socket
from app import app
import os

if __name__ == '__main__':
    socket.run(app, debug=True, port=os.getenv("PORT", default=5000))
