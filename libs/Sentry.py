import sentry_sdk
from conf.main_config import SentrySDK as sentry_cfg

sentry_sdk.init(
    dsn=sentry_cfg.dsn,
    traces_sample_rate=sentry_cfg.traces_sample_rate,
    profiles_sample_rate=sentry_cfg.profiles_sample_rate,
    server_name=sentry_cfg.server_name,
)
