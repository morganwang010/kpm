import os


class Config(object):
    """ Default configuration """
    DEBUG = False
    KUBE_APIMASTER = os.getenv('KUBE_APIMASTER', 'http://localhost:8001')
    KPM_REGISTRY_HOST = os.getenv('KPM_REGISTRY_HOST', 'http://localhost:5000')
    KPM_BUILDER_HOST = os.getenv('KPM_BUILDER_HOST', 'http://localhost:5000')
    KPM_URI = os.getenv('KPM_URI', "http://localhost:5000")
    KPM_MODELS_MODULE = os.getenv('KPM_MODELS_MODULE', "kpm.models.etcd")
    KPM_MODELS = os.getenv('KPM_MODELS', '{"Package": "kpm.models.etcd.package:Package"}')


class ProductionConfig(Config):
    """ Production configuration """
    KPM_URI = 'https://api.kpm.sh'


class DevelopmentConfig(Config):
    """ Development configuration """
    DEBUG = True
#    KPM_URI = 'https://api.kpm.sh'
    KPM_URI = os.getenv('KPM_URI', "http://localhost:5000")
