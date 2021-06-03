from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/53d041617679298ef80d").json()
post_objects = []
for post in posts:
    post_objs = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_objs)

app = Flask(__name__)


@app.route('/')
def home():
    api_url = "https://api.npoint.io/53d041617679298ef80d"
    response = requests.get(api_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/posts/<num>")
def get_posts(num):
    title = post_objects[int(num) - 1].title
    body = post_objects[int(num) - 1].body
    return render_template("post.html", num=num, title=title, body=body)

if __name__ == "__main__":
    app.run(debug=True)
