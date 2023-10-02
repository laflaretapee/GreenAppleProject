from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.core.model import BaseModel
from src.core.config import load_config


class BaseRepository:
    engine = create_engine(load_config().db.alchemy_url)
    _model: BaseModel = NotImplemented
