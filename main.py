from conf.main_config import WebConfiguration as web_cfg
from routes.fastapi_routes import fastapi_app
from routes.quart_routes import quart_app
# from libs.Sentry import sentry_sdk
# from sentry_sdk.integrations.asgi import SentryAsgiMiddleware bitch7

fastapi_app.mount("/", quart_app)

if __name__ == '__main__':
    # fastapi_app = SentryAsgiMiddleware(fastapi_app)
    import uvicorn
    uvicorn.run(
        "__main__:fastapi_app",
        host=web_cfg.host,
        port=web_cfg.port,
        log_level=web_cfg.log_level,
        reload=True,
    )