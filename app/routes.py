from flask import Blueprint, render_template, flash, redirect, url_for, send_from_directory
from .forms import BookingForm
from . import mail
from flask_mail import Message
import os

main = Blueprint('main', __name__)

@main.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(main.root_path, '..'), 'robots.txt')

@main.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(main.root_path, '..'), 'sitemap.xml')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/services')
def services():
    return render_template('services.html') 

@main.route('/team')
def team():
    return render_template('team.html')

@main.route('/book', methods=['GET', 'POST'])
def book():
    booking_form = BookingForm()
    if booking_form.validate_on_submit():
        # Send email
        msg = Message(
            subject=f'New Booking Request — {booking_form.first_name.data} {booking_form.last_name.data}',
            sender=os.getenv('MAIL_USERNAME'),
            recipients=[os.getenv('MAIL_RECEIVER')],
            reply_to=booking_form.email.data,
            body=f"""New booking request from {booking_form.first_name.data} {booking_form.last_name.data} on the CFP Dental website.

Phone: {booking_form.phone.data}
Email: {booking_form.email.data}

Message: {booking_form.message.data}
        """
        )
        mail.send(msg)
        flash('Your booking request has been submitted successfully!', 'success')
        return redirect(url_for('main.book'))
    return render_template('book.html', form=booking_form)