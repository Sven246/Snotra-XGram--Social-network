import os
from werkzeug.utils import secure_filename
from flask import current_app

class FileService:

    @staticmethod
    def save_file(file):
        filename = secure_filename(file.filename)
        path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)

        file.save(path)
        return f"/uploads/{filename}"
