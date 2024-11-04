from quart_redis import RedisHandler
from libs.WebServer import quart_app
from conf.main_config import Redis as redis_cfg

redis = RedisHandler(quart_app, conn_uri="redis://localhost:6379", conn_attempts=5)