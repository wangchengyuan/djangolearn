# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Asset(Base):
    __tablename__ = 'assets'

    id = Column(BIGINT(20), primary_key=True)
    related_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"))
    type = Column(TINYINT(4), nullable=False)
    file_name = Column(String(100), nullable=False, server_default=text("''"))
    file_path = Column(String(100), nullable=False, server_default=text("''"))
    status = Column(TINYINT(4), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, index=True, server_default=text("'1980-01-01 00:00:00'"))
    updated_at = Column(TIMESTAMP, nullable=False, index=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
