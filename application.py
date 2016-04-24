from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""
    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application():
    """application form"""
    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def confirmation():
    """presents confirmation of submittal"""
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    pay = request.form.get("salary")
    job_title = request.form.get("position")

    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salary=pay,
                            position=job_title)


if __name__ == "__main__":
    app.run(debug=True)
