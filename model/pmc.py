from api import db

class STAFF_PARKING(db.Model):
    __tablename__='staff_parking'
    id = db.Column(db.INT,primary_key=True, autoincrement=True)
    staff_id = db.Column(db.String(36)) #
    parking_id = db.Column(db.String(36))
    created_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

#物业公司信息
class PMC(db.Model):
    __tablename__ = 'pmc'
    uuid = db.Column(db.String(36),primary_key=True)
    name = db.Column(db.String(255))

#物业员工
class STAFF(db.Model):
    __tablename__ = 'staff'
    uuid = db.Column(db.String(36),primary_key=True)
    name = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    pmc = db.Column(db.String(36))
    wx_id = db.Column(db.String(255))
    wx_phone = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
