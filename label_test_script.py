from usps_lib import save_pdf_from_base64, save_json_from_dict, get_label, make_request_xml

import xml_templates as xmlt
from time import sleep

# this tests if it works with predefined test data
label_image_b64, response_dict = get_label(xmlt.test_label)
save_pdf_from_base64(label_image_b64, "new_example.pdf") 
json_returned = save_json_from_dict(response_dict, "test_label_request_1.json") 
print("JSON data from predefined:\n" + json_returned)
print("\n" + str(xmlt.test_label) + "\n")

sleep(2)

# this tests if it still works as above when we format the string
test_formatted = make_request_xml(xmlt.label_xml_base, xmlt.test_label_opts)
print("\n" + test_formatted)
label_image_b64, response_dict = get_label(test_formatted)
save_pdf_from_base64(label_image_b64, "formatted_request_test.pdf") 
json_returned2 = save_json_from_dict(response_dict, "test_label_request_2.json") 
print("\nJSON data from formatted:\n" + json_returned2)
#print("formatted response dict:\n" + str(response_dict))
