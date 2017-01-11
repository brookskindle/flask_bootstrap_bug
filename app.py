#!/usr/bin/env python3
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

class DummyPagination:
    """A dummy pagination object with seven "pages" in it. Can be passed to
    Flask Bootstrap in place of an actual pagination object."""
    def __init__(self):
        self.pages = list(range(7))  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        self.page = 3
        self.has_prev = True
        self.prev_num = 2
        self.has_next = True
        self.next_num = 4

    def iter_pages(self):
        return iter(self.pages)


@app.route("/")
def index():
    dummy_pagination = DummyPagination()
    return render_template("index.html", pagination=dummy_pagination)


if __name__ == "__main__":
    app.run(debug=True)
