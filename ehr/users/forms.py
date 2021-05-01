from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from ehr.models import Admin


class RegistrationForm(FlaskForm):
	name = StringField('Name', 
							validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
							validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


	def validate_name(self, name):
		user = Admin.query.filter_by(name=name.data).first()
		if user:
			raise ValidationError('That name is taken. Please choose a new one.')


class LoginForm(FlaskForm):
	name = StringField('Name', 
							validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username', 
							validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', 
							validators=[DataRequired(), Email()])
	submit = SubmitField('Update')


	def validate_username(self, username):
		if username.data != current_user.username:
			user = Admin.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a new one.')


	def validate_email(self, email):
		if email.data != current_user.email:
			user = Admin.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a new one.')


class RequestResetForm(FlaskForm):
	email = StringField('Email', 
						validators=[DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')


	def validate_username(self, email):
		user = Admin.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is not account with that email. You must register first.')
 

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
							validators=[DataRequired(), 
							EqualTo('password')])
	submit = SubmitField('Reset Password')
