class Config(object):
    DEBUG = False
    TESTING = False
    
    """
    To generate secret key, from python shell type the following:
    >>> import binascii
    >>> binascii.hexlify(os.urandom(24))
    b'0ccd512f8c3493797a23557c32db38e7d51ed74f14fa7580'
    """

    SECRET_KEY = "a7444c03378a58bff0b0de61dc9d954496d6676396a0dc7f"
    
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    SECRET_KEY = "4571028dc68c6e149749584f2dfae7db078a5ad3b84ec893"


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"
    
    SESSION_COOKIE_SECURE = False

