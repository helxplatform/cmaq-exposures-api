import sys
import os
from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from sqlalchemy.orm import sessionmaker

parser = ConfigParser()
parser.read('swagger_server/ini/connexion.ini')
parser.set("postgres", "host", os.environ.get("POSTGRES_HOST"))
parser.set("postgres", "port", os.environ.get("POSTGRES_PORT"))
parser.set("postgres", "database", os.environ.get("POSTGRES_DATABASE"))
parser.set("postgres", "username", os.environ.get("POSTGRES_USERNAME"))
parser.set("postgres", "password", os.environ.get("POSTGRES_PASSWORD"))
POSTGRES_ENGINE = 'postgresql://' + parser.get('postgres', 'username') + ':' + parser.get('postgres', 'password') \
                  + '@' + parser.get('postgres', 'host') + ':' + parser.get('postgres', 'port') \
                  + '/' + parser.get('postgres', 'database')
sys.path.append(parser.get('sys-path', 'exposures'))
engine = create_engine(POSTGRES_ENGINE, poolclass=NullPool, echo=True)
Session = sessionmaker(bind=engine)
