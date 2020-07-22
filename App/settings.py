def get_db_uri(self, dbnfo):

    engine = dbnfo.get('ENGINE') or 'sqlite'
    driver = dbnfo.get('DRIVER') or 'sqlite'
    user = dbnfo.get('USER') or ''
    password = dbnfo.get('PASSWORD') or ''
    name = dbnfo.get('NAME') or ''
    host = dbnfo.get('HOST') or ''
    port = dbnfo.get('PORT') or ''

    return '{}+{}://{}:{}@{}:{}/{}'.format(engine,driver,user,password,name,host,port)




class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG= True
    dbinfo = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'',
        'PORT':'3306',
        'HOST':'localhost',
        'NAME':'helloflask'
    }
    SQLALCHEMY_DATABASE_URI  = get_db_uri(dbinfo)



class TestConfig(Config):
    TESTING= True
    dbinfo = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'',
        'PORT':'3306',
        'HOST':'localhost',
        'NAME':'helloflask'
    }
    SQLALCHEMY_DATABASE_URI  = get_db_uri(dbinfo)



class StagingConfig(Config):

    dbinfo = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'',
        'PORT':'3306',
        'HOST':'localhost',
        'NAME':'helloflask'
    }
    SQLALCHEMY_DATABASE_URI  = get_db_uri(dbinfo)

    class ProductConfig(Config):

        dbinfo = {
            'ENGINE': 'mysql',
            'DRIVER': 'pymysql',
            'USER': 'root',
            'PASSWORD': '',
            'PORT': '3306',
            'HOST': 'localhost',
            'NAME': 'helloflask'
        }
        SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)



