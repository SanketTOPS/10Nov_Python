from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#DB Config.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app) #DB Init.

#DB Model Config
class Studinfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    city=db.Column(db.String(100))
    

with app.app_context():
    db.create_all()

@app.route('/',methods=['GET'])
def index():
    stdata=Studinfo.query.all()
    return render_template('index.html',stdata=stdata)


@app.route('/insertdata',methods=['GET','POST'])
def insertdata():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        city=request.form["city"]
        
        stdata=Studinfo(name=name,email=email,city=city)
        db.session.add(stdata)
        db.session.commit()
        print("Record Inserted!")
    return render_template('insertdata.html')

app.run(debug=True)