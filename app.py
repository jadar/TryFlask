from flask import *
from flask_mongoengine import MongoEngine, Document
from bson import json_util
import os 

if 'MONGODB_URI' in os.environ.keys():
	mongo_uri = os.environ['MONGODB_URI']
else:
	mongo_uri = 'localhost'
print(mongo_uri)

# Create Flask app.
app = Flask(__name__)

# Configure the database.
app.config['MONGODB_SETTINGS'] = {
	'db': 'test',
	'host': mongo_uri
}
db = MongoEngine(app)

# Define a Post object for the database.
class Post(Document):
	author = db.StringField(required=True)
	body = db.StringField(required=True, min_length=0)
	title = db.StringField(required=True, min_length=0)

# Define a root route. (Say that 10x quick..)
@app.route('/')
def base():
	return "/posts, GET POST, Gets or creates Post records."

# Define a 'posts' route which can create posts and return a list of all posts (in JSON).
@app.route('/posts', methods=['GET', 'POST'])
def posts():
	if request.method == 'POST':
		post = createPost(request.form['title'], request.form['body'], request.form['author'])
		return jsonify(post)
	else:
		objects = Post.objects
		return jsonify(objects)

# Helper method to create posts.
def createPost(title, body, author):
	post = Post(title=title, body=body, author=author)
	post.save()
	return post