import os

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def index():
    if request.method == "POST" or request.method == "PATCH" or request.method == "DELETE" or request.method == "PUT":
        return redirect(url_for("index"))
    else:
        return render_template("index.html", index_page=True)


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=False)
