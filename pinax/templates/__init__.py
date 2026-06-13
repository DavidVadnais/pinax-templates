from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pinax-templates")
except PackageNotFoundError:
    __version__ = "unknown"

default_app_config = "pinax.templates.apps.AppConfig"
