from flask import Flask
import modules.db_functions as dbf
from modules.create_db import create_db
from json import dumps


app = Flask(__name__)


@app.route('/')
def index():
    return dumps('Flask app!')


@app.route('/categories')
def get_categories():
    return dumps(dbf.categories_all())


@app.route('/category/<string:name>')
def get_category(name):
    return dumps(dbf.find_category(name))


@app.route('/register/<int:user_id>')
def reg_user(user_id):
    return dumps(dbf.register_user(user_id))


@app.route('/subs/<int:user_id>')
def get_subs(user_id):
    return dumps(dbf.user_subscribes(user_id))


@app.route('/sub/<int:user_id>/<int:category_id>')
def user_subscribe(user_id, category_id):
    return dumps(dbf.subscribe(user_id, category_id))


@app.route('/unsub/<int:user_id>/<int:category_id>')
def user_unsubscribe(user_id, category_id):
    return dumps(dbf.unsubscribe(user_id, category_id))


@app.route('/get_news/<string:category>')
def get_news(category):
    return dbf.fetch_news(category, 10)


if __name__ == '__main__':
    create_db()
    app.run(debug=True)
