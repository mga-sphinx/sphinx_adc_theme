"""Sphinx ADC theme.

Fork From https://github.com/coordt/ADCtheme/.

"""
import os

VERSION = (0, 1, 1)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
