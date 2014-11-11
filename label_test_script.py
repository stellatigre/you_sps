from usps_lib import save_pdf_from_base64, get_label
import json
import xml_templates as xmlt
from time import sleep
from pprint import pprint

#def test_predefined_request():
# this tests if it works with predefined test data
#    label_image_b64, response_dict = get_label(xmlt.test_label)
#    file_number = response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationNumber']
#    save_pdf_from_base64(label_image_b64, file_number + ".pdf") 
#    json_returned = json.dumps(response_dict) 

#test_predefined_request()
#sleep(2)

# this tests if it still works as above when we format the string to re-insert the same data
label_image_b64, response_dict = get_label(xmlt.test_label_opts)
file_number = response_dict['SigConfirmCertifyV4.0Response']['SignatureConfirmationNumber']
save_pdf_from_base64(label_image_b64, file_number + ".pdf") 
pprint(response_dict)
json_returned2 = json.dumps(response_dict) 
print("\nJSON data from formatted:\n" + json_returned2)
