# This file just contains predefined templates
# for XML requests to the USPS API, for rates and lables
import configfile as config

rate_test_xml = '''
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
rate_xml_base = '''
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

label_xml_base = '''
<?xml version="1.0" encoding="UTF-8" ?>
<SigConfirmCertifyV4.0Request USERID="{api_user}" PASSWORD="XXXXXX">
  <Revision>2</Revision>
  <ImageParameters />
  <FromName>{from_name}</FromName>
  <FromFirm>{from_firm}</FromFirm>
  <FromAddress1>{from_address1}</FromAddress1>
  <FromAddress2>{from_address2}</FromAddress2>
  <FromCity>{from_city}</FromCity>
  <FromState>{from_state}</FromState>
  <FromZip5>{from_zip5}</FromZip5>
  <FromZip4/>
  <ToName>{to_name}</ToName>
  <ToFirm>{to_firm}</ToFirm>
  <ToAddress1>{to_address1}</ToAddress1>
  <ToAddress2>{to_address2}</ToAddress2>
  <ToCity>{to_city}</ToCity>
  <ToState>{to_state}</ToState>
  <ToZip5>{to_zip5}</ToZip5>
  <ToZip4 />
  <ToPOBoxFlag></ToPOBoxFlag>
  <WeightInOunces>{weight_ounces}</WeightInOunces>
  <ServiceType>{service_type}</ServiceType>
  <SeparateReceiptPage>{seperate_receipt_page}</SeparateReceiptPage>
  <POZipCode>{po_zipcode}</POZipCode>
  <ImageType>{image_type}</ImageType>
  <AddressServiceRequested>{address_service_requested}</AddressServiceRequested>
  <HoldForManifest>{hold_for_manifest}</HoldForManifest>
  <Container>{container}</Container>
  <Size>{size}</Size>
  <Width>{width}</Width>
  <Length>{length}</Length>
  <Height>{height}</Height>
  <Girth>{girth}</Girth>
  <ReturnCommitments>{return_commitments}</ReturnCommitments>
 </SigConfirmCertifyV4.0Request>
'''

test_rate_opts = {
    #'api_user' : config.api_user,
    'package_id' : '1',
    'service' : 'PRIORITY',
    'zip_origin' : 78702,
    'zip_dest' : 20772,
    'pounds' : 1,
    'ounces' : 8,
    'container' : 'NONRECTANGULAR',
    'size' : 'Large',
    'width' : 15,
    'length' : 10,
    'height' : 35,
    'girth' : 65
}

test_label_opts = {
    'api_user' : config.api_user,
    'from_name' : 'Lean Doer',
    'from_firm' : 'USPS',
    'from_address1' : 'RM 2100',
    'from_address2' : '475 Enfant Plaza SW',
    'from_city' : 'Washington',
    'from_state' : 'DC',
    'from_zip5' : 20260,
    'to_name' : 'Spooky Skellingtons',
    'to_firm' : 'OMnicorp. LTD.',
    'to_address1' : 'Ste 240',
    'to_address2' : '2 Massachusetts Ave NE',
    'to_city' : 'Washington',
    'to_state' : 'DC',
    'to_zip5' : 20212,
    'weight_ounces' : '2',
    'service_type' : 'Priority',
    'seperate_receipt_page' : 'False',
    'po_zipcode' : '20770', 
    'image_type' : config.image_type,
    'address_service_requested' : "False",
    'hold_for_manifest' : 'N',
    'container' : 'NONRECTANGULAR',
    'size' : 'LARGE',
    'width' : 7,
    'length' : 15,
    'height' : 10,
    'girth' : 40,
    'return_commitments' : 'true'
}

test_label = '''
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
  <ImageType>PDF</ImageType>
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
