from stories import Story, story_list
from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY']  = "dogs"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """opens home page to dropdown menu of stories
        user can choose story
    """
    return render_template('home.html',keys=story_list.keys())

@app.route('/story_form')
def story_form():
    """Creates form for selected story
        User inputs answers to prompts
    """
    title = request.args['title']
    story = story_list[title]
    return render_template('story_form.html',prompts=story.prompts,title = title)

@app.route('/story/<title>')
def created_story(title):
    """Renders completed story with answers"""
    story = story_list[title]
    story_text = story.generate(request.args)
    return render_template('story.html', story_text=story_text)