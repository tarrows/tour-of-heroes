import os

app = Flask(__name__,
    static_folder=os.getcwd() + '/app/public',
    static_url_path='')

app.config.from_pyfile('config.py', silent=True)

@app.route('/')
def root:
    return app.send_static_file('index.html')
