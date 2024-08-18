from . import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    lastLogin = db.Column(db.DateTime, default=func.now())
    isVerified = db.Column(db.Boolean, default=False)
    
    resetPasswordToken = db.Column(db.String(255))
    resetPasswordExpiresAt = db.Column(db.DateTime)
    verificationToken = db.Column(db.String(255))
    verificationTokenExpiresAt = db.Column(db.DateTime)

    # Timestamps for created_at and updated_at
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())