from flask import Flask, request, render_template
from util import load_candidates_from_json, get_candidate_by_id, get_candidates_by_skill, get_candidates_by_name
from config import PATH

data_json = {}


def run_app():
    app = Flask(__name__)

    @app.route("/")
    def page_index():
        return render_template("index.html", items=data_json)

    @app.route("/candidate/<user_name>")
    def page_candidate(user_name):

        return render_template("single.html", u_name = get_candidates_by_name(user_name) )

    app.run()


if __name__ == '__main__':
    data_json = load_candidates_from_json(PATH)
    run_app()
