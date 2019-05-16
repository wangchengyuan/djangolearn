# coding: utf-8
from sqlalchemy import CHAR, Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    signer_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    mobile = Column(String(11), nullable=False, index=True, server_default=text("''"))
    truename = Column(String(45), nullable=False, index=True, server_default=text("''"))
    id_number = Column(CHAR(20), nullable=False, unique=True)
    is_test = Column(INTEGER(3), nullable=False, index=True, server_default=text("'0'"))
    gender = Column(INTEGER(3), nullable=False)
    phone = Column(String(20), nullable=False, server_default=text("''"))
    _from = Column('from', String(30), nullable=False, server_default=text("''"))
    refer = Column(String(30), nullable=False, server_default=text("''"))
    created_at = Column(TIMESTAMP, nullable=False, index=True, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, index=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    status = Column(SMALLINT(3), nullable=False, server_default=text("'200'"))
