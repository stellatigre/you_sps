import requests as req
import xmltodict as xml2dict
import configfile as config
import xml_templates as xmlt
from usps_lib import make_request_xml, json_from_dict, get_shipping_rate
from pprint import pprint

expected_sample_response_dict = {'RateV4Response': {'Package': {'@ID': '1ST',
                                'ZipOrigination': '44106',
                                'ZipDestination': '20770',
                                'Pounds': '1',
                                'Ounces': '8',
                                'Container': 'NONRECTANGULAR',
                                'Size': 'LARGE',
                                'Zone': '3',
                                'Postage': {'@CLASSID': '1',
                                            'MailService': 'Priority Mail '
                                                           '2-Day&lt;sup&gt;&#8482;&lt;/sup&gt;',
                                            'Rate': '19.90'}}}}

def test_rate_data():
    print("\nJSON Response Content from USPS with test XML string:\n")
    rate_response = req.post(config.rate_api_address, xmlt.rate_test_xml)
    dict_response = xml2dict.parse(rate_response.content)
    json_result = json_from_dict(dict_response)
    pprint(dict_response)
    pprint(json_result)
    assert expected_sample_response_dict == dict_response

test_rate_data()

print("\nResponse Content with get_shipping_rate and test data:\n")
rate_response2 = get_shipping_rate(xmlt.test_rate_opts)
pprint(rate_response2)


