from datetime import datetime, timedelta
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, jsonify, redirect
from flask_login import login_required, current_user
from . import db
from sqlalchemy import func
from .models import IncidentReport, VisitorRegistration, Registered_Unit, VehicleRegistration, OTP, Notification, User, Blacklist
from flask_admin import AdminIndexView
from .decorators import role_required
import random
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/userpage')
@role_required('user')
@login_required
def userpage():
    return render_template("userpage.html", user=current_user)

@views.route('/tenantpage')
@role_required('tenant')
@login_required
def tenantpage():
    return render_template("tenantpage.html", user=current_user)

@views.route('/security_page')
@role_required('security')
@login_required
def security_page():
    return render_template("security_page.html")

@views.route('/incident_report', methods=['GET', 'POST'])
def incident_report():
    if request.method == 'POST':
        report_date = request.form.get('reportDate')
        incident_type = request.form.get('incidentType')
        description = request.form.get('description')
        first_report = IncidentReport.query.filter_by(id=40000).first()

        # Check if anonymous checkbox is checked
        anonymous = 'anonymousCheck' in request.form
        reported_by = None if anonymous else request.form.get('reportedBy')
        unit_id = None if anonymous else request.form.get('unitId')
        contact_number = None if anonymous else request.form.get('contactNumber')

        # Validation for required fields
        if not report_date or not incident_type or not description:
            flash('Please fill out all required fields.', 'danger')
            return render_template("incident_report.html", user=current_user)

        try:
            report_date = datetime.strptime(report_date, '%Y-%m-%dT%H:%M')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DDTHH:MM format.', 'danger')
            return render_template("incident_report.html", user=current_user)
        
        if first_report is None:
            new_report = IncidentReport(
                id = 40000,
                reportDate=report_date,
                incidentType=incident_type,
                description=description,
                contactNumber=contact_number,
                reportedBy=reported_by,
                unitId=unit_id
            )
            db.session.add(new_report)
            db.session.commit()
            flash('Report added successfully!', 'success')
            return redirect(url_for('views.incident_report'))
        else:
            new_report = IncidentReport(
            reportDate=report_date,
            incidentType=incident_type,
            description=description,
            contactNumber=contact_number,
            reportedBy=reported_by,
            unitId=unit_id
            )
            db.session.add(new_report)
            db.session.commit()
            flash('Report added successfully!', 'success')
            return redirect(url_for('views.incident_report'))

    # Determine the user's role and authentication status for conditional back button rendering
    user_role = getattr(current_user, 'roles', 'visitor')  # Default to 'visitor' if not authenticated or no role
    user_authenticated = current_user.is_authenticated

    return render_template("incident_report.html", 
                           user=current_user, 
                           user_role=user_role, 
                           user_authenticated=user_authenticated)

@views.route('/security_edit_incident/<int:report_id>', methods=['GET', 'POST'])
@role_required('security')
@login_required
def security_edit_incident(report_id):
    report = IncidentReport.query.get_or_404(report_id)
    
    if request.method == 'POST':
        # Here, you simply update the 'checked' status
        report.checked = True
        db.session.commit()
        flash('Incident report marked as checked.', 'success')
        return redirect(url_for('views.security_incident'))
    
    return render_template("security_edit_incident.html", report=report, user=current_user)

@views.route('/security_incident')
@role_required('security')
@login_required
def security_incident():
    # Fetching unchecked incident reports
    incident_reports = IncidentReport.query.filter_by(checked=False).all()
    return render_template("security_incident.html", incident_reports=incident_reports, current_user=current_user)

@views.route('/security_checked')
@role_required('security')
@login_required
def security_checked():
    # Fetching checked incident reports
    incident_reports = IncidentReport.query.filter_by(checked=True).all()
    return render_template("security_checked.html", incident_reports=incident_reports, current_user=current_user)

