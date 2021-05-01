import os
from flask import Flask
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '74cfe9519ac69de16029f20e2786f1e5'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:ehr2password@aahn9mlfrrvcm5.cacrvcq7qcsm.us-east-2.rds.amazonaws.com:3306/ebdb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pvrsmkusylwhgk:bbd8018d93372752c8eb5397352e6b5997cf89f4fdcf876907df313b4bbfcb44@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d7tb0tb2cjde8h'

db = SQLAlchemy(app)


class Patient(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False) 
	address = db.Column(db.String(200), nullable=False)
	birth_date = db.Column(db.DateTime, nullable=False)
	sex = db.Column(db.String(10), nullable=False) 
	post = db.Column(db.String(100), nullable=False)
	unit = db.Column(db.String(100), nullable=False) 
	phone = db.Column(db.String(25), nullable=False)
	age = db.Column(db.Integer, nullable=False) 
	origin = db.Column(db.String(80), nullable=False)
	lg = db.Column(db.String(60), nullable=False) 
	marital_status = db.Column(db.String(20), nullable=False)
	picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	kin_name = db.Column(db.String(100), nullable=False) 
	kin_address = db.Column(db.String(200), nullable=False)
	kin_occupation = db.Column(db.String(50), nullable=False) 
	kin_phone = db.Column(db.String(50), nullable=False) 
	genotype = db.Column(db.String(10), nullable=False)
	height = db.Column(db.String(10), nullable=False)
	remark = db.Column(db.String(300), nullable=True)  
	status = db.Column(db.String(10), nullable=False)
	disability = db.Column(db.String(30), nullable=True)


class Admin(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)
	has_toured = db.Column(db.Boolean, nullable=False, default=False)

	def get_reset_token(self, expires_sec=1800):
		s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'admin_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			admin_id = s.loads(token)['admin_id']
		except:
			return None
		return User.query.get(admin_id)

	def __repr__(self):
		return f"User('{self.name}', '{self.password}')"


class Staff(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False) 
	address = db.Column(db.String(200), nullable=False)
	birth_date = db.Column(db.DateTime, nullable=False)
	sex = db.Column(db.String(10), nullable=False) 
	dept = db.Column(db.String(50), nullable=False)
	title = db.Column(db.String(20), nullable=False) 
	qualification = db.Column(db.String(50), nullable=False)
	phone = db.Column(db.String(25), nullable=False)
	age = db.Column(db.Integer, nullable=False) 
	state = db.Column(db.String(40), nullable=False)
	lg = db.Column(db.String(60), nullable=False) 
	marital_status = db.Column(db.String(20), nullable=False)
	picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	post = db.Column(db.String(30), nullable=False) 
	appointment = db.Column(db.String(50), nullable=False)


class DiagnoseTable(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	patient_number = db.Column(db.Integer, nullable=False)
	ailment = db.Column(db.String(200), nullable=False) 
	treatment = db.Column(db.String(350), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


db.create_all()
db.session.commit()
