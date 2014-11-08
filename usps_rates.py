import requests as req

api_addr = "http://production.shippingapis.com/ShippingAPI.dll?API=RateV4"
api_user = "183ABSTR1250"

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
</RateV4Request>'''

# package_info must contain the specific fields we want
def make_request_xml(base_xml_string, package_info):
    return base_xml_string.format(**package_info)

test_opts = {
    'api_user' : api_user,
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

testxml3 = '''
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
</RateV4Request>'''

print("\nXML output from make_request_xml:")
xml_formatted = make_request_xml(testxml3, test_opts)
print(xml_formatted)

print("\nResponse Content from USPS with test XML string:")
rate_response = req.post(api_addr, testxml)
print(rate_response.content)

print("\nResponse Content with formatted XML string number 2:")
rate_response2 = req.post(api_addr, xml_formatted)
print(rate_response2.content)


