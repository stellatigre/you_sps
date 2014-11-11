from sqlalchemy import create_engine, Column, Integer, String, Float, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configfile import db as conf
from pprint import pprint

conn_string = "postgresql+psycopg2://{user}:{password}@{host}/{name}".format(**conf)
db = create_engine(conn_string)
Session = sessionmaker(bind=db)
Base = declarative_base()

class Rate(Base):
    __tablename__ = 'rates'

    id = Column(Integer, primary_key=True)
    container = Column(String)
    rate = Column(Numeric)
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

    id = Column(Integer, primary_key=True)
    confirmation_number = Column(Integer)
    to_name = Column(String)
    to_firm = Column(String)
    to_address1 = Column(String)
    to_address2 = Column(String)
    to_city = Column(String)
    to_state = Column(String)
    to_zip5 = Column(Integer)
    to_zip4 = Column(Integer)
    postnet = Column(String)
    rdc = Column(Integer)
    postage= Column(Numeric)
    zone = Column(Integer)
    insurance_fee = Column(Numeric)
    carrier_route= Column(String)
    return_commitments = Column(String)             # true or false
    commitment_name = Column(String)
    scheduled_delivery = Column(String)
    
    
def create_rates_table(db_engine):                  # honestly these are mostly for
    Rate.metadata.create_all(db_engine)             # remembering how to create the tables easily

def create_label_table(db_engine):
    Label.metadata.create_all(db_engine)

def label_entry_from_response_dict(data):
    data = data['SigConfirmCertifyV4.0Response']
    
    mapped = Label(
        to_name = data['ToName'],
        to_firm = data['ToFirm'],
        to_address1 = data['ToAddress1'],
        to_address2 = data['ToAddress2'],
        to_city = data['ToCity'],
        to_state = data['ToState'],
        postnet = data['Postnet'],
        rdc = data['RDC'],
        rate = data['Postage'],
        insurance_fee = data['InsuranceFee'],
        carrier_route = data['CarrierRoute'],
        scheduled_delivery = data['Commitment']['ScheduledDeliveryDate'],
        commitment_name = data['Commitment']['CommitmentName'],
        to_zip5 = data['ToZip5'],
        to_zip4 = data['ToZip4'],
        zone = data['Zone']
    )
    naive_commit(mapped)
    return mapped

def rate_entry_from_response_dict(data):
    pprint(data)
    data = data['RateV4Response']['Package']
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
    naive_commit(mapped)
    return mapped
        
def naive_commit(mapped_Object):                    # this is naive, so
    session = Session()                             # TODO: consider questions of session scope  
    session.add(mapped_Object)                      # perhaps leave off manual flushing ?
    session.commit()
    session.flush()
    

