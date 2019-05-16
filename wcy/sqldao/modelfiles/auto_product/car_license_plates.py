# coding: utf-8
from sqlalchemy import Column, DECIMAL, Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CarLicensePlate(Base):
    __tablename__ = 'car_license_plates'
    __table_args__ = (
        Index('idx_car_sta', 'car_id', 'status'),
    )

    id = Column(INTEGER(10), primary_key=True)
    car_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    license_plate = Column(String(20), nullable=False, index=True, server_default=text("''"))
    license_plate_prefix = Column(String(5), nullable=False, server_default=text("''"))
    status = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    money = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("'1980-01-01 00:00:00'"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("'1980-01-01 00:00:00'"))
    tmp_license_plate = Column(String(20), nullable=False, server_default=text("''"))
    tmp_license_plate_prefix = Column(String(5), nullable=False, server_default=text("''"))
    express_number = Column(String(32), nullable=False, server_default=text("''"))
