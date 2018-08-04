import sys
from app import app

def main(argv):
    app.run(host=app.config['HOST'], port=app.config['PORT'], threaded=True)

if __name__ == "__main__":
    main(sys.argv)
