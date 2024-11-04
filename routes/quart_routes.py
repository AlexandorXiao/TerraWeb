from libs.WebServer import quart_app
from quart import render_template, redirect, url_for, jsonify, request
from libs.DiscordOAuth import discordOAuth

print(f"Папка шаблонов: {quart_app.jinja_loader.searchpath}")

@quart_app.route("/")
async def index():
    return await render_template("index.html", logined=True, player_name="_ErrorNotFound")

@quart_app.route("/auth/discord/check")
async def check_auth():
    ds = await discordOAuth.fetch_user()
    return jsonify({
        "username": ds.username,
        "email": ds.email,
        "id": ds.id
    })

@quart_app.route("/auth/discord/login")
async def login():
    return await discordOAuth.create_session()

@quart_app.route("/auth/discord/callback")
async def callback():
    await discordOAuth.callback()
    return redirect(url_for(".check_auth"))

@quart_app.route("/auth/discord/logout")
async def logout():
    discordOAuth.revoke_token()
    return redirect(url_for(".check_auth"))