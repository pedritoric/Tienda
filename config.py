class Config:
    SECRET_KEY='1234567890@@##12345'

class Developmentconfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'gmC9SBPooUWv]_AG'
    MYSQL_DB = 'tienda'

config = {
    'development':Developmentconfig,
    'default':Developmentconfig
}

