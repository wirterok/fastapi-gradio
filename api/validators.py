import imghdr

class ValidateImageType:
    @classmethod
    def validate(cls, image_path):
        avaliable_formats = ['jpeg', 'png']
        file_format = imghdr.what(image_path)
        if file_format not in avaliable_formats:
            raise ValueError("Invalid format, only 'jpg' or 'png' can be accepted")