@views.route('/security_vehicle')
@role_required('security')
@login_required
def security_vehicle():
    # Get the current date and time
    current_time = datetime.utcnow()

    # Query for vehicle registrations with a parking duration later than the current time
    vehicle_registrations = VehicleRegistration.query.filter(
        VehicleRegistration.duration_of_park > current_time
    ).all()

    return render_template("security_vehicle.html", vehicle_registrations=vehicle_registrations, user=current_user)

@views.route('/visitor')
def visitor():
    return render_template("visitor.html", user=current_user)

@views.route('/visitor_registration', methods=['GET', 'POST'])
def visitor_registration():
    if request.method == 'POST':
        name = request.form.get('name')
        ic_number = request.form.get('ic_number')
        phone_number = request.form.get('phone_number')
        duration_of_stay = request.form.get('duration_of_stay')
        visiting_unit_number = request.form.get('visiting_unit_number')
        first_visitor = VisitorRegistration.query.filter_by(id=200000).first()
        
        try:
            duration_of_stay = datetime.strptime(duration_of_stay, '%Y-%m-%dT%H:%M')  
        except ValueError:
            flash('Invalid date format for duration of stay.', 'error')
            return redirect(url_for('views.visitor_registration'))

        if len(phone_number) < 10:
            flash('Phone number must be at least 10 digits.', 'error')
            return redirect(url_for('views.visitor_registration'))
        
        if len(ic_number) < 12 or len(ic_number) > 12:
            flash('IC number must be 12 digits no \'-\' in between.', 'error')
            return redirect(url_for('views.visitor_registration'))

        unit_exists = Registered_Unit.query.filter_by(unit=visiting_unit_number).first()
        if not unit_exists:
            flash('Unit number does not exist, registration denied.', 'error')
            return redirect(url_for('views.visitor_registration'))
        elif unit_exists.available == False:
            flash('Unit is not available. Please contact owner', 'error')
            return redirect(url_for('views.visitor_registration'))
        
        if duration_of_stay.date() < datetime.today().date():
            flash('Duration of stay cannot be earlier than today\'s date.', 'error')
            return redirect(url_for('views.visitor_registration'))
        
        if first_visitor is None:
            visitor = VisitorRegistration(
                id = 200000,
                name=name,
                ic_number=ic_number,
                phone_number=phone_number,
                duration_of_stay=duration_of_stay,
                unit=visiting_unit_number
            )
            db.session.add(visitor)
            db.session.commit()
            flash(f'Registration successful! Your registration ID is {visitor.id}.', 'success')
            return redirect(url_for('views.visitor_registration'))
        else:
            visitor = VisitorRegistration(
            name=name,
            ic_number=ic_number,
            phone_number=phone_number,
            duration_of_stay=duration_of_stay,
            unit=visiting_unit_number
            )

            db.session.add(visitor)
            db.session.flush()  # Flush to assign an ID to the visitor instance
            db.session.commit()

            flash(f'Registration successful! Your registration ID is {visitor.id}.', 'success')
            return redirect(url_for('views.visitor'))
    return render_template("visitor_registration.html", user=current_user)

