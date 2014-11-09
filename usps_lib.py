import base64
import requests as req
import xmltodict as xml2dict
import xml_templates as xmlt    # these are both local modules 
import configfile as config     # in the same directory
try: import simplejson as json
except ImportError: import json
from pprint import pprint

# package_info must be a dict containing the specific fields we want
def make_request_xml(base_xml_string, package_info):
    return base_xml_string.format(**package_info)

# feed this function xml from make_request_xml
def get_label(package_info):
    package_info_xml = make_request_xml(xmlt.label_xml_base, package_info)
    label_response = req.get(config.label_api_address + package_info_xml)
    label_dict = xml2dict.parse(label_response.content)
    
    #pprint(label_dict)
    try:
        label_image = label_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationLabel']
        return (label_image, label_dict)
    except KeyError as error:
        print("\nsomething went wrong with the request...\n" + error)
        return (None, label_dict)
 
# USPS's api returns data in base64 PDF or TIF - chose PDF
def save_pdf_from_base64(base64_pdf, image_filename):
    filepath = "./pdfs/" + image_filename
    try:
        with open(filepath, "wb") as pdf_image:
            pdf_image.write(base64.b64decode(base64_pdf))
            pdf_image.close()
        return filepath
    except Exception as error:
        print("\nerror saving PDF file...\n" + error)
        return False


# just pass this a dict of the right options, see test data
def get_shipping_rate(package_info):
    package_info['api_user'] = config.api_user
    xml_request = make_request_xml(xmlt.rate_xml_base, package_info)
    rate_response = req.post(config.rate_api_address, xml_request)  # actual request
    response_xml = rate_response.content
    response_dict = xml2dict.parse(response_xml)
    return response_dict


def json_from_dict(input_dict):
    encoder = json.JSONEncoder()
    json_data = encoder.encode(input_dict) 
    return json_data
