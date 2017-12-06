from __future__ import absolute_import

import hashlib
import os

from django.conf import settings
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from django.template import TemplateDoesNotExist, Origin
from django.template.loaders.base import Loader as BaseLoader
from django.utils._os import safe_join
from django.utils.functional import cached_property
from pypugjs import process
from pypugjs.ext.django import Compiler
from pypugjs.utils import process

from .compiler import Compiler


class Loader(BaseLoader):
    is_usable = True

    def __init__(self, engine, loaders, dirs=None):
        self.dirs = dirs
        self.engine = engine
        self.template_cache = {}
        self._loaders = loaders

    @cached_property
    def loaders(self):
        return self.engine.get_template_loaders(self._loaders)

    def reset(self):
        """ Empty the template cache. """
        self.template_cache.clear()

    def get_dirs(self):
        return self.dirs if self.dirs is not None else self.engine.dirs

    def get_contents(self, origin):

        contents = self.template_cache.get(origin.name)
        if settings.DEBUG or not contents:
            if os.path.splitext(origin.template_name)[1] in ('.pug', '.jade'):
                try:
                    contents = origin.loader.get_contents(origin)
                    contents = process(contents, filename=origin.template_name, compiler=Compiler)
                except FileNotFoundError:
                    raise TemplateDoesNotExist(origin)
            else:
                contents = origin.loader.get_contents(origin)
            self.template_cache[origin.name] = contents

        return contents

    def get_template_sources(self, template_name):
        """
        Only forward the internal loaders sources.
        """
        for loader in self.loaders:
            for origin in loader.get_template_sources(template_name):
                yield origin
