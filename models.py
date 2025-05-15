from sqlalchemy import Column, Integer, String, LargeBinary, Text
from database import Base

class food_images(Base):
    __tablename__ = 'food_images'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(100), unique=True)
    filemime = Column(String(25))
    filepath = Column(String, unique=True)
    filedata = Column(Text)
    prediction_label = Column(String(10))
