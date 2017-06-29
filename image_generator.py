import imgkit
import os
import inspect
import tempfile

class ImageGenerator:
    def generate_image(self, string):
        options = {
            'format': 'png',
            'crop-w': '425',
             "xvfb": ""
        }

        file = tempfile.NamedTemporaryFile(suffix='.png')
        print(file.name)
        imgkit.from_string(string, file.name, options=options)