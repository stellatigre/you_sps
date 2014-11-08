# this file is the actual http listener and server
import configfile as config
try: import simplejson as json
except ImportError: import json
from flask import Flask, render_template, request, url_for
from usps_lib import save_pdf_from_base64, json_from_dict, get_label

app = Flask(__name__)

@app.route('/label', methods=['GET'])
def label():    
    return "label route stub"


@app.route('/rates', methods=['POST'])
def rates():
    json_data = json.loads(request.get_data())
    print(str(json_data))
    
    return "swag, it works\n"

# Run the application
if __name__ == '__main__':
  app.run( 
        host = "0.0.0.0",
        port = int(config.listen_port)
  )

