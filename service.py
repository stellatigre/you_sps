# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import configfile as config

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET']))
def hey():
    return "hey qt"

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/rates', methods=['POST'])
def rates():
    json_data = request.get_data()
    print(json_data)
    return "swag\n"
    #return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host = "0.0.0.0",
        port = int(config.listen_port)
  )

