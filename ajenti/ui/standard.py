from ajenti.api import *
from ajenti.ui import p, UIElement


@p('width', default=None)
@p('height', default=None)
@p('scroll', default=False, type=bool)
@plugin
class Box (UIElement):
    typeid = 'box'


@p('text', default='', bindtypes=[str, unicode, int])
@plugin
class Label (UIElement):
    typeid = 'label'


@p('icon', default=None, bindtypes=[str, unicode])
@p('style', default='normal')
@plugin
class Icon (UIElement):
    typeid = 'icon'


@p('text', default='', bindtypes=[str, unicode])
@p('icon', default=None)
@p('style', default='normal')
@plugin
class Button (UIElement):
    typeid = 'button'


@p('value', default='', bindtypes=[str, unicode, int])
@p('type', default='text')
@plugin
class TextBox (UIElement):
    typeid = 'textbox'


@p('value', default='', bindtypes=[str, unicode])
@p('icon', default=None)
@p('placeholder', default=None)
@plugin
class Editable (UIElement):
    typeid = 'editable'


@p('text', default='')
@p('value', default=False, bindtypes=[bool])
@plugin
class CheckBox (UIElement):
    typeid = 'checkbox'


@p('items', default=[])
@p('values', default=[])
@p('value', default='', bindtypes=[str, unicode])
@plugin
class Dropdown (UIElement):
    typeid = 'dropdown'


@p('items', default=[])
@p('values', default=[])
@p('value', default='', bindtypes=[str, unicode])
@plugin
class Combobox (UIElement):
    typeid = 'combobox'


@p('text', default='', bindtypes=[str, unicode])
@plugin
class FormLine (UIElement):
    typeid = 'formline'


@p('text', default='', bindtypes=[str, unicode])
@plugin
class FormGroup (UIElement):
    typeid = 'formgroup'


@p('expanded', default=False, type=bool, bindtypes=[bool])
@plugin
class Collapse (UIElement):
    typeid = 'collapse'


@p('expanded', default=False, type=bool, bindtypes=[bool])
@plugin
class CollapseRow (UIElement):
    typeid = 'collapserow'


@p('buttons')
@plugin
class Dialog (UIElement):
    typeid = 'dialog'


@p('width', default=None)
@plugin
class Table (UIElement):
    typeid = 'dt'


@p('width', default=None)
@plugin
class TableCell (UIElement):
    typeid = 'dtd'


@p('text', default='', bindtypes=[str, unicode])
@p('width', default=None)
@plugin
class TableHeader (UIElement):
    typeid = 'dth'


@p('title', default='', bindtypes=[str, unicode])
@plugin
class Tab (UIElement):
    typeid = 'tab'


@p('active', default=0)
@plugin
class Tabs (UIElement):
    typeid = 'tabs'