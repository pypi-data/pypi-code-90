# Published at https://pypi.org/project/acryl-datahub/.
__package_name__ = "acryl-datahub"
__version__ = "0.8.6.0"


def is_dev_mode() -> bool:
    return __version__ == "0.0.0.dev0"


def nice_version_name() -> str:
    if is_dev_mode():
        return "unavailable (installed editable via git)"
    return __version__