@views.route('/preregister', methods=['GET', 'POST'])
@role_required('user', 'tenant')
def preregister():
    if request.method == 'POST':
        name = request.form.get('name')
        ic_number = request.form.get('ic_number')
        phone_number = request.form.get('phone_number')
        duration_of_stay = request.form.get('duration_of_stay')
        visiting_unit_number = request.form.get('visiting_unit_number')
        first_visitor = VisitorRegistration.query.filter_by(id=200000).first()
        
        try:
            duration_of_stay = datetime.strptime(duration_of_stay, '%Y-%m-%dT%H:%M')  
        except ValueError:
            flash('Invalid date format for duration of stay.', 'error')
            return redirect(url_for('views.visitor_registration'))

        if len(phone_number) < 10:
            flash('Phone number must be at least 10 digits.', 'error')
            return redirect(url_for('views.preregister'))
        
        if len(ic_number) < 12 or len(ic_number) > 12:
            flash('IC number must be 12 digits no \'-\' in between.', 'error')
            return redirect(url_for('views.preregister'))

        unit_exists = Registered_Unit.query.filter_by(unit=visiting_unit_number).first()
        if not unit_exists:
            flash('Unit number does not exist, registration denied.', 'error')
            return redirect(url_for('views.preregister'))
        elif unit_exists.available == False:
            flash('Unit is not available.', 'error')
            return redirect(url_for('views.preregister'))
        
        if duration_of_stay.date() < datetime.today().date():
            flash('Duration of stay cannot be earlier than today\'s date.', 'error')
            return redirect(url_for('views.visitor_registration'))
        if first_visitor is None:
            visitor = VisitorRegistration(
                id = 200000,
                name=name,
                ic_number=ic_number,
                phone_number=phone_number,
                duration_of_stay=duration_of_stay,
                unit=visiting_unit_number,
                owner_approved = True
            )
            db.session.add(visitor)
            db.session.commit()
            flash(f'Registration successful!', 'success')
            return redirect(url_for('views.userpage'))
        else:
            visitor = VisitorRegistration(
            name=name,
            ic_number=ic_number,
            phone_number=phone_number,
            duration_of_stay=duration_of_stay,
            unit=visiting_unit_number,
            owner_approved = True
            )

            db.session.add(visitor)
            db.session.flush()  # Flush to assign an ID to the visitor instance
            db.session.commit()

            flash(f'Registration successful!', 'success')
            return redirect(url_for('views.userpage'))
    return render_template("preregister.html", user=current_user, role=current_user.roles)

@views.route('/vehicle_registration', methods=['GET', 'POST'])
def vehicle_registration():
    if request.method == 'POST':
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        car_number = request.form.get('car_number')
        duration_of_park = request.form.get('duration_of_park')
        visiting_unit_number = request.form.get('visiting_unit_number')
        first_vehicle = VehicleRegistration.query.filter_by(id=500000).first()

        if len(phone_number) < 10:
            flash('Phone number must be at least 10 digits.', 'error')
            return redirect(url_for('views.vehicle_registration'))

        unit_exists = Registered_Unit.query.filter_by(unit=visiting_unit_number).first()
        if not unit_exists:
            flash('Unit number does not exist, registration denied.', 'error')
            return redirect(url_for('views.vehicle_registration'))
        
        duration_of_park_datetime = datetime.strptime(duration_of_park, '%Y-%m-%dT%H:%M')
        
        if duration_of_park_datetime.date() < datetime.today().date():
            flash('Duration of park cannot be earlier than today\'s date.', 'error')
            return redirect(url_for('views.vehicle_registration'))
        
        if first_vehicle is None:
            visitor = VehicleRegistration(
                id = 500000,
                name=name,
                phone_number=phone_number,
                car_number=car_number,
                duration_of_park = datetime.strptime(duration_of_park, '%Y-%m-%dT%H:%M'),
                unit=visiting_unit_number
            )
            db.session.add(visitor)
            db.session.commit()
            flash(f'Registration successful!', 'success')
            return redirect(url_for('views.vehicle_registration'))
        else:
            visitor = VehicleRegistration(
            name=name,
            phone_number=phone_number,
            car_number=car_number,
            duration_of_park = datetime.strptime(duration_of_park, '%Y-%m-%dT%H:%M'),
            unit=visiting_unit_number
            )

            db.session.add(visitor)
            db.session.flush()  # Flush to assign an ID to the visitor instance
            db.session.commit()

            flash(f'Registration successful!', 'success')
            return redirect(url_for('views.visitor'))
    return render_template("vehicle_registration.html", user=current_user)

