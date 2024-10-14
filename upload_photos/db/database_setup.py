from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from upload_photos import app


Base = declarative_base()

from upload_photos.db.models import uploadPhotos

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.create_all(engine)