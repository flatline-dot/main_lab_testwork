from sqlalchemy import Column, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Bill(Base):
    __tablename__ = 'bill'
    __table_args__ = (UniqueConstraint('client_name', 'client_org', 'num'),)

    id = Column(Integer, primary_key=True)
    client_name = Column(String(30))
    client_org = Column(ForeignKey('org.id', ondelete='CASCADE'))
    num = Column(Integer)
    sum = Column(Integer)
    date = Column(Date)
    service = Column(ForeignKey('service.id', ondelete='CASCADE'))
    orgs = relationship('Org')
    services = relationship('Service')


class Org(Base):
    __tablename__ = 'org'

    id = Column(Integer, primary_key=True)
    org_name = Column(String(30), unique=True)


class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    service_title = Column(String(50))
