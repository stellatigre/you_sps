from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configfile import db as conf

conn_string = "postgresql+psycopg2://{user}:{password}@{host}/{name}".format(**conf)
db = create_engine(conn_string)
Session = sessionmaker(bind=db)
session = Session()

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
    
def create_rates_table(db_engine):
    Rate.metadata.create_all(db_engine)

def rate_entry_from_response_dict(data):
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
    session.add(mapped)
    session.commit()
    session.flush()
    return mapped
        
    
#create_rates_table(db)

