"""Minimal shim for the `distutils` namespace.

This package provides a small compatibility shim that re-exports
the `version` helpers from `setuptools._distutils` so older packages
that do `from distutils.version import LooseVersion` continue to work
in environments where the stdlib `distutils` is not available.
"""
from .version import *
