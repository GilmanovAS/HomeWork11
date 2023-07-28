from flask import Flask, request, render_template
from config import PATH

def run_app():
    app = Flask(__name__)

    @app.route("/")
    def page_index():
        return render_template("index.html", hi="Go", items=["refer", "ferfer", "refre"])

    app.run()

if __name__ == '__main__':
        run_app()
