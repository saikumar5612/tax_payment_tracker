from . import db

class TaxRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.String(50), nullable=True)  # Nullable for unpaid
    status = db.Column(db.String(10), nullable=False, default="unpaid")
    due_date = db.Column(db.String(50), nullable=False)
