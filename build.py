#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    conan_packager = ConanMultiPackager()
    reference = conan_packager.reference.__repr__()
    recipe_data = conan_packager.conan_api.inspect(".", ["alias"])
    conan_packager.conan_api.export_alias(reference, recipe_data["alias"])
    conan_packager.uploader.upload_packages(reference, upload=conan_packager._upload_enabled(), package_id=None)