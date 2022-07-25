from sqlalchemy import create_engine, MetaData

engine = create_engine(url="mysql+pymysql://ufood:ufood2022@ufoodb.c2ppwslmpouq.us-east-1.rds.amazonaws.com:3306/ufood", echo=True)
meta = MetaData()
conn = engine.connect()
