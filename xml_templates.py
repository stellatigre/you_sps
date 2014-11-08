# This file just contains predefined templates
# for XML requests to the USPS API, for rates and lables
import configfile as config

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

test_label_opts = {
    'api_user' : config.api_user,
    'from_name' : 'Bella Nomar',
    'from_firm' : 'USPS',
    'from_address1' : 'Office 419',
    'from_address2' : '475 Enfant Plaza SW',
    'from_city' : 'Washington',
    'from_state' : 'DC',
    'from_zip5' : 20260,
    'to_name' : 'Jake The Magic Dog',
    'to_firm' : 'Abstractron',
    'to_address1' : 'Apt. #1B9',
    'to_address2' : '2 Massachusetts Ave NE',
    'to_city' : 'Washington',
    'to_state' : 'DC',
    'to_zip5' : 20212,
    'weight_ounces' : '10',
    'service_type' : 'Priority',
    'seperate_receipt_page' : 'False',
    'po_zipcode' : '20770', 
    'image_type' : config.image_type,
    'address_service_requested' : "False",
    'hold_for_manifest' : 'N',
    'container' : 'NONRECTANGULAR',
    'size' : 'LARGE',
    'width' : 7,
    'length' : 20.5,
    'height' : 15,
    'girth' : 60,
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