@views.route('/generate_otp', methods=['GET', 'POST'])
@role_required('user', 'tenant')
def generate_otp():
    if request.method == 'POST':
        otp_number = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        creation_time = datetime.utcnow()  # Use UTC time for consistency
        new_otp = OTP(otp=otp_number, created_at=creation_time)  # Assuming OTP model has a created_at field
        db.session.add(new_otp)
        db.session.commit()
        session['otp_id'] = new_otp.id  # Store OTP ID in session to retrieve later
        flash(f'Your OTP is {otp_number}. It will expire in 10 minutes.', 'success')
        return redirect(url_for('views.generate_otp'))
    
    otp_info = None
    if 'otp_id' in session:
        otp_record = OTP.query.get(session['otp_id'])
        if otp_record and otp_record.is_valid():
            otp = otp_record.otp
            # Calculate expiration time based on the OTP creation time + 10 minutes
            expiration_time = otp_record.created_at + timedelta(minutes=10)
            # Convert times to ISO format for JavaScript
            current_time_iso = datetime.utcnow().isoformat() + 'Z'  # Append 'Z' to indicate UTC
            expiration_time_iso = expiration_time.isoformat() + 'Z'
            otp_info = {
                'otp': otp,
                'current_time': current_time_iso,
                'expiration_time': expiration_time_iso
            }
        else:
            session.pop('otp_id')  # Remove expired or used OTP from session
    
    return render_template('generate_otp.html', otp_info=otp_info, user=current_user)

@views.route('/verify_otp', methods=['GET', 'POST'])
@role_required('security')
def verify_otp():
    if request.method == 'POST':
        otp_number = request.form.get('otp')
        otp_record = OTP.query.filter_by(otp=otp_number).first()
        if otp_record and otp_record.is_valid():
            otp_record.used = True
            db.session.commit()
            flash('OTP verified successfully!', 'success')
        else:
            flash('Invalid or expired OTP.', 'error')
        return redirect(url_for('views.verify_otp'))
    return render_template('verify_otp.html', user=current_user)

@views.route('/security_visitor', methods=['GET', 'POST'])
@role_required('security')
@login_required
def security_visitor():
    visitor = None
    if request.method == 'POST':
        ic_number = request.form.get('ic_number')
        # Current date at 00:00:00 hours to exclude past times within today
        today_start = datetime.utcnow().date()

        # Adjust the query to exclude registrations where duration_of_stay is before today
        visitor = VisitorRegistration.query.filter(
            VisitorRegistration.ic_number == ic_number,
            VisitorRegistration.duration_of_stay >= today_start
        ).order_by(VisitorRegistration.duration_of_stay.desc()).first()

        if not visitor:
            flash('Visitor does not exist, the IC number is incorrect, or there are no scheduled future visits.', 'error')
            return redirect(url_for('views.security_visitor'))

    return render_template('security_visitor.html', user=current_user, visitor=visitor)

@views.route('/availability')
@role_required('user')
@login_required
def availability():
    # Assuming the 'ic' in Registered_Unit links to the current user
    user_units = Registered_Unit.query.filter_by(ic=current_user.ic).all()
    return render_template('availability.html', units=user_units, user=current_user)

@views.route('/update_availability/<int:unit_id>', methods=['POST'])
@role_required('user')
@login_required
def update_availability(unit_id):
    unit = Registered_Unit.query.get_or_404(unit_id)
    # Ensure the user is authorized to update this unit
    if unit.ic == current_user.ic:
        new_status = request.form.get('available') == 'true'
        unit.available = new_status
        db.session.commit()
        flash('Unit availability updated successfully!', 'success')
    else:
        flash('Unauthorized action.', 'danger')
    return redirect(url_for('views.availability'))

@views.route('/manage_account')
@role_required('user', 'tenant')
@login_required
def manage_account():
    # Pass 'role' as a string or list, depending on your implementation
    return render_template('manage_account.html', user=current_user, role=current_user.roles)

@views.route('/edit_account', methods=['GET', 'POST'])
@role_required('user', 'tenant')
@login_required
def edit_account():
    # This route renders the form for editing user details and processes the form submissions
    if request.method == 'POST':
        # Since this is handled by 'edit_user_details' and 'change_password', redirect accordingly
        return redirect(url_for('views.manage_account'))
    return render_template('edit_account.html', user=current_user, role=current_user.roles)

@views.route('/edit_user_details', methods=['POST'])
@role_required('user', 'tenant')
@login_required
def edit_user_details():
    # Your existing logic for updating user details
    phone_num = request.form.get('phone_num')
    email = request.form.get('email')
    user = User.query.get(current_user.id)
    if user:
        user.phone_num = phone_num
        user.email = email
        db.session.commit()
        flash('Your details have been updated.', 'success')
    else:
        flash('User not found.', 'error')
    return redirect(url_for('views.manage_account'))

