from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


states = [
  "Abia",
  "Adamawa",
  "Akwa Ibom",
  "Anambra",
  "Bauchi",
  "Bayelsa",
  "Benue",
  "Borno",
  "Cross River",
  "Delta",
  "Ebonyi",
  "Edo",
  "Ekiti",
  "Enugu",
  "FCT - Abuja",
  "Gombe",
  "Imo",
  "Jigawa",
  "Kaduna",
  "Kano",
  "Katsina",
  "Kebbi",
  "Kogi",
  "Kwara",
  "Lagos",
  "Nasarawa",
  "Niger",
  "Ogun",
  "Ondo",
  "Osun",
  "Oyo",
  "Plateau",
  "Rivers",
  "Sokoto",
  "Taraba",
  "Yobe",
  "Zamfara"
]

state_choices = []

for state in states:
	state_choices.append((state, state))

lg_choices = [('Local Government A', 'Local Government A'), ('Local Government B', 'Local Government B')]
marital_status_choices = [('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated')]
genotype_choices = [('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS')]

class AddPatientForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "e.g John Doe"}) 
	address = StringField('Address', validators=[DataRequired()], 
		render_kw={"placeholder": "e.g. 123 Something Street, Town, City"}) 
	birth_date = DateField('Birth Date', validators=[DataRequired()], format='%Y-%m-%d') 
	sex = SelectField('Sex', validators=[DataRequired()], choices=[('Male', 'Male'), ('Female', 'female')])  
	post = StringField('Post', validators=[DataRequired()]) 
	unit = StringField('Unit', validators=[DataRequired()])  
	phone = StringField('Phone', validators=[DataRequired()], render_kw={"placeholder": "e.g 08012345678"}) 
	age = IntegerField('Age', validators=[DataRequired()]) 
	origin = SelectField('Origin', validators=[DataRequired()], choices=state_choices) 
	lg = SelectField('Local Government', validators=[DataRequired()], choices=lg_choices)  
	marital_status = SelectField('Marital Status', validators=[DataRequired()], choices=marital_status_choices)
	picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
	kin_name = StringField("Next of Kin's Name", validators=[DataRequired()]) 
	kin_address = StringField("Next of Kin's Address", validators=[DataRequired()])
	kin_occupation = StringField("Next of Kin's Occupation.", validators=[DataRequired()]) 
	kin_phone = StringField("Next of Kin's Phone No.", validators=[DataRequired()])
	genotype = SelectField('Genotype', validators=[DataRequired()], choices=genotype_choices)
	height = StringField('height', validators=[DataRequired()])
	remark = TextAreaField('Remark')   
	status = StringField('Status') 
	disability = StringField('Disability')
	submit = SubmitField('Add Record')


class AddStaffForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()]) 
	address = StringField('Address', validators=[DataRequired()]) 
	birth_date = DateField('birth_date', validators=[DataRequired()]) 
	sex = SelectField('Sex', validators=[DataRequired()], choices=[('Male', 'Male'), ('Female', 'female')])  
	dept = StringField('Department', validators=[DataRequired()]) 
	title = StringField('Title', validators=[DataRequired()])  
	qualification = StringField('Qualification', validators=[DataRequired()])
	phone = StringField('Phone', validators=[DataRequired()]) 
	age = IntegerField('Name', validators=[DataRequired()]) 
	state = SelectField('State', validators=[DataRequired()], choices=state_choices) 
	lg = SelectField('Local Government', validators=[DataRequired()], choices=lg_choices)  
	marital_status = SelectField('Marital Status', validators=[DataRequired()], choices=marital_status_choices)
	picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
	post = StringField('Post', validators=[DataRequired()])
	appointment = StringField('Appointment', validators=[DataRequired()],)
	submit = SubmitField('Add Staff')


class AddDiagnosisForm(FlaskForm):
	patient_number = IntegerField('Patient Number', validators=[DataRequired()]) 
	ailment = TextAreaField('Ailment', validators=[DataRequired()])
	treatment = TextAreaField('Ailment', validators=[DataRequired()])
	submit = SubmitField('Add Diagnosis')
