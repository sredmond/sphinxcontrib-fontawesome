"""Support for `Font Awesome`_ icons and logos in Sphinx documentation."""
from .fa import (fa_role, FontAwesomeIcon,
    visit_icon_node, depart_icon_node,
    latex_visit_icon_node, latex_depart_icon_node)

__version__ = '0.0.1'


def setup(app):
    app.add_node(FontAwesomeIcon,
                 html=(visit_icon_node, depart_icon_node),
                 latex=(latex_visit_icon_node, latex_depart_icon_node),
                 text=(visit_icon_node, depart_icon_node),
                 man=(visit_icon_node, depart_icon_node),
                 texinfo=(visit_icon_node, depart_icon_node))

    app.add_css_file('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css')
    app.add_js_file('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js')
    app.add_latex_package('fontawesome')
    # For whatever reason, pdflatex and xelatex aren't working with my fontawesome installation.
    app.config.latex_engine = 'lualatex'

    # Define a custom role. Eventually, add a directive or updates to a prolog for substitutions.
    app.add_role('fa', fa_role)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
