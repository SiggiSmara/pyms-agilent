#!/usr/bin/env python3

# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import os
import re
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath(".."))

# this package
from __pkginfo__ import __version__

github_username = "PyMassSpec"
github_repository = "pyms-agilent"
github_url = f"https://github.com/{github_username}/{github_repository}"

rst_prolog = f""".. |pkgname| replace:: pyms-agilent
.. |pkgname2| replace:: ``pyms-agilent``
.. |browse_github| replace:: `Browse the GitHub Repository <{github_url}>`__
"""

author = "Dominic Davis-Foster"
project = "pyms-agilent".replace('_', '-')
slug = re.sub(r'\W+', '-', project.lower())
release = version = __version__
copyright = "2019-2021 Dominic Davis-Foster"  # pylint: disable=redefined-builtin
language = "en"
package_root = "pyms_agilent"

extensions = [
		"sphinx_toolbox",
		"sphinx_toolbox.more_autodoc",
		"sphinx_toolbox.more_autosummary",
		"sphinx_toolbox.documentation_summary",
		"sphinx_toolbox.tweaks.param_dash",
		"sphinx_toolbox.tweaks.latex_toc",
		"sphinx.ext.intersphinx",
		"sphinx.ext.mathjax",
		"sphinxcontrib.httpdomain",
		"sphinxcontrib.extras_require",
		"sphinx.ext.todo",
		"sphinxemoji.sphinxemoji",
		"notfound.extension",
		"sphinx_copybutton",
		"sphinxcontrib.default_values",
		"sphinxcontrib.toctree_plus",
		"sphinx_debuginfo",
		"seed_intersphinx_mapping",
		"enum_tools.autoenum",
		"attr_utils.annotations",
		"attr_utils.autoattrs",
		"chemistry",
		]

sphinxemoji_style = "twemoji"
todo_include_todos = bool(os.environ.get("SHOW_TODOS", 0))
gitstamp_fmt = "%d %b %Y"

templates_path = ["_templates"]
html_static_path = ["_static"]
source_suffix = ".rst"
master_doc = "index"
suppress_warnings = ["image.nonlocal_uri"]
pygments_style = "default"

intersphinx_mapping = {
		"python": ("https://docs.python.org/3/", None),
		"sphinx": ("https://www.sphinx-doc.org/en/stable/", None),
		}

html_theme = "domdf_sphinx_theme"
html_theme_options = {"logo_only": False}
html_theme_path = ["../.."]
html_show_sourcelink = True  # True will show link to source

html_context = {
		"display_github": True,
		"github_user": "PyMassSpec",
		"github_repo": "pyms-agilent",
		"github_version": "master",
		"conf_py_path": "/doc-source/",
		}
htmlhelp_basename = slug

latex_documents = [("index", f'{slug}.tex', project, author, "manual")]
man_pages = [("index", slug, project, [author], 1)]
texinfo_documents = [("index", slug, project, author, slug, project, "Miscellaneous")]

toctree_plus_types = {
		"class",
		"function",
		"method",
		"data",
		"enum",
		"flag",
		"confval",
		"directive",
		"role",
		"confval",
		"protocol",
		"typeddict",
		"namedtuple",
		"exception",
		}

add_module_names = False
hide_none_rtype = True
all_typevars = True
overloads_location = "bottom"
documentation_summary = "PyMassSpec interface to Agilent .d datafiles"

autodoc_exclude_members = [   # Exclude "standard" methods.
		"__dict__",
		"__class__",
		"__dir__",
		"__weakref__",
		"__module__",
		"__annotations__",
		"__orig_bases__",
		"__parameters__",
		"__subclasshook__",
		"__init_subclass__",
		"__attrs_attrs__",
		"__init__",
		"__new__",
		"__getnewargs__",
		"__abstractmethods__",
		"__hash__",
		]
autodoc_default_options = {
		"members": None,  # Include all members (methods).
		"special-members": None,
		"autosummary": None,
		"show-inheritance": None,
		"exclude-members": ','.join(autodoc_exclude_members),
		}
