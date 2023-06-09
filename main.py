from flask import Flask, redirect, url_for, session, request, render_template
from db_scripts import *
from settings import *
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("about.html")


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if "AUTH" in session:
        return redirect(url_for("index"))

@app.route('/post/category/<category_name>', methods=['POST', 'GET'])
def postCategory(category_name):
    category_id = getIdByCategory(category_name)





    posts = getPostsByCategory(category_name)

    return render_template('post_category.html', category_name=category_name, posts=posts, category_id=category_id)


@app.route('/about')
def about():
    return "<h1>About</h1>"


app.config['SECRET_KEY'] = "VerySecretKey"

if __name__ == "__main__":
    app.run(debug=True, port=5000)