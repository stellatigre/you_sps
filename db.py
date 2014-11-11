from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configfile import db as conf

conn_string = "postgresql+psycopg2://{user}:{password}@{host}/{name}".format(**conf)
db = create_engine(conn_string)
Session = sessionmaker(bind=db)

Base = declarative_base()

class Rate(Base):
    __tablename__ = 'rates'

    id = Column(Integer, primary_key=True)
    container = Column(String)
    rate = Column(Float)
    class_id = Column(Integer)
    mail_service = Column(String)
    size = Column(String)
    pounds = Column(Integer)
    ounces = Column(Integer)
    zip_origin = Column(Integer)
    zip_destination = Column(Integer)
    zone = Column(Integer)

class Label(Base):
    __tablename__ = 'labels'

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
    'to_firm' : 'Omnicorp. LTD.',
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

    
def create_rates_table(db_engine):
    Rate.metadata.create_all(db_engine)

def rate_entry_from_response_dict(data):
    data = data['RateV4Response']['Package']
    session = Session()
    mapped = Rate(
        rate = data['Postage']['Rate'],
        class_id = data['Postage']['@CLASSID'],
        mail_service = data['Postage']['MailService'],
        pounds = data['Pounds'],
        ounces = data['Ounces'],
        size = data['Size'],
        zip_origin = data['ZipOrigination'],
        zip_destination = data['ZipDestination'],
        zone = data['Zone']
    )
    session.add(mapped)
    session.commit()
    session.flush()
    return mapped
        
    
#create_rates_table(db)

