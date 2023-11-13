from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
@app.route('/home')
@app.route('/dashboard')
def index():
    # Load the template
    template = open("templates/index.html", "r")
    template_content = template.read()

    # Set the data
    data = {
        "title": "Hello, world!",
    }

    # Render the template
    response = render_template(template_content, **data)

@app.route("/historyAtt", methods=["POST"])
def historyAtt():
    # Collect form data
    name = request.form.get("name")
    position = request.form.get("position")
    type = request.form.get("type")
    date = request.form.get("date")
    clockInHour = request.form.get("clockInHour")
    clockInMinute = request.form.get("clockInMinute")

    # Prepare data object for AJAX request
    data = {
        name: name,
        position: position,
        type: type,
        date: date,
        clockInHour: clockInHour,
        clockInMinute: clockInMinute
    }

    # Submit attendance
    if name is not None and position is not None and type is not None and date is not None and clockInHour is not None and clockInMinute is not None:
        # Success
        response = {"success": True}
    else:
        # Error
        response = {"error": "Incomplete data"}

    return response

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)