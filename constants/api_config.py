from datetime import timedelta

SECRET_KEY = "D7|}I,)D'8MjU5%hZg&k,mQbU9'bO"
JWT_COOKIE_SECURE = False
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=48)
PROPAGATE_EXCEPTIONS = True