from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import login_user, current_user, logout_user, login_required 
from ehr import db, bcrypt 
from ehr.models import Admin, Patient, Staff, Patient, Staff, DiagnoseTable
from ehr.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from ehr.records.forms import AddPatientForm, AddStaffForm, AddDiagnosisForm

from ehr.utils import save_picture, send_reset_email

from ehr import create_app


app = create_app()

@app.route('/', methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('record'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Admin.query.filter_by(name=form.name.data).first()

		if user:
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			flash(f'You have successfully logged in.', 'success')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check name and password', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('record'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Admin(name=form.name.data, password=hashed_pw)
		db.session.add(user)
		db.session.commit()

		flash(f'Your account has been created! You are now able to log in.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file

		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route('/home', methods=['GET', 'POST'])
def home():
	count_patient = len(Patient.query.all())
	count_staff = len(Staff.query.all())
	count_diagnosis = len(DiagnoseTable.query.all())

	return render_template('home.html', title='Home', 
							count_patient=count_patient, 
							count_staff=count_staff, 
							count_diagnosis=count_diagnosis)


@app.route('/record', methods=['GET', 'POST'])
def record():
	page = request.args.get('page', 1, type=int)
	patients = Patient.query.paginate(page=page, per_page=5)
	form = AddPatientForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)

		image_file = url_for('static', filename='profile_pics/' + picture_file)

		patient = Patient(name=form.name.data, address=form.address.data, 
						birth_date=form.birth_date.data, sex=form.sex.data, 
						post=form.post.data, unit=form.post.data, 
						phone=form.phone.data, age=form.age.data, origin=form.origin.data,
						lg=form.lg.data, marital_status=form.marital_status.data, 
						picture=picture_file, kin_name=form.kin_name.data, 
						kin_address=form.kin_address.data, kin_occupation=form.kin_occupation.data, 
						kin_phone=form.kin_phone.data, genotype=form.genotype.data, 
						height=form.height.data, remark=form.remark.data, 
						status=form.status.data, disability=form.disability.data)
		db.session.add(patient)
		db.session.commit()
		flash('Your record has been created!', 'success')
		return redirect(url_for('record'))
	return render_template('record.html', title='Patients', patients=patients, form=form)


# @app.route("/single_patient/<int:patient_id>")
# def single_patient(patient_id):
# 	form = AddPatientForm()
# 	patient = Patient.query.get_or_404(patient_id)
# 	return render_template('single_patient.html', title='Patient', patient=patient, form=form)


@app.route('/staff', methods=['GET', 'POST'])
def staff():
	page = request.args.get('page', 1, type=int)
	staffs = Staff.query.paginate(page=page, per_page=5)
	form = AddStaffForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)

		image_file = url_for('static', filename='profile_pics/' + picture_file)

		staff = Staff(name=form.name.data, address=form.address.data, 
						birth_date=form.birth_date.data, sex=form.sex.data, 
						dept=form.dept.data, title=form.title.data, 
						qualification=form.qualification.data,
						phone=form.phone.data, age=form.age.data, state=form.state.data,
						lg=form.lg.data, marital_status=form.marital_status.data, 
						picture=picture_file, post=form.post.data, appointment=form.appointment.data)
		db.session.add(staff)
		db.session.commit()
		flash('Your record has been created!', 'success')
		return redirect(url_for('staff'))
	return render_template('staff.html', title='Staff', staffs=staffs, form=form)


@app.route("/single_staff/<int:staff_id>")
def single_staff(staff_id):
	staff = Staff.query.get_or_404(staff_id)
	return render_template('single_staff.html', title='Staff', staff=staff)


@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
	page = request.args.get('page', 1, type=int)
	diagnoses = DiagnoseTable.query.paginate(page=page, per_page=5)
	form = AddDiagnosisForm()
	if form.validate_on_submit():

		diagnosis = DiagnoseTable(patient_number=form.patient_number.data, 
								  ailment=form.ailment.data, treatment=form.treatment.data)
		db.session.add(diagnosis)
		db.session.commit()
		flash('Your record has been created!', 'success')
		return redirect(url_for('diagnosis'))
	return render_template('diagnosis.html', title='Diagnosis', diagnoses=diagnoses, form=form)


@app.route("/single_patient/<int:patient_id>", methods=['GET', 'POST'])
def single_patient(patient_id): 
	patient = Patient.query.get_or_404(patient_id)

	image_file = url_for('static', filename='profile_pics/' + patient.picture)
	
	form = AddPatientForm()

	if form.validate_on_submit():
		patient.name = form.name.data
		patient.address = form.address.data
		patient.birth_date = form.birth_date.data
		patient.sex = form.sex.data
		patient.post = form.post.data
		patient.unit = form.unit.data
		patient.phone = form.phone.data
		patient.age = form.age.data
		patient.origin = form.origin.data
		patient.lg = form.lg.data
		patient.marital_status = form.marital_status.data
		patient.picture = form.picture.data
		patient.kin_name = form.kin_name.data
		patient.kin_address = form.kin_address.data
		patient.kin_occupation = form.kin_occupation.data
		patient.kin_phone = form.kin_phone.data
		patient.kin_address = form.kin_address.data
		patient.genotype = form.genotype.data
		patient.height = form.height.data
		patient.remark = form.remark.data
		patient.status = form.status.data
		patient.disability = form.disability.data

		db.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('single_patient', patient_id=patient_id, patient=patient, form=form, title="Patient", image_file=image_file))
	elif request.method == 'GET':
		form.name.data = patient.name
		form.address.data = patient.address
		form.birth_date.data = patient.birth_date 
		form.sex.data = patient.sex
		form.post.data = patient.post 
		form.unit.data = patient.unit 
		form.phone.data = patient.phone
		form.age.data = patient.age 
		form.origin.data = patient.origin
		form.lg.data = patient.lg 
		form.marital_status.data = patient.marital_status 
		form.picture.data = patient.picture 
		form.kin_name.data = patient.kin_name
		form.kin_address.data = patient.kin_address
		form.kin_occupation.data = patient.kin_occupation
		form.kin_phone.data = patient.kin_phone 
		form.genotype.data = patient.genotype
		form.height.data = patient.height 
		form.remark.data = patient.remark 
		form.status.data = patient.status 
		form.disability.data = patient.disability
	return render_template('single_patient.html', patient_id=patient_id, patient=patient, form=form, title="Patient", image_file=image_file)


@app.route("/single_patient/<int:patient_id>/delete", methods=['POST'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    flash('The patient record has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/staff/<int:staff_id>/delete", methods=['POST'])
def delete_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    db.session.delete(staff)
    db.session.commit()
    flash('The staff record has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/diagnosis/<int:diagnosis_id>/delete", methods=['POST'])
def delete_diagnosis(diagnosis_id):
    diagnosis = DiagnoseTable.query.get_or_404(diagnosis_id)
    db.session.delete(diagnosis)
    db.session.commit()
    flash('The diagnosis has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/single_diagnosis/<int:diagnosis_id>")
def single_diagnosis(diagnosis_id):
	diagnosis = DiagnoseTable.query.get_or_404(diagnosis_id)
	return render_template('single_diagnosis.html', title='Diagnosis', diagnosis=diagnosis)


if __name__ == '__main__':
	app.run(debug=True)
	# app.run(host='0.0.0.0')