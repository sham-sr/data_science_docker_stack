import os
UPLOAD_FOLDER = "/uploads/"
MAPBOX_API_KEY = os.getenv('pk.eyJ1Ijoic2hhbXNyIiwiYSI6ImNram9rY2EzZDEycHYyeHRmbHl4amp1czIifQ.6iRHt70f5SK3yFmqVnq4GA', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://superset_admin:Kolema_2159@mysql:3306/superset?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'rtfdg534sdvsd345bd564gdf3453dfbh'
ENABLE_PROXY_FIX = True

