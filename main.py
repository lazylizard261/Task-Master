

from datetime import datetime
from flask import request
from flask import Flask, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return '<Task %r>' % self.id


@app.route("/", methods=['GET','POST'])
def index():
    tasks = Todo.query.order_by(Todo.date_created).all()
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content!="":
            new_task = Todo(content=task_content)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return "Unable to update DB"
        else:
            return render_template('index.html',tasks=tasks, err = "Please Enter tasks")
    else:
       

        return render_template('index.html',tasks = tasks)



@app.route("/update/<int:id>", methods=['POST','GET'])
def edit(id):
    
     task_to_edit = Todo.query.get_or_404(id)

     if request.method == 'POST':
        task_to_edit.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Oops!. Unable to update the Task"
     else:
        return render_template('update.html',task=task_to_edit)




@app.route("/delete/<int:id>")
def delete(id):
    tast_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(tast_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "OOPS! There was a probleb deleting the task."


if __name__ == "__main__":
    app.run()
