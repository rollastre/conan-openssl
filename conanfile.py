#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile


class AliasConanfile(ConanFile):
    name = "OpenSSL"
    version = "1.0.2"
    _patch = 'q'
    alias = "{}/{}{}@conan/stable".format(name, version, _patch)
