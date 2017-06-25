import imgkit

class ImageGenerator:
    def generate_image(self, string):
        options = {
            'format': 'png',
            'crop-w': '425',
            'quiet': '',
            "xvfb": ""
        }
        imgkit.from_string(string, './pics/out.png', options=options)