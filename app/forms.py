from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TaxRecordForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    payment_date = StringField('Payment Date')
    status = SelectField('Status', choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], validators=[DataRequired()])
    due_date = SelectField('Due Date', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')
