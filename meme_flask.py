from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            response = r.json()
            meme_large = response.get("preview", [None, None])[-2]
            subreddit = response.get("subreddit", "unknown")
            if meme_large:
                return meme_large, subreddit, False  # <-- error=False when success
        return "/static/fallback.jpg", "unknown", True  # <-- error=True when fail
    except Exception:
        return "/static/fallback.jpg", "unknown", True  # <-- error=True when fail


@app.route("/")
def index():
    meme_pic, subreddit, error = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, error=error)

if __name__ == "__main__":
    app.run(debug=True)