.. _adc: https://developer.apple.com/library/mac/navigation/
.. _bower: http://www.bower.io
.. _sphinx: http://www.sphinx-doc.org
.. _compass: http://www.compass-style.org
.. _sass: http://www.sass-lang.com
.. _grunt: http://www.gruntjs.com
.. _node: http://www.nodejs.com
.. _demo: http://mga-sphinx.github.io/sphinx_adc_theme
.. _hidden: http://sphinx-doc.org/markup/toctree.html

***************************************
Apple Developer Connection Sphinx Theme
***************************************

.. image:: https://travis-ci.org/mga-sphinx/sphinx_adc_theme.svg?branch=master
    :target: https://travis-ci.org/mga-sphinx/sphinx_adc_theme

.. contents:: 

This is a sphinx_ theme that made for adc_.

Installation
============

Via package
-----------

Download the package or add it to your ``requirements.txt`` file:

.. code:: bash

    $ pip install sphinx_adc_theme

In your ``conf.py`` file:

.. code:: python

    import sphinx_adc_theme

    html_theme = "sphinx_adc_theme"

    html_theme_path = [sphinx_adc_theme.get_html_theme_path()]

Via git or download
-------------------

Symlink or subtree the ``sphinx_adc_theme/sphinx_adc_theme`` repository into your documentation at
``docs/_themes/sphinx_adc_theme`` then add the following two settings to your Sphinx
conf.py file:

.. code:: python

    html_theme = "sphinx_adc_theme"
    html_theme_path = ["_themes", ]

Changelog
=========

0.1.2
-----

* Fix broken package on pypi

0.1.1
-----

* Fix Image path in CSS Broken
* Fix TOC.js nevers load


Contributing or modifying the theme
===================================

The sphinx_adc_theme is primarily a sass_ project that requires a few other sass libraries. I'm
using bower_ to manage these dependencies and sass_ to build the css. The good news is
I have a very nice set of grunt_ operations that will not only load these dependencies, but watch
for changes, rebuild the sphinx demo docs and build a distributable version of the theme.
The bad news is this means you'll need to set up your environment similar to that
of a front-end developer (vs. that of a python developer). That means installing node and ruby.

Set up your environment
-----------------------

1. Install sphinx_ into a virtual environment.

.. code::

    pip install sphinx

2. Install sass

.. code::

    gem install sass

2. Install node, bower and grunt.

.. code::

    // Install node
    brew install node

    // Install bower and grunt
    npm install -g bower grunt-cli

    // Now that everything is installed, let's install the theme dependecies.
    npm install

Now that our environment is set up, make sure you're in your virtual environment, go to
this repository in your terminal and run grunt:

.. code::

    grunt

This default task will do the following **very cool things that make it worth the trouble**.

1. It'll install and update any bower dependencies.
2. It'll run sphinx and build new docs.
3. It'll watch for changes to the sass files and build css from the changes.
4. It'll rebuild the sphinx docs anytime it notices a change to .rst, .html, .js
   or .css files.


Before you create an issue
--------------------------

I don't have a lot of time to maintain this project due to other responsibilities.
I know there are a lot of Python engineers out there that can't code sass / css and
are unable to submit pull requests. That said, submitting random style bugs without
at least providing sample documentation that replicates your problem is a good
way for me to ignore your request. RST unfortunately can spit out a lot of things
in a lot of ways. I don't have time to research your problem for you, but I do
have time to fix the actual styling issue if you can replicate the problem for me.


Before you send a Pull Request
------------------------------

When you're done with your edits, you can run ``grunt build`` to clean out the old
files and rebuild a new distribution, compressing the css and cleaning out
extraneous files. Please do this before you send in a PR.


