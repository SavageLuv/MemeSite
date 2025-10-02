from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    r = requests.get(url)

    # Safety check
    if r.status_code == 200:
        response = r.json()
        meme_large = response["preview"][-2]
        subreddit = response["subreddit"]
        return meme_large, subreddit
    else:
        # fallback in case API fails
        return None, None


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(debug=True)