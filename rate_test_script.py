import requests as req
import configfile as config
from usps_lib import make_request_xml

testxml = '''
http://production.shippingapis.com/ShippingAPI.dll?API=RateV4&XML=<RateV4Request USERID="183ABSTR1250" >
     <Revision/>
     <Package ID="1ST">
          <Service>PRIORITY</Service>
          <ZipOrigination>44106</ZipOrigination>
          <ZipDestination>20770</ZipDestination>
          <Pounds>1</Pounds>
          <Ounces>8</Ounces>
          <Container>NONRECTANGULAR</Container>
          <Size>LARGE</Size>
          <Width>15</Width>
          <Length>30</Length>
          <Height>15</Height>
          <Girth>55</Girth>
     </Package>
</RateV4Request>
'''

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

print("\nXML output from get_shipping_rate")
xml_formatted1 = get_shipping_rate(test_opts)
print(xml_formatted1)

print("\nXML output from make_request_xml:")
xml_formatted = make_request_xml(rate_request_base, test_opts)
print(xml_formatted)

print("\nResponse Content from USPS with test XML string:")
rate_response = req.post(config.rate_api_address, testxml)
print(rate_response.content)

print("\nResponse Content with formatted XML string number 2:")
rate_response2 = req.post(config.rate_api_address, xml_formatted)
print(rate_response2.content)


