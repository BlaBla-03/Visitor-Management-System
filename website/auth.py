from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Registered_Unit, Role
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import auth 
from flask_login import login_user, login_required, logout_user, current_user
from . decorators import role_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Logged in successfully!', category='success')
            
            # Redirect user based on role
            if any(role.name == 'admin' for role in user.roles):
                return redirect(url_for('views.admin.index'))
            elif any(role.name == 'security' for role in user.roles):
                return redirect(url_for('views.security_page'))
            elif any(role.name == 'tenant' for role in user.roles):
                return redirect(url_for('views.tenantpage'))
            else:
                return redirect(url_for('views.userpage'))
        else:
            flash('Invalid email or password', category='error')
            
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if not session.get('validated'):
        # Redirect to the validation page if the check fails
        return redirect(url_for('auth.validate_ic_unit'))
    
    if request.method == 'POST':
        # Get the data from the form
        email = request.form.get('email')
        username = request.form.get('username')
        phone_num = request.form.get('phone_num')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        ic = session.get('ic')  # Get the IC from the session
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(phone_num) < 10:
            flash('Phone number must be greater than 10 characters. Example "01131366628', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Fetch the user role
            user_role = Role.query.filter_by(name='user').first()

            # Create a new user and assign the user role
            new_user = User(email=email, username=username, phone_num=phone_num, 
                            password=generate_password_hash(password1, method='scrypt'), 
                            ic=ic, roles=[user_role])
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            session.pop('validated', None)
            session.pop('ic', None)
            return redirect(url_for('views.userpage'))
            
    return render_template("sign_up.html", user=current_user)

@auth.route('/validate-ic-unit', methods=['GET', 'POST'])
def validate_ic_unit():
    if request.method == 'POST':
        ic = request.form.get('ic')
        unit = request.form.get('unit')
        
        # Query the database for a record matching the provided IC and unit
        registered_unit = Registered_Unit.query.filter_by(ic=ic, unit=unit).first()
        
        # If a matching record is found, proceed with the validation
        if registered_unit:
            session['validated'] = True
            session['ic'] = ic  # Optionally store the IC in the session if needed later
            return redirect(url_for('auth.sign_up'))
        else:
            # Check which part of the validation failed
            if Registered_Unit.query.filter_by(ic=ic).first():
                flash('Unit Number doesn\'t match.', category='error')
            else:
                flash('Invalid IC Number', category='error')
    
    return render_template('validate_ic_unit.html', user=current_user)

@auth.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = User.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            # Check if user has the 'admin' role
            if any(role.name == 'admin' for role in admin.roles):
                flash('Logged in successfully!', category='success')
                login_user(admin)  # Use login_user for admins too
                return redirect(url_for('admin.index'))
            else:
                flash('Access denied: You must be an admin to log in here.', category='error')
        else:
            flash('Incorrect credentials, try again.', category='error')
            
    return render_template("admin_login.html", user=current_user)


@auth.route('/security', methods=['GET', 'POST'])
def security():
    if request.method == 'POST':
        # Get the data from the form
        username = request.form.get('username')
        password = request.form.get('password')
        
        security = User.query.filter_by(username=username).first()
        if security and check_password_hash(security.password, password):  # Assuming the hashed password is stored in admin.password
            flash('Logged in successfully!', category='success')
            login_user(security)  # Use login_user for admins too
            return redirect(url_for('views.security_page'))
        else:
            flash('Incorrect credentials, try again.', category='error')
            
    return render_template("security.html", user=current_user)

@auth.route('/tenant_signup', methods=['GET', 'POST'])
@role_required('user')
def tenant_signup():
    if request.method == 'POST':
        # Get the data from the form
        email = request.form.get('email')
        username = request.form.get('username')
        phone_num = request.form.get('phone_num')
        ic = request.form.get('ic_num')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        tenant_unit = request.form.get('tenant_unit')  # Get the tenant unit from the form
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(phone_num) < 10:
            flash('Phone number must be greater than 10 characters. Example "01131366628', category='error')
        elif len(ic) != 12:
            flash('IC number must be 12 digits no \'-\' in between.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Fetch the user role
            user_role = Role.query.filter_by(name='tenant').first()

            # Create a new user and assign the user role and tenant unit
            new_user = User(email=email, username=username, phone_num=phone_num,
                            password=generate_password_hash(password1, method='scrypt'),
                            ic=ic, roles=[user_role], tenant_unit=tenant_unit)  # Add tenant_unit here
            db.session.add(new_user)
            db.session.commit()
            flash('Tenant\'s account created!', category='success')
            return redirect(url_for('views.manage_tenant'))

    return render_template("tenant_signup.html", user=current_user)

@auth.route('/security_signup', methods=['GET', 'POST'])
@role_required('admin')
def security_signup():
    if request.method == 'POST':
        # Get the data from the form
        email = request.form.get('email')
        username = request.form.get('username')
        phone_num = request.form.get('phone_num')
        ic = request.form.get('ic_num')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(phone_num) < 10:
            flash('Phone number must be greater than 10 characters. Example "01131366628', category='error')
        elif len(ic) != 12:
            flash('IC number must be 12 digits no \'-\' in between.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Fetch the user role
            user_role = Role.query.filter_by(name='security').first()

            new_user = User(email=email, username=username, phone_num=phone_num,
                            password=generate_password_hash(password1, method='scrypt'),
                            ic=ic, roles=[user_role]) 
            db.session.add(new_user)
            db.session.commit()
            flash('Security\'s account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("security_signup.html", user=current_user)

            