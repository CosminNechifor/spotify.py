from . import utils
from .utils import OAuth2

_types = utils._spotify__lookup()

from .errors import *
from .models import *

from .client import Client
from .local import LocalClient
from .http import HTTPClient, HTTPUserClient

__title__ = 'spotify'
__author__ = 'mental'
__license__ = 'MIT'
__version__ = '0.1.9'
