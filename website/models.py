from sqlalchemy import func
from . import db
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from flask_security import RoleMixin, SQLAlchemyUserDatastore
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, request, url_for, flash
from datetime import datetime, timedelta
from wtforms import ValidationError

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    __tablename__ = 'user' 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    ic = db.Column(db.String(12), db.ForeignKey('registered_unit.ic'))
    phone_num = db.Column(db.String(20))
    password = db.Column(db.String(80))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    tenant_unit = db.Column(db.String(5), db.ForeignKey('registered_unit.unit'), nullable=True)
    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)

class Role(db.Model, RoleMixin):
    __tablename__ = 'role' 
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    
class UserModelView(ModelView):
    column_list = ['username', 'email', 'ic', 'phone_num', 'roles']
    form_columns = ['username', 'email', 'ic', 'phone_num', 'password', 'roles']
    form_overrides = {'roles': QuerySelectMultipleField}
    form_args = {'roles': {
            'query_factory': lambda: db.session.query(Role).all(),
            'get_label': 'name',
            'allow_blank': False,
            'validators': [],}}
    
    def on_model_change(self, form, model, is_created):
        # This method is called before a model is created or updated
        if is_created and form.password.data:
            # Hash the password using scrypt
            hashed_password = generate_password_hash(form.password.data, method='scrypt')
            # Update the model's password field with the hashed password
            model.password = hashed_password
        elif not is_created and form.password.data:
            # Check if the password has been changed. If so, hash the new password.
            original_password = User.query.get(model.id).password
            if form.password.data != original_password:
                hashed_password = generate_password_hash(form.password.data, method='scrypt')
                model.password = hashed_password
        super(UserModelView, self).on_model_change(form, model, is_created)

    def is_accessible(self):
        # Check if current user is authenticated and has the 'admin' role
        return current_user.is_authenticated and current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # Redirect unauthorized users
        if not current_user.is_authenticated:
            # Redirect to login page if the user is not logged in
            return redirect(url_for('auth.admin_login', next=request.url))
        else:
            # Display an error message and redirect to the home page
            # if the user is logged in but does not have admin rights
            flash('You do not have access to this page.', 'error')
            return redirect(url_for('/home')) 

class Registered_Unit(db.Model):
    __tablename__ = 'registered_unit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ic = db.Column(db.String(12)) 
    unit = db.Column(db.String(5))
    available = db.Column(db.Boolean, default=True)
    
class RegisteredUnitModelView(ModelView):
    column_list = ['ic', 'unit', 'available']

        
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        if not current_user.is_authenticated:
            # Redirect to login page if the user is not logged in
            return redirect(url_for('auth.admin_login', next=request.url))
        else:
            # Display an error message and redirect to the home page
            # if the user is logged in but does not have admin rights
            flash('You do not have access to this page.', 'error')
            return redirect(url_for('/'))
    
def initialize_admin_data():
    # Create roles if they don't exist
    for role_name in ['user', 'admin', 'security', 'tenant']:  # Added 'tenant' to the list
        if not Role.query.filter_by(name=role_name).first():
            role = Role(name=role_name)
            db.session.add(role)
    
    db.session.commit()

    # Check if the admin user exists
    admin_user = User.query.filter_by(email="admin123@gmail.com").first()
    if not admin_user:
        # Insert default admin data
        admin = User(id = 10000,
            username="admin123",
            email="admin123@gmail.com",
            password=generate_password_hash("admin123", method="scrypt"),
            roles=[Role.query.filter_by(name='admin').first()]
        )
        db.session.add(admin)
        db.session.commit()
        
        security = User(
            username="security",
            email="security@gmail.com",
            password=generate_password_hash("1234567", method="scrypt"),
            roles=[Role.query.filter_by(name='security').first()]
        )
        db.session.add(security)
        db.session.commit()
        
    new_unit = Registered_Unit.query.filter_by(unit="A0101").first()
    if not new_unit:
        
        new_unit = Registered_Unit(id = 5000, ic = "030226040249", unit = "A0101")
        db.session.add(new_unit)
        db.session.commit()
    
class IncidentReport(db.Model):
    __tablename__ = 'incident_report'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reportDate = db.Column(db.DateTime)
    incidentType = db.Column(db.String(100))
    reportedBy = db.Column(db.String(50))
    contactNumber = db.Column(db.String(15))
    description = db.Column(db.String(2000))
    checked = db.Column(db.Boolean, default=False)
    unitId = db.Column(db.String(4), db.ForeignKey('registered_unit.unit'), nullable=True)
    
class VisitorRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ic_number = db.Column(db.String(12))
    phone_number = db.Column(db.String(22))
    duration_of_stay = db.Column(db.DateTime)
    unit = db.Column(db.String(5), db.ForeignKey('registered_unit.unit'))
    registration_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    owner_approved = db.Column(db.Boolean, default=False)
    
class VehicleRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone_number = db.Column(db.String(22))
    car_number = db.Column(db.String(20))
    duration_of_park = db.Column(db.DateTime)
    unit = db.Column(db.String(5), db.ForeignKey('registered_unit.unit'))
    registration_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    
class OTP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    otp = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    used = db.Column(db.Boolean, default=False)

    def is_valid(self):
        # Check if OTP is still valid (not used and within 10 minutes)
        return not self.used and (datetime.utcnow() - self.created_at) < timedelta(minutes=10)
    
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(100))
    visitor_ic = db.Column(db.String(12))
    unit = db.Column(db.String(5), db.ForeignKey('registered_unit.unit'))
    message = db.Column(db.String(255))
    duration_of_stay = db.Column(db.DateTime)
    checked = db.Column(db.Boolean, default=False)
    
class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ic = db.Column(db.String(12))
    gender = db.Column(db.String(10))
    reason = db.Column(db.String(255))
    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

