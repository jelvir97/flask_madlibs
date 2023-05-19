from stories import Story, story
from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY']  = "dogs"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html',prompts=story.prompts)

@app.route('/story')
def created_story():
    story_text = story.generate(request.args)
    return render_template('story.html', story_text=story_text)