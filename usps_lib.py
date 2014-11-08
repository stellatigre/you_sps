import base64
import requests as req
import xmltodict as xml2dict
import xml_templates as xmlt    # these are both local modules 
import configfile as config     # in the same directory
try: import simplejson as json
except ImportError: import json

# package_info must be a dict containing the specific fields we want
def make_request_xml(base_xml_string, package_info):
    return base_xml_string.format(**package_info)


# feed this function xml from make_request_xml
def get_label(package_info_xml):
    label_response = req.get(config.api_address + package_info_xml)
    label_dict = xml2dict.parse(label_response.content)
    try:
        label_image = label_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationLabel']
        return (label_image, label_dict)
    except KeyError as error:
        print("\nsomething went wrong with the request...\n")
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
        print("\nerror saving PDF file...")
        return False


# storing this in the filesystem for purposes
# of providing demo data, could go in a DB easily
def save_json_from_dict(input_dict, filename):
    encoder = json.JSONEncoder()
    json_data = encoder.encode(input_dict)
    #print(json.dumps(input_dict, indent=4, sort_keys=True))
    
    try:
        with open("./json/" + filename, "w") as json_file:
            json_file.write(json_data)
            json_file.close()   
        return json_data
    except:
        return False

