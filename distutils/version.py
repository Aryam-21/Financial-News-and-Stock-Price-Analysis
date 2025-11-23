"""Provide `distutils.version` compatibility via `setuptools._distutils`.

Only the things commonly used by third-party packages are exported.
If `setuptools._distutils` isn't available, raise ImportError so callers
see an informative message.
"""
try:
    # setuptools bundles a vendored copy of distutils for newer Pythons
    from setuptools._distutils.version import LooseVersion, StrictVersion
except Exception as e:
    raise ImportError("setuptools._distutils is required for this compatibility shim: " + str(e))

__all__ = ["LooseVersion", "StrictVersion"]
