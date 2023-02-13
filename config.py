class Config:
    DEBUG = True
    DEVELOPMENT = True
    APP_NAME = 'xia-tutorial-example-0001'
    APP_DESCRIPTION = "X-I-A Example - 0001"
    RESOURCE_MAPPING = {
    }


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = True
    DEVELOPMENT = False
