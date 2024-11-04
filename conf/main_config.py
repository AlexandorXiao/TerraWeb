class WebConfiguration:
    host = "0.0.0.0"
    port = 8080
    log_level = "debug"
    
    docs_url = "/api/docs"
    redoc_url = "/api/redocs"

class SentrySDK:
    server_name = ""
    dsn = ""
    traces_sample_rate = 1.0
    profiles_sample_rate = 1.0

class Database:
    host = "localhost"
    port = 3306
    user = "admin"
    password = "secret"
    database = "devlopment"

class Cloudflare:
    ip_ranges = [
        "173.245.48.0/20",
        "103.21.244.0/22",
        "103.22.200.0/22",
        "103.31.4.0/22",
        "141.101.64.0/18",
        "108.162.192.0/18",
        "190.93.240.0/20",
        "188.114.96.0/20",
        "197.234.240.0/22",
        "198.41.128.0/17",
        "162.158.0.0/15",
        "104.16.0.0/13",
        "104.24.0.0/14",
        "172.64.0.0/13",
        "131.0.72.0/22",
        "2400:cb00::/32",
        "2606:4700::/32",
        "2803:f800::/32",
        "2405:b500::/32",
        "2405:8100::/32",
        "2a06:98c0::/29",
        "2c0f:f248::/32",
    ]

class RedisAPI:
    conn_uri = "redis://localhost"
    conn_attempts = 5

class DiscordOauth:
    client_id = 0
    client_secret = ""
    redirect_uri = "http://localhost:8080/auth/discord/callback"
    bot_token = ""