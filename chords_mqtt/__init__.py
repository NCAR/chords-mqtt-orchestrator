from pkg_resources import DistributionNotFound, get_distribution

from . import config  # noqa: F401

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # Package is not installed
    pass
