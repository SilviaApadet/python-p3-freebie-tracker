#!/usr/bin/env python3

# Script goes here!
from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create some Companies
apple = Company(name="Apple", founding_year=1976)
hp = Company(name="Hp", founding_year=1939)

# Create some Devs
silvia = Dev(name="Silvia")
eugene = Dev(name="Eugene")

# Create some Freebies
freebie1 = Freebie(item_name="Laptop", value=2000, company=hp, dev=silvia)
freebie2 = Freebie(item_name="Headphones", value=200, company=apple, dev=eugene)
freebie3 = Freebie(item_name="Smartwatch", value=300, company=apple, dev=silvia)

session.add_all([apple, hp, silvia, eugene, freebie1, freebie2, freebie3])
session.commit()