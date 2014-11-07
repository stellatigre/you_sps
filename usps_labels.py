import requests as req

api_addr = "https://secure.shippingapis.com/ShippingAPI.dll?API=SignatureConfirmationCertifyV4&XML="
api_user = "564ORDOR2223"


# package_info must contain the specific fields we want
def make_request_xml(base_xml_string, package_info):
    return base_xml_string.format(**package_info)

test_opts = {
    'api_user' : api_user,
    'from_address1' : '2000 E 9th street',
    'from_address2' : 'apt #b',
    'from_city' : 'Austin',
    'from_state' : 'Texas',
    'from_zip5' : 78702
}

test_xml = '''
<?xml version="1.0" encoding="UTF-8" ?>

<SigConfirmCertifyV4.0Request USERID="564ORDOR2223" PASSWORD="XXXXXX">

  <Revision>2</Revision>

  <ImageParameters />

  <FromName>John Doe</FromName>

  <FromFirm>USPS</FromFirm>

  <FromAddress1>RM 2100</FromAddress1>

  <FromAddress2>475 Enfant Plaza SW</FromAddress2>

  <FromCity>Washington</FromCity>

  <FromState>DC</FromState>

  <FromZip5>20260</FromZip5>

  <FromZip4/>

  <ToName>Janice Dickens</ToName>

  <ToFirm>XYZ Corporation</ToFirm>

  <ToAddress1>Ste 100</ToAddress1>

  <ToAddress2>2 Massachusetts Ave NE</ToAddress2>

  <ToCity>Washington</ToCity>

  <ToState>DC</ToState>

  <ToZip5>20212</ToZip5>

  <ToZip4 />

  <ToPOBoxFlag></ToPOBoxFlag>

  <WeightInOunces>10</WeightInOunces>

  <ServiceType>Priority</ServiceType>

  <SeparateReceiptPage>False</SeparateReceiptPage>

  <POZipCode>20770</POZipCode>

  <ImageType>TIF</ImageType>

  <AddressServiceRequested>False</AddressServiceRequested>

  <HoldForManifest>N</HoldForManifest>

  <Container>NONRECTANGULAR</Container>

  <Size>LARGE</Size>

  <Width>7</Width>

  <Length>20.5</Length>

  <Height>15</Height>

  <Girth>60</Girth>

  <ReturnCommitments>true</ReturnCommitments>

 </SigConfirmCertifyV4.0Request>
'''


base_request = '''
    <?xml version="1.0" encoding="UTF-8" ?>
      <ExpressMailLabelCertifyRequest  USERID="{api_user}">
        <Option />
        <Revision>2</Revision>
        <EMCAAccount />
        <EMCAPassword />
        <ImageParameters />
        <FromFirstName>Adam</FromFirstName>
        <FromLastName>Smith</FromLastName>
        <FromFirm/>
    <FromAddress1>{from_address1}</FromAddress1>
    <FromAddress2>{from_address2}</FromAddress2>
    <FromCity>{from_city}</FromCity>
    <FromState>{from_state}</FromState>
    <FromZip5>{from_zip5}</FromZip5>
    <FromZip4/>
        <FromPhone>2125551234</FromPhone>
    <ToFirstName>Janice</ToFirstName>
    <ToLastName>Dickens</ToLastName>
    <ToFirm>XYZ Corporation</ToFirm>
    <ToAddress1>Ste 100</ToAddress1>
    <ToAddress2>2 Massachusetts Ave NE</ToAddress2>
    <ToCity>Washington</ToCity>
    <ToState>DC</ToState>
    <ToZip5>20212</ToZip5>
    <ToZip4 />
        <ToPhone>2125551234</ToPhone>
        <WeightInOunces>105</WeightInOunces>
        <FlatRate/>
        <SundayHolidayDelivery/>
        <StandardizeAddress/>
        <WaiverOfSignature/>
        <NoHoliday/>
        <NoWeekend/>
        <SeparateReceiptPage/>
        <POZipCode>20212</POZipCode>
        <FacilityType>DDU</FacilityType>
        <ImageType>PDF</ImageType>
        <LabelDate>10/19/2010</LabelDate>
        <CustomerRefNo/>
        <SenderName>Adam Smith</SenderName>
        <SenderEMail>asmith@email.com</SenderEMail>
        <RecipientName>Janice Dickens</RecipientName>
        <RecipientEMail>jdickens@email.com</RecipientEMail>
        <HoldForManifest/>
        <CommercialPrice>false</CommercialPrice>
        <InsuredAmount>425.00</InsuredAmount>
        <Container>NONRECTANGULAR</Container>
        <Size>LARGE</Size>
        <Width>7</Width>
        <Length>20.5</Length>
        <Height>15</Height>
        <Girth>60</Girth>
      </ExpressMailLabelCertifyRequest>
'''



print("\nResponse Content with formatted XML string number 2:")
rate_response1 = req.get(api_addr + test_xml)
print(rate_response1.content)

xml_dict = xml.fromstring(rate_response1.content)
print(xml_dict)

#print("\nResponse Content with formatted XML string number 2:")
#rate_response = req.post(api_addr, xml_formatted)
#print(rate_response.content)


