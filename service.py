# this file is the actual http listener and server
import configfile as config
try: import simplejson as json
except ImportError: import json
from flask import Flask, render_template, request, url_for
from usps_lib import save_pdf_from_base64, get_label, get_shipping_rate
from pprint import pprint
import db   # local db module

app = Flask(__name__)

@app.route('/label', methods=['POST'])
def label():    
    json_data = json.loads(request.get_data().decode("UTF-8"))
    usps_label, response_dict = get_label(json_data) 
    file_number = response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationNumber']
    pdf_path = save_pdf_from_base64(usps_label, file_number)
    db.label_entry_from_response_dict(response_dict)    

    # if we want to discard the base64 representation instead of forwarding back to requester
    #del response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationLabel'] 

    response_dict['label_url'] = config.host + '/' + pdf_path
    return json.dumps(response_dict)
    


@app.route('/rates', methods=['POST'])
def rates():
    json_data = json.loads(request.get_data().decode("UTF-8"))
    usps_rate_response = get_shipping_rate(json_data)
    db.rate_entry_from_response_dict(usps_rate_response)
    return json.dumps(usps_rate_response)

# Run the service
if __name__ == '__main__':
    app.debug = config.debug   
    app.run( 
        host = "0.0.0.0",
        port = int(config.listen_port)
    )

