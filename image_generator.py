import imgkit
import os
import inspect
import tempfile

class ImageGenerator:
    def generate_image(self, string):
        options = {
            'format': 'png',
            'crop-w': '425',
            #  "xvfb": ""
        }

        imgkit.from_string(string, './pics/out.png', options=options)