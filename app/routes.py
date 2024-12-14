from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from . import db
from .models import TaxRecord
from .forms import TaxRecordForm
import datetime

main_bp = Blueprint('main', __name__)

# Populate due date dropdown
def get_due_dates():
    current_year = datetime.datetime.now().year
    return [f"04/15/{current_year}", f"06/15/{current_year}", f"09/15/{current_year}", f"01/15/{current_year + 1}"]

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = TaxRecordForm()
    form.due_date.choices = get_due_dates()

    # Initialize the base query for fetching records
    query = TaxRecord.query

    # Apply filtering based on query params (status and due_date)
    status_filter = request.args.get('status')
    due_date_filter = request.args.get('due_date')

    if status_filter:
        query = query.filter(TaxRecord.status == status_filter)

    if due_date_filter:
        query = query.filter(TaxRecord.due_date == due_date_filter)

    # Fetch the filtered records from the database
    records = query.all()

    # Calculate total amount and tax due
    total_amount = sum(record.amount for record in records)
    tax_rate = 0.06  # Example tax rate (6%)
    tax_due = total_amount * tax_rate

    # Get current year and next year for the dropdown
    current_year = datetime.datetime.now().year
    next_year = current_year + 1

    if form.validate_on_submit():
        record = TaxRecord(
            company=form.company.data,
            amount=form.amount.data,
            payment_date=form.payment_date.data,
            status=form.status.data,
            due_date=form.due_date.data,
        )
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('index.html', form=form, records=records, total_amount=total_amount, tax_rate=tax_rate,
                           tax_due=tax_due, current_year=current_year, next_year=next_year)
