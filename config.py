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

    #UPLOADS = "/home/username/app/app/static/images/uploads"
    #IMAGE_UPLOADS = "/home/theo/workspace/flask-starter-template/app/static/img/uploads"
    ALLOWED_IMAGE_EXTENSIONS = ["PNG", "JPG", "JPEG", "GIF"]
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024
    # CLIENT_IMAGES = "home/theo/workspace/flask-starter-template/app/static/client/img"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    SECRET_KEY = "4571028dc68c6e149749584f2dfae7db078a5ad3b84ec893"


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    #UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"
    IMAGE_UPLOADS = "/home/theo/workspace/flask-starter-template/app/static/img/uploads"
    CLIENT_IMAGES = "/home/theo/workspace/flask-starter-template/app/static/client/img"
    CLIENT_CSV = "/home/theo/workspace/flask-starter-template/app/static/client/csv"
    CLIENT_PDF = "/home/theo/workspace/flask-starter-template/app/static/client/pdf"
    CLIENT_REPORTS = "/home/theo/workspace/flask-starter-template/app/static/client/reports"





    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    #UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"
    
    SESSION_COOKIE_SECURE = False

