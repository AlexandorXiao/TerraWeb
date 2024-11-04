from quart_discord import DiscordOAuth2Session
from libs.WebServer import quart_app
from conf.main_config import DiscordOauth as ds_cfg

discordOAuth = DiscordOAuth2Session(client_id=ds_cfg.client_id, client_secret=ds_cfg.client_secret, redirect_uri=ds_cfg.redirect_uri, bot_token=ds_cfg.bot_token, app=quart_app)