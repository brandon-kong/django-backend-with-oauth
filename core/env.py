import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cast values and assign 
env = environ.Env(
    # Debugging
    DEBUG                    = (bool, True),

    # Security
    ALLOWED_HOSTS            = (list, []),
    CORS_ORIGIN_WHITELIST    = (list, []),

    # Database
    DATABASE_URL             = (str, 'sqlite:///db.sqlite3'),

    # Secret
    SECRET_KEY               = (str, 'secret'),
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))