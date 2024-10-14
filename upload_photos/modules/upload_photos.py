from upload_photos import app

from upload_photos.controllers.uploadPhotos import uploadPhotos, indexRoute

# controller import
app.route('/', methods=['GET'])(indexRoute)
app.route('/upload_image', methods=['POST'])(uploadPhotos)