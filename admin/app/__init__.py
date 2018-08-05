import os

from flask import Flask, jsonify


app = Flask(__name__,
    static_folder=os.getcwd() + '/app/public',
    static_url_path='')

app.config.from_pyfile('config.py', silent=True)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/api/v1/hero/<id>', methods=['GET'])
def hero(id):
    if request.method == 'GET':
        return jsonify(get_hero(id)), 200

@app.errorhandler(400)
def bad_request(err):
    return jsonify(error='400 Bad Request'), 400

@app.errorhandler(404)
def page_not_found(err):
    return jsonify(error='404 Page not Found'), 404

@app.errorhandler(500)
def internal_error(err):
    return jsonify(error='500 Internal Error: {}'.format(err)), 500


def get_hero(id):
    """
    mock method
    """
    hero = { "id": id, "name": "Hayato" }
    return hero
