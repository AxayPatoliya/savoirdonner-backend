from upload_photos import app
import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime

#Model Imports
from upload_photos.db.database_setup import (Base as Base)
from upload_photos.db.models.uploadPhotos import (PhotoEntry as PhotoEntry)
from sqlalchemy import create_engine, func, desc, or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def indexRoute():
    return jsonify({"status": "success", "message": "Server is up and running"}), 200

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploadPhotos():
    if request.method == 'POST':
        try:
            # Get data from the request
            location = request.form.get('location')
            comment = request.form.get('comment')
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            file = request.files.get('photo')

            if not file or not allowed_file(file.filename):
                return jsonify({"status": "error", "message": "Invalid file type"}), 400

            # Save the photo file
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Store the image name and other data in the database
            photo_entry = PhotoEntry(
                Location=location,
                Photo=filename,  # Store the name of the file
                Comment=comment,
                Latitude=latitude,
                Longitude=longitude,
            )

            session = DBSession()
            session.add(photo_entry)
            session.commit()
            session.close()

            return jsonify({"status": "success", "message": "Photo uploaded successfully"}), 201

        except Exception as e:
            # session.rollback()
            return jsonify({"status": "error", "message": str(e)}), 500
