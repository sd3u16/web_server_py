from flask import Flask, render_template, send_from_directory
import os




#render_template allows us to send the html file

app = Flask(__name__)


print(__name__)

#export FLASK_APP=server.py
#flask run
#export FLASK_ENV=development
#name in this case is main because this is the main file


@app.route('/<username>/<post_id>')
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)



@app.route("/about")
def about_page():
    return render_template('./about.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/blog")
def blogs():
    return 'These are my thoughts on blogs'


@app.route("/blog/2020/dogs")
def blog2():
    return 'This is my dog'