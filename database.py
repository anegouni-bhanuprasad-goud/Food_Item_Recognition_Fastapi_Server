from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "" # Local_Database_URL
aws_database_url = "" # AWS_Database_URL
engine =create_engine(url=database_url, echo=True)
aws_engine = create_engine(url=aws_database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)
awsSessionLocal = sessionmaker(bind=aws_engine, autoflush=False)

Base = declarative_base()