from split_settings.tools import include
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Include base settings
include('base.py')

# Map environment modes to corresponding settings files
ENV_MODE_MAP = {
    'development': 'development.py',
    'production': 'production.py',
    'testing': 'testing.py',
}

# Get the current environment mode
env_mode = env.str('ENV_MODE', default='development')

# Include the corresponding settings file
include(ENV_MODE_MAP.get(env_mode, 'development.py'))