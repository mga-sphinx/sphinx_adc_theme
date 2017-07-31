"""Sphinx ADC theme.

Fork From https://github.com/coordt/ADCtheme/.

"""
import os
import xml.etree.ElementTree as ET

VERSION = (0, 1, 4)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__


def setup(app):
    app.connect('html-page-context', update_context)
    app.connect('html-page-context', add_html_link)
    app.connect('build-finished', create_sitemap)
    app.sitemap_links = []
    return {'version': __version__,
            'parallel_read_safe': True}

def get_html_theme_path():
    """Return list of HTML theme paths."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def get_theme_version():
    """Return the theme version"""
    return __version__

def update_context(app, pagename, templatename, context, doctree):
    context['adc_theme_version'] = __version__

def add_html_link(app, pagename, templatename, context, doctree):
    """As each page is built, collect page names for the sitemap"""
    base_url = app.config['html_theme_options'].get('base_url', '')
    if base_url:
        app.sitemap_links.append(base_url + pagename + ".html")

def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    if (not app.config['html_theme_options'].get('base_url', '') or
           exception is not None or
           not app.sitemap_links):
        return

    filename = app.outdir + "/sitemap.xml"
    print("Generating sitemap.xml in %s" % filename)

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = link

    ET.ElementTree(root).write(filename)
