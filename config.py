class Config(object):
    ABC=''

class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True


config_dict = {"Production": ProductionConfig, "Debug": DebugConfig}