#!flask/bin/python
from src import application

if __name__ == '__main__':
    application.run(host="127.0.0.1", port=9090, debug=True)
