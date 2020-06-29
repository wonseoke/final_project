# web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect, request, flash

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    #return "Welcome Home (TODO)"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html")

@home_routes.route("/lookup")
def moving():
    print("VISITED THE ABOUT PAGE")
    #return "Moving Page (TODO)"
    return render_template("lookup.html")

@home_routes.route("/users/new")
def register():
    print("VISITED THE REGISTRATION PAGE")
    return render_template("new_user_form.html")

@home_routes.route("/users/create", methods=["POST"])
def create_user():
    print("FORM DATA:", dict(request.form))
    # FYI: we are able to access the form data via the "request" object we import from flask
    # ... these keys correspond with the "name" attributes of each <input> element in the form!
    #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}

    user = dict(request.form)
    # todo: store in a database or google sheet!

    # FYI: "warning", "primary", "danger", "success", etc. are bootstrap color classes
    # ... see https://getbootstrap.com/docs/4.3/components/alerts/
    # ... and the flash messaging section of the "bootstrap_layout.html" file for more details
    flash(f"User '{user['full_name']}' created successfully! (TODO)", "warning")
    return redirect("/")

@home_routes.route("/inquiry", methods=["POST"])
def create_inquiry():
    print("FORM DATA:", dict(request.form))
    # FYI: we are able to access the form data via the "request" object we import from flask
    # ... these keys correspond with the "name" attributes of each <input> element in the form!
    #> {'email_address': 'me@example.com', 'zip_origin': '#####', 'zip_destination': '#####', 'move_size': 's#'}

    inquiries = dict(request.form)
    # todo: store in a database or google sheet!

    # FYI: "warning", "primary", "danger", "success", etc. are bootstrap color classes
    # ... see https://getbootstrap.com/docs/4.3/components/alerts/
    # ... and the flash messaging section of the "bootstrap_layout.html" file for more details
    flash(f"Quote bid by '{inquiries['email_address']}' created successfully! Please await for a willing mover to contact you", "success")
    return redirect("/")

@home_routes.route("/lookup", methods=["GET", "POST"])
def weather_forecast():
    print("GENERATING A WEATHER FORECAST...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_hourly_forecasts(zip_code)
    print(results.keys())
    return render_template("moving.html", zip_code=zip_code, results=results)
