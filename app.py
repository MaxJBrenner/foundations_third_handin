from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        tool_name = request.form['name']
        tool_description = request.form['description']
        tool_content = request.form["content"]
        tool_link = request.form["link"]
        new_tool = Tool(name=tool_name, description=tool_description, content=tool_content, link=tool_link)

        try:
            db.session.add(new_tool)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tools = Tool.query.order_by(Tool.date_created).all()
        return render_template('index.html', tools=tools)
 
    
@app.route('/add-tool', methods=['POST', 'GET'])
def addTool():
    return render_template('add-tool.html')


@app.route('/view-tool', methods=['POST', 'GET'])
def viewTool():
    tool = Tool.query.get(request.args)
    return render_template('view-tool.html', tool=tool)

    
def prepopulate():
    with app.app_context():
        db.create_all()
        
        # Create All Categories
        category1 = Category(name="Writing")
        db.session.add(category1)
        category2 = Category(name="Images")
        db.session.add(category2)
        category3 = Category(name="Coding")
        db.session.add(category3)
        
        
        # Create All Tools
        example_text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
        toolList = [{"name": "ChatGPT", "description": "AI ChatBot - conversational search engine", "link": "https://openai.com/blog/chatgpt/"},
                    {"name": "Github Copilot", "description": "Ai code creator - text to code - suggest code and entire functions in real-time", "link": "https://github.com/features/copilot/"},
                    {"name": "Dall E2", "description": "AI image creator - create realistic images and art from a description in natural language", "link": "https://openai.com/dall-e-2/"},
                    {"name": "Copy.ai", "description": "AI writing platform - Generate many types of content (e.g. Blogs)", "link": "https://www.copy.ai/"},
                    {"name": "Writer", "description": "PAI writing platform - unlock on-brand content at scale (+ AI Content Detector)", "link": "https://writer.com/"},
                    {"name": "Writesonic", "description": "AI writing platform - Generate many types of content (e.g Blog Post, Tweets, LinkedIn Posts)", "link": "https://writesonic.com/"}]
        
        for tool in toolList:
            new_tool = Tool(name=tool["name"], description=tool["description"], content=example_text, link=tool["link"])
            db.session.add(new_tool)
            
        db.session.commit()
        
if __name__ == "__main__":
    app.run(debug=True, port=5005)
    
