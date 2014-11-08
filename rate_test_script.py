import requests as req
import xmltodict as xml2dict
import configfile as config
import xml_templates as xmlt
from usps_lib import make_request_xml, json_from_dict
from pprint import pprint

test_opts = {
    'api_user' : config.api_user,
    'package_id' : '1ST',
    'service' : 'PRIORITY',
    'zip_origin' : 44280,
    'zip_dest' : 20772,
    'pounds' : 25,
    'ounces' : 8,
    'container' : 'NONRECTANGULAR',
    'size' : 'LARGE',
    'width' : 25,
    'length' : 40,
    'height' : 35,
    'girth' : 65
}

rate_request_base = '''
http://production.shippingapis.com/ShippingAPI.dll?API=RateV4&XML=<RateV4Request USERID="{api_user}" >
     <Revision/>
     <Package ID="{package_id}">
          <Service>{service}</Service>
          <ZipOrigination>{zip_origin}</ZipOrigination>
          <ZipDestination>{zip_dest}</ZipDestination>
          <Pounds>{pounds}</Pounds>
          <Ounces>{ounces}</Ounces>
          <Container>{container}</Container>
          <Size>{size}</Size>
          <Width>{width}</Width>
          <Length>{length}</Length>
          <Height>{height}</Height>
          <Girth>{girth}</Girth>
     </Package>
</RateV4Request>
'''

def get_shipping_rate(package_info):
    xml_request = make_request_xml(rate_request_base, package_info)
    rate_response = req.post(config.rate_api_address, xml_request)
    response_xml = rate_response.content
    return response_xml    


print("\nResponse Content from USPS with test XML string:")
rate_response = req.post(config.rate_api_address, xmlt.rate_test_xml)
print(rate_response.content)

print("\nResponse Content with get_shipping_rate:")
rate_response2 = get_shipping_rate(test_opts)
print(rate_response2)
dynamic_returned = json_from_dict(xml2dict.parse(rate_response2), filename="rate_response_2.json")
pprint(dynamic_returned)


