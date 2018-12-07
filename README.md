[![Build Status](https://travis-ci.org/conan-community/conan-openssl.svg?branch=master)](https://travis-ci.org/conan-community/conan-openssl)

# Conan OpenSSL

[Conan.io](https://conan.io) package **ALIAS** for OpenSSL library

The packages generated with this **conanfile** can be found in [Conan Center](https://bintray.com/conan-community/conan/OpenSSL%3Aconan/1.0.2%3Astable).

## ALIAS

This package is an alias for that latest OpenSSL 1.0.2 pacth version. The current target is **1.0.2q**

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Export alias

    $ conan alias OpenSSL/1.0.2@conan/stable OpenSSL/1.0.2q@conan/stable

## Upload packages to server

    $ conan upload OpenSSL/1.0.2@conan/stable

## Reuse the packages

### Basic setup

    $ conan install OpenSSL/1.0.2@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    OpenSSL/1.0.2@conan/stable

    [options]
    OpenSSL:shared=true # false
    # Take a look for all available options in conanfile.py

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
