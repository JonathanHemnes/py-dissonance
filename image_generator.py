import imgkit
import os

class ImageGenerator:
    def generate_image(self, string):
        options = {
            'format': 'png',
            'crop-w': '425',
            "xvfb": ""
        }
        dir = os.getcwd() + 'pics/out.png'
        imgkit.from_string(string, dir, options=options)