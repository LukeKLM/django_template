from .settings import *  # noqa

DEBUG = True
DEBUG_TOOLBAR = False

INTERNAL_IPS = ["127.0.0.1"]

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(os.environ.get("PROJECT_HOME_DIR", ""), "tmp/emails/")
BASE_PROTOCOL = "http://"
BASE_URL = BASE_PROTOCOL + os.environ.get("PROJECT_MAIN_DOMAIN", default="")
os.makedirs(EMAIL_FILE_PATH, exist_ok=True)
