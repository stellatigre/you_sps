# this file is the actual http listener and server
import configfile as config
try: import simplejson as json
except ImportError: import json
from flask import Flask, render_template, request, url_for
from usps_lib import save_pdf_from_base64, json_from_dict, get_label, get_shipping_rate
from pprint import pprint

app = Flask(__name__)

@app.route('/label', methods=['POST'])
def label():    
    json_data = json.loads(request.get_data().decode("UTF-8"))
    usps_label, request_dict = get_label(json_data) 
    file_number = response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationNumber']
    pdf_path = save_pdf_from_base64(usps_label, file_number)
    print(pdf_path)
    return config.host + pdf_path


@app.route('/rates', methods=['POST'])
def rates():
    json_data = json.loads(request.get_data().decode("UTF-8"))
    usps_rate_response = json_from_dict(get_shipping_rate(json_data))
    return usps_rate_response

# Run the service
if __name__ == '__main__':
    app.debug = True   
    app.run( 
        host = "0.0.0.0",
        port = int(config.listen_port)
    )