@views.route('/change_password', methods=['POST'])
@role_required('user', 'tenant')
@login_required
def change_password():
    # Your existing logic for changing the password
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_new_password = request.form.get('confirm_new_password')
    
    user = User.query.get(current_user.id)
    if user and check_password_hash(user.password, old_password):
        if new_password == confirm_new_password:
            user.password = generate_password_hash(new_password, method='scrypt')
            db.session.commit()
            flash('Your password has been changed.', 'success')
        else:
            flash('Passwords do not match.', 'error')
    else:
        flash('Incorrect current password.', 'error')
    return redirect(url_for('views.manage_account'))

@views.route('/notify_owner', methods=['POST'])
def notify_owner():
    data = request.json
    duration_of_stay = datetime.strptime(data['duration_of_stay'], '%Y-%m-%d %H:%M:%S')  # Parse the date string
    first_noti = Notification.query.filter_by(id=1000000).first()
    
    if first_noti is None:
        new_notification = Notification(
            id = 1000000,
            visitor_name=data['visitor_name'],
            visitor_ic=data['visitor_ic'],
            unit=data['unit'],  
            message='A new visitor has requested access to your unit.',
            duration_of_stay=duration_of_stay  
        )
        db.session.add(new_notification)
        db.session.commit()
        return jsonify({"message": "Notification sent successfully"}), 200
    else:
        new_notification = Notification(
            visitor_name=data['visitor_name'],
            visitor_ic=data['visitor_ic'],
            unit=data['unit'],  
            message='A new visitor has requested access to your unit.',
            duration_of_stay=duration_of_stay  
        )
        db.session.add(new_notification)
        db.session.commit()
        return jsonify({"message": "Notification sent successfully"}), 200

@views.route('/notifications')
@role_required('user')
@login_required
def notifications():
    today = datetime.utcnow().date()

    # Find the Registered_Unit(s) associated with the current user's IC
    user_ic = current_user.ic
    user_units = Registered_Unit.query.filter_by(ic=user_ic).all()

    # Extract unit numbers from the user's units
    user_unit_numbers = [unit.unit for unit in user_units]

    # Fetch notifications for the units associated with the current user
    notifications = Notification.query.filter(
        Notification.unit.in_(user_unit_numbers),
        Notification.checked == False,
        Notification.duration_of_stay >= datetime(today.year, today.month, today.day)
    ).order_by(Notification.duration_of_stay.desc()).all()

    return render_template('notifications.html', notifications=notifications, user=current_user)


@views.route('/approve_visitor', methods=['POST'])
@role_required('user')
@login_required
def approve_visitor():
    data = request.json
    visitor_ic = data.get('visitor_ic')
    unit = data.get('unit')
    
    # Find the latest VisitorRegistration entry for the given IC and unit
    visitor_registration = VisitorRegistration.query.filter_by(ic_number=visitor_ic, unit=unit).order_by(VisitorRegistration.registration_date.desc()).first()
    
    if visitor_registration:
        visitor_registration.owner_approved = True
        # Now find and update the corresponding notification(s)
        Notification.query.filter_by(visitor_ic=visitor_ic, unit=unit).update({'checked': True})
        db.session.commit()
        return jsonify({'message': 'Visitor approved successfully.'}), 200
    
    return jsonify({'error': 'Visitor registration not found.'}),

@views.route('/manage_visitor')
@role_required('user')
@login_required
def manage_visitor():
    # Fetch all units owned by the current user
    user_units = Registered_Unit.query.filter_by(ic=current_user.ic).all()
    if not user_units:
        return redirect(url_for('views.index'), message="No units found for the current user.")

    # Extract unit numbers to a list for querying
    user_unit_numbers = [unit.unit for unit in user_units]

    # Query for visitors where the unit is in the user's units, duration of stay is in the future, and owner_approved is True
    visitors = VisitorRegistration.query.filter(
        VisitorRegistration.unit.in_(user_unit_numbers),
        VisitorRegistration.duration_of_stay > datetime.now(),
        VisitorRegistration.owner_approved == True  # Filter by owner_approved
    ).all()

    return render_template('manage_visitor.html', visitors=visitors, user=current_user)

