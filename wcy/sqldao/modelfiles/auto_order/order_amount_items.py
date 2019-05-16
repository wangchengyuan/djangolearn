# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OrderAmountItem(Base):
    __tablename__ = 'order_amount_items'

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(INTEGER(11), nullable=False, index=True)
    item_type = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
    item_amount = Column(DECIMAL(15, 2), nullable=False, server_default=text("'0.00'"))
    item_description = Column(String(500), nullable=False, server_default=text("''"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("'1989-01-01 00:00:00'"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    status = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
