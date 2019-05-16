# coding: utf-8
from sqlalchemy import Column, DateTime, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Car(Base):
    __tablename__ = 'cars'

    id = Column(INTEGER(10), primary_key=True)
    store_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    order_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    order_no = Column(String(32), nullable=False, index=True, server_default=text("''"))
    sku_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    model_code = Column(String(20), nullable=False, server_default=text("''"))
    frame_no = Column(String(50), nullable=False, index=True, server_default=text("''"))
    engine_no = Column(String(50), nullable=False, index=True, server_default=text("''"))
    invoice = Column(String(50), nullable=False, server_default=text("''"))
    user_id = Column(INTEGER(10), nullable=False)
    status = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    hosting_status = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("'1980-01-01 00:00:00'"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("'1980-01-01 00:00:00'"))
    merchant_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    lot_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    stock_input_at = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    stock_output_at = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    purchase_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    stock_up_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    province_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    city_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    validate_status = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    status_expire_at = Column(DateTime, server_default=text("'2099-12-31 23:59:59'"))
    status_update_at = Column(DateTime, server_default=text("'2099-12-31 23:59:59'"))
    dispatch_status = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    is_exhibit = Column(TINYINT(4), nullable=False, index=True, server_default=text("'0'"))
    listing_store_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"))
    listing_city_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"))
    exhibit_marked_time = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    last_location_status_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"))
    is_temp_license_plate_delivery = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    sale_status = Column(TINYINT(4), nullable=False, index=True, server_default=text("'0'"))
    stock_state = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    state = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    insurance_needs = Column(String(255), nullable=False, server_default=text("''"))
    recycle_status = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
