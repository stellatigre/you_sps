import base64
import requests as req
import xmltodict as xml2dict
import xml_templates as xmlt    # these are both local modules 
import configfile as config     # in the same directory


# package_info must contain the specific fields we want
def make_request_xml(base_xml_string, package_info):
    return base_xml_string.format(**package_info)

def get_label(package_info):
    label_response = req.get(config.api_address + package_info)
    label_dict = xml2dict.parse(label_response.content)
    label_image_64 = label_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationLabel']
    return (label_image_64, label_dict)

def save_pdf_from_base64(base64_pdf, image_filename):
    with open("./pdfs/" + image_filename, "wb") as image_pdf:
        image_pdf.write(base64.b64decode(base64_pdf))
        image_pdf.close()
    return "./pdfs/label_example.pdf"

label_image, response_dict = get_label(xmlt.test_label)
save_pdf_from_base64(label_image, "new_example.pdf") 
print("Response as a dict:\n" + str(response_dict))
