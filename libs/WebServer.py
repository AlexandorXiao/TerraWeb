from quart import Quart
import os
from fastapi import FastAPI
from secrets import token_hex as secret_token
from conf.main_config import WebConfiguration as web_cfg


quart_app = Quart(__name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'html'), static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets'))
quart_app.secret_key = secret_token(48)

fastapi_app = FastAPI(
    docs_url=web_cfg.docs_url, 
    redoc_url=web_cfg.redoc_url,
    )