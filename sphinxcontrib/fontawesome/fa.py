"""Font Awesome role and directive for Sphinx."""
import json
import os

from docutils import nodes
from docutils.parsers.rst.roles import set_classes


ICON_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'icons.json')
def filter_icons(path=ICON_PATH):
    """Load metadata about Font Awesome icons."""
    with open(path, 'r') as f:
        all_icons = json.load(f)
    icons = {
        key: {
            'styles': value['styles'],
            'unicode': value['unicode'],
            'label': value['label']
        }
        for key, value in all_icons.items()
    }
    return icons


class FontAwesomeIcon(nodes.inline):
    pass


def visit_icon_node(self, node):
    classes = ' '.join(node.get('classes', []))
    if not classes:
        raise nodes.SkipNode
    self.body.append('<i class="{classes}">'.format(classes=classes))


def depart_icon_node(self, node):
    self.body.append('</i>')


def latex_visit_icon_node(self, node):
    label = node.get('fa-label')
    if not label:
        raise nodes.SkipNode
    self.body.append('\n\\faicon{{{}}}'.format(label))


def latex_depart_icon_node(self, node):
    pass



def fa_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    if ' ' in text:
        label, style = text.split()
    else:
        label = text
        if label not in icons:
            style = 'regular'
        style = icons[label]['styles'][0]
    assert label in icons

    shorthand = {
        'regular': 'far',
        'solid': 'fas',
        'brands': 'fab',
        'light': 'fal',  # Pro only.
        'duotone': 'fad',  # Pro only.
    }
    assert style in shorthand
    assert style in icons[label]['styles']

    set_classes(options)  # But why?
    options.update(classes=[])

    options['classes'].append(shorthand.get(style, 'fa'))
    options['classes'].append('fa-{label}'.format(label=label))
    options['fa-label'] = label

    node = FontAwesomeIcon(rawtext, **options)

    return [node], []

# Global metadata about icons.
icons = filter_icons()
