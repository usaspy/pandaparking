from api import db

#停车场信息
class PARKING(db.Model):
    __tablename__='parking'
    uuid = db.Column(db.String(36),primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    pmc = db.Column(db.String(36))
    photos = db.Column(db.Text(65536))
    type = db.Column(db.Integer)
    service_kind = db.Column(db.Integer)
    service_time = db.Column(db.String(255))
    service_spaces = db.Column(db.Integer)
    location_x = db.Column(db.Float(8))
    location_y = db.Column(db.Float(8))
    state = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

#停车场收费规则
class PARKING_RULES(db.Model):
    __tablename__='parking_rules'
    id = db.Column(db.INT,primary_key=True, autoincrement=True)
    parking_id = db.Column(db.String(36))
    rule = db.Column(db.Text(65536))
    created_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

#车主常用车辆信息
class VEHICLE(db.Model):
    __tablename__='parking_rules'
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.INT,primary_key=True, autoincrement=True)
    owner_id = db.Column(db.String(36))
    vehicle_number = db.Column(db.String(255))
    vehicle_info = db.Column(db.Text(65536))
    created_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)