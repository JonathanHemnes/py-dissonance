from jinja2 import Template, Environment, PackageLoader, select_autoescape

class HtmlGenerator:
    
    def generate(self, author, date, text):
        env = Environment(
            loader=PackageLoader('newspaper', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('newspaper.html')
        return template.render(author=author, date=date, text=text)