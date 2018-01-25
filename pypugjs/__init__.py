__version__ = '5.1.1'
from __future__ import absolute_import

from .compiler import Compiler  # noqa
from .ext import html
from .filters import register_filter  # noqa
from .parser import Parser  # noqa
from .utils import process  # noqa


def simple_convert(template):
    return html.process_pugjs(template)
