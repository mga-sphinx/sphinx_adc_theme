"""Sphinx ADC theme.

Fork From https://github.com/coordt/ADCtheme/.

"""
import os
from pkg_resources import get_distribution, DistributionNotFound

try:
    release = get_distribution('sphinx_adc_theme').version
    __version__ = '.'.join(release.split('.')[:2])
    __version_full__ = release  # Keep for old compatibility
except DistributionNotFound:
    # package is not installed
    __version__ = None
    __version_full__ = None

def get_html_theme_path():
    """Return list of HTML theme paths."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def get_theme_version():
    """Return the theme version"""
    return __version__

def update_context(app, pagename, templatename, context, doctree):
    context['adc_theme_version'] = __version__

def setup(app):
    app.connect('html-page-context', update_context)
    app.add_html_theme('sphinx_adc_theme', get_html_theme_path())
    return {'version': __version__,
            'parallel_read_safe': True}
