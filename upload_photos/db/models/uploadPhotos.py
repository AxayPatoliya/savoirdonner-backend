from upload_photos.db.database_setup import Base

import datetime
import os
import sys
from sqlalchemy import Column, Index, ForeignKey, Integer, String, Interval, Date, DateTime, Float, JSON, Boolean, Sequence, Numeric, case, LargeBinary, func, Enum, desc, DECIMAL, asc
from datetime import datetime
import base64

class PhotoEntry(Base):
    __tablename__ = 'photo_entry'

    ID = Column(Integer, primary_key=True)
    Location = Column(String(), nullable=False)
    Comment = Column(String(), nullable=False)
    Photo = Column(String(), nullable=False)
    Latitude = Column(Float, nullable=False)
    Longitude = Column(Float, nullable=False)
    CrDtTm = Column(DateTime, default=datetime.now, nullable=False)

    def to_dict(self):
        return {
            'ID': self.ID,
            'Location': self.Location,
            'Comment': self.Comment,
            'Photo': self.Photo,
            'Latitude': self.Latitude,
            'Longitude': self.Longitude,
            'CrDtTm': self.CrDtTm
        }