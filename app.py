from flask import *
from flask_mongoengine import MongoEngine, Document
from bson import json_util

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'test'}

db = MongoEngine(app)

class Post(Document):
	author = db.StringField(required=True)
	body = db.StringField(required=True, min_length=0)
	title = db.StringField(required=True, min_length=0)

@app.route('/')
def base():
	return "/posts, GET POST, Gets or creates Post records."

@app.route('/posts', methods=['GET', 'POST'])
def posts():
	if request.method == 'POST':
		post = createPost(request.form['title'], request.form['body'], request.form['author'])
		return jsonify(post)
	else:
		objects = Post.objects
		return jsonify(objects)

def createPost(title, body, author):
	post = Post(title=title, body=body, author=author)
	post.save()
	return post