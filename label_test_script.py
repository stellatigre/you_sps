from usps_lib import save_pdf_from_base64, json_from_dict, get_label, make_request_xml

import xml_templates as xmlt
from time import sleep

def test_predefined_request():
# this tests if it works with predefined test data
    label_image_b64, response_dict = get_label(xmlt.test_label)
    file_number = response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationNumber']
    save_pdf_from_base64(label_image_b64, file_number + ".pdf") 
    json_returned = json_from_dict(response_dict) 

test_predefined_request()
sleep(2)

# this tests if it still works as above when we format the string to re-insert the same data
test_formatted = make_request_xml(xmlt.label_xml_base, xmlt.test_label_opts)
label_image_b64, response_dict = get_label(test_formatted)
file_number = response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationNumber']
save_pdf_from_base64(label_image_b64, file_number + ".pdf") 
json_returned2 = json_from_dict(response_dict) 
#print("\nJSON data from formatted:\n" + json_returned2)
