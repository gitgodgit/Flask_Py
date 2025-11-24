from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  

    def __repr__(self):
        return '<Task %r>' % self.id
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# app.py (Add this section at the bottom, before if __name__ == "__main__")

@app.shell_context_processor
def make_shell_context():
    # This dictionary tells flask shell to load 'db', 'app', and your model 'Todo'
    return {'db': db, 'app': app, 'Todo': Todo}