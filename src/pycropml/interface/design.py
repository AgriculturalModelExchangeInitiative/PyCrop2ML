from __future__ import print_function
from IPython.display import display
from ipywidgets import Button, widgets, VBox, HBox

words=["Inputs-Outputs", "Function", "Algorithm", "Description"]
tab1 = [Button(description=w) for w in words]
out= widgets.Output()

tab3 = widgets.IntText(description='a')
tab4 = widgets.IntText(description='bb')
tab2 = widgets.Tab(children=[tab3, tab4])
tab2.set_title(0, 'Create')
tab2.set_title(1, 'Edit')

def inout_button_clicked(b):
    tab1[0].description="Inputs-Outputs"
    with out:
        print("Button clicked.")
        display(widgets.IntText(description="a"))

def func_button_clicked(b):
    tab1[1].description="Functions"
    with out:
        print("Button clicked.")
        display(widgets.IntText(description="a"))

tab1[0].on_click(inout_button_clicked)
tab1[1].on_click(func_button_clicked)
vtab1=VBox([HBox([tab1[0], tab1[1]]), HBox([tab1[2], tab1[3]]), out])

tab = widgets.Tab(children=[vtab1, tab2])

tab.set_title(0, 'Create')
tab.set_title(1, 'Edit')

d = VBox(children=[tab])



from traitlets import (
    Unicode,
    Instance,
    Bool,
    Integer,
    Dict,
    List,
    Tuple,
    Any,
    All,
    parse_notifier_name
)
from itertools import chain
class cropGridWidget(widgets.DOMWidget):
    _view_name = Unicode('CropgridView').tag(sync=True)
    _model_name = Unicode('CropGridModel').tag(sync=True)
    _view_module = Unicode('CropGrid').tag(sync=True)
    _model_module = Unicode('CropGrid').tag(sync=True)
    _view_module_version = Unicode('1.1.1').tag(sync=True)
    _model_module_version = Unicode('1.1.1').tag(sync=True)
    def __init__(self,*args, **kwargs):

        self._handlers = _EventHandlers()
        widgets.DOMWidget.__init__(self)

    def on(self, names, handler):
        self._handlers.on(names, handler)
    
    def off(self, names, handler):
        self._handlers.off(names, handler)

class _EventHandlers(object):
    
    def __init__(self):
        self._listeners = {}

    def on(self, names, handler):
        names = parse_notifier_name(names)
        for n in names:
            self._listeners.setdefault(n, []).append(handler)

    def off(self, names, handler):
        names = parse_notifier_name(names)
        for n in names:
            try:
                if handler is None:
                    del self._listeners[n]
                else:
                    self._listeners[n].remove(handler)
            except KeyError:
                pass

    def notify_listeners(self, event, crop_widget):
        event_listeners = self._listeners.get(event['name'], [])
        all_listeners = self._listeners.get(All, [])
        for c in chain(event_listeners, all_listeners):
            c(event, crop_widget)