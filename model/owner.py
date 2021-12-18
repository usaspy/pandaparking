from api import db

#车主信息
class OWNER(db.Model):
    __tablename__='owner'
    uuid = db.Column(db.String(36),primary_key=True)
    wx_id = db.Column(db.String(255))
    wx_phone = db.Column(db.String(255))
    the_last_order = db.Column(db.String(36))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

#常用停车场
class OWNER_PARKING(db.Model):
    __tablename__='owner_parking'
    id = db.Column(db.INT,primary_key=True, autoincrement=True)
    owner_id = db.Column(db.String(36))
    parking_id = db.Column(db.String(36))
    created_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)