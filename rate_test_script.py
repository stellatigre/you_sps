import requests as req
import xmltodict as xml2dict
import configfile as config
import xml_templates as xmlt
from usps_lib import make_request_xml, json_from_dict, get_shipping_rate
from pprint import pprint

print("\nJSON Response Content from USPS with test XML string:\n")
rate_response = req.post(config.rate_api_address, xmlt.rate_test_xml)
pprint(json_from_dict(xml2dict.parse(rate_response.content)))

print("\nResponse Content with get_shipping_rate and test data:\n")
rate_response2 = get_shipping_rate(xmlt.test_rate_opts)
dynamic_returned = json_from_dict(xml2dict.parse(rate_response2), filename="rate_response_2.json")
pprint(dynamic_returned)


