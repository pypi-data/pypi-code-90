# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GroupTree(Component):
    """A GroupTree component.


Keyword arguments:

- id (string; required)

- data (list of dicts; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data']
        self._type = 'GroupTree'
        self._namespace = 'webviz_subsurface_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GroupTree, self).__init__(**args)
