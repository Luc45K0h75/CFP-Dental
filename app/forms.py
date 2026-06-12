from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class BookingForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired("First name is required."), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired("Last name is required."), Length(max=50)])
    email = StringField('Email', validators=[DataRequired("Email is required."), Email(), Length(max=120)])
    message = StringField('Message', validators=[DataRequired("Message is required."), Length(max=500)])
    phone = StringField('Phone Number', validators=[DataRequired("Phone number is required."), Length(max=20)])
    
