from upload_photos import app

from upload_photos.controllers.uploadPhotos import uploadPhotos, indexRoute, getPhotosData

# controller import
app.route('/', methods=['GET'])(indexRoute)
app.route('/api/upload_image', methods=['POST'])(uploadPhotos)
app.route('/api/get_photos_data', methods=['GET'])(getPhotosData)