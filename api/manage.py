from __init__ import db

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    reporting = db.Column(db.String(120), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=True)

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" :self.name,
            "role" :self.role,
            "experience" :self.experience,
            "reporting" : self.reporting,
            "joined_at" :self.joined_at,
        }