@views.route('/unapprove_visitor/<int:visitor_id>', methods=['POST'])
@role_required('user')
@login_required
def unapprove_visitor(visitor_id):
    # Assuming current_user.ic contains the IC number of the logged-in user
    user_ic = current_user.ic

    # Fetch all units associated with the current user's IC number
    user_units = Registered_Unit.query.filter_by(ic=user_ic).all()
    user_unit_numbers = [unit.unit for unit in user_units]

    # Then, find the visitor with the given ID and ensure it belongs to one of these units
    visitor = VisitorRegistration.query.filter(
        VisitorRegistration.id == visitor_id,
        VisitorRegistration.unit.in_(user_unit_numbers)
    ).first()

    if visitor:
        visitor.owner_approved = False
        db.session.commit()
        flash('Visitor has been removed.', 'success')
    else:
        flash('Visitor not found or does not belong to your unit.', 'error')

    return redirect(url_for('views.manage_visitor'))

@views.route('/manage_tenant')
@role_required('user')
@login_required
def manage_tenant():
    # Define user_ic from the current_user
    user_ic = current_user.ic
    
    # Get all units associated with the current_user's IC
    user_units = Registered_Unit.query.filter_by(ic=user_ic).all()
    user_unit_numbers = [unit.unit for unit in user_units]

    # Get tenants for all units owned by the current_user
    tenants = User.query.filter(User.tenant_unit.in_(user_unit_numbers), User.roles.any(name='tenant')).all()

    return render_template('manage_tenant.html', tenants=tenants, user=current_user)

@views.route('/delete_tenant/<int:tenant_id>', methods=['POST'])
@role_required('user')
@login_required
def delete_tenant(tenant_id):
    tenant = User.query.filter_by(id=tenant_id).first()
    
    # Ensure the tenant belongs to the same unit and the current user has permission to delete
    if tenant and tenant.tenant_unit == current_user.tenant_unit:
        db.session.delete(tenant)
        db.session.commit()
        return jsonify({'message': 'Tenant deleted successfully'}), 200
    return jsonify({'error': 'Unauthorized or tenant not found'}), 403

@views.route('/security_blacklist', methods=['GET', 'POST'])
@role_required('security')  # Make sure only security personnel can access
@login_required
def security_blacklist():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        ic = request.form.get('ic')
        gender = request.form.get('gender')
        reason = request.form.get('reason')
        first_blacklist = Blacklist.query.filter_by(id=100).first()

        # Validate the inputs as needed and then create a new Blacklist entry
        if name and ic and gender and reason:  # Simple validation check
            if first_blacklist is None:
                new_entry = Blacklist(id = 100, name=name, ic=ic, gender=gender, reason=reason)
                db.session.add(new_entry)
                db.session.commit()
                flash('New entry added to the blacklist.', 'success')
            else:   
                new_entry = Blacklist(name=name, ic=ic, gender=gender, reason=reason)
                db.session.add(new_entry)
                db.session.commit()
                flash('New entry added to the blacklist.', 'success')
        else:
            flash('All fields are required.', 'error')

    # Always display the current blacklist
    blacklist_entries = Blacklist.query.all()
    return render_template('security_blacklist.html', blacklist_entries=blacklist_entries)

@views.route('/contact')
def contact():
    # Assuming you have a way to retrieve these numbers, for simplicity, they are hardcoded here
    security_phone = "+60 0367-8900"
    management_phone = "+60 0367-8901"
    
    security_email = "security@example.com"
    management_email = "management@example.com"

    return render_template('contact.html', 
                           security_phone=security_phone, 
                           management_phone=management_phone,
                           security_email=security_email,
                           management_email=management_email, user=current_user)


