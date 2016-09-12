import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):

    def get(self):
        main_html = jinja_env.get_template("templates/index.html")
        self.response.write(main_html.render())

    # Any chance I could do a translate function
    # def translate(self):

    def post(self):

        to_translate = {}
        translated_html = jinja_env.get_template("templates/translated.html")
        words_to_translate = self.request.get("to_translate")
        pig_latin_list = []
        # A for loop for sentences
        for word in words_to_translate.split():
            pig_latin = "{}-{}ay".format(word[1:], word[0])
            pig_latin_list.append(pig_latin)

        to_translate["translation"] =  " ".join(pig_latin_list).capitalize()
        self.response.write(translated_html.render(to_translate))

        # Have it translate to english. Two buttons.

app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
