from jinja2 import Template, Environment, PackageLoader

class HtmlGenerator:
    
    def generate(self, author, date, text):
        env = Environment(
            loader=PackageLoader('newspaper', 'templates')
        )
        template = env.get_template('newspaper.html')
        return template.render(author=author, date=date, text=text)