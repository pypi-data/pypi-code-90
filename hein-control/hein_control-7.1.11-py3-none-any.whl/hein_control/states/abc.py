"""
Module for generic states and state ABCs.

Custom states may be defined for etiher Operational or Action states, but should follow the convention for full
functionality.

# Operational states:

- an offline or unavailable state should be indicated by 0
- operational states should be indicated by values 1 or greater
- inoperable or error states should be indicated by values -1 or less

# Action states

- use 0 to represent an inactive state
- use values 1 or greater to indicate active states


# Custom states

Custom states are supported where a enumeration value is an instance of a State subclass. This adds support for
callbacks when a state is switched to.
"""

import logging
import warnings
from enum import Enum
from typing import Callable, Union, List


state_logger = logging.getLogger('hein_control.states')


class State:
    def __init__(self,
                 value: int,
                 *callbacks: Callable,
                 alias: str = None,
                 ):
        """
        Custom state definition with additional support. An integer value must be specified, and callbacks are supported.
        If callbacks are specified for a state, these callbacks will be automatically executed when the state is set.

        :param value: state value
        :param callbacks: callback functions. These functions should take no arguments.
        :param alias: name alias for convenience
        """
        self.value = value
        self.alias = alias
        self.pre_state_callbacks = list(callbacks)
        self.post_state_callbacks = []

    def __str__(self):
        return f'{self.value} ({len(self.pre_state_callbacks) + len(self.post_state_callbacks)} callbacks)'

    def __eq__(self, other: Union[int, 'State']):
        if isinstance(other, State):
            return other.value == self.value
        return other == self.value

    def __lt__(self, other: Union[int, 'State']):
        if isinstance(other, State):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other: Union[int, 'State']):
        if isinstance(other, State):
            return self.value > other.value
        return self.value > other

    def __le__(self, other: Union[int, 'State']):
        return self < other or self == other

    def __ge__(self, other: Union[int, 'State']):
        return self > other or self == other

    @property
    def has_pre_state_change_callbacks(self) -> bool:
        """whether the State has defined pre-state-change callbacks"""
        return len(self.pre_state_callbacks) > 0

    @property
    def has_post_state_change_callbacks(self) -> bool:
        """whether the State has defined post-state-change callbacks"""
        return len(self.post_state_callbacks) > 0

    @property
    def has_callbacks(self) -> bool:
        """whether the State instance has registered callbacks"""
        return self.has_pre_state_change_callbacks or self.has_post_state_change_callbacks

    def register_pre_state_callbacks(self, *callbacks: Callable):
        """
        Registers the provided callbacks with the State instance. These callbacks will be executed before a Component
        state manager switches to this state.

        :param callbacks: callbacks to register
        """
        return self.register_callbacks(*callbacks, pre_state=True)

    def register_post_state_callbacks(self, *callbacks):
        """
        Registers the provided callbacks with the State instance. These callbacks will be executed after a Component
        state manager switches to this state.

        :param callbacks: callbacks to register
        """
        return self.register_callbacks(*callbacks, pre_state=False)

    def register_callbacks(self, *callbacks: Callable, pre_state: bool = True):
        """
        Registers the provided callbacks with the State instance. These callbacks will be executed when a Component
        state manager switches to this state.

        :param callbacks: callbacks to register
        :param pre_state: whether the callbacks should be pre or post state transition
        """
        callback_list = self.pre_state_callbacks if pre_state is True else self.post_state_callbacks
        for callback in callbacks:
            if callable(callback) is False:
                raise TypeError(f'the provided callback is not callable: {callback}')
            if callback not in callback_list:
                state_logger.debug(f'registering {"pre" if pre_state else "post"}-state change {callback} to {self}')
                callback_list.append(callback)

    def deregister_callbacks(self, *callbacks: Callable):
        """
        De-registers callbacks from the State. If a callback is not registered with the instance that callbck will be
        ignored.

        :param callbacks: callbacks to remove from the instance
        """
        # todo catch the event that the same callback is registered both before and after the event
        for callback in callbacks:
            if callback in self.pre_state_callbacks:
                state_logger.debug(f'removing {callback} from {self} pre-state-change callbacks')
                self.pre_state_callbacks.remove(callback)
            elif callback in self.post_state_callbacks:
                state_logger.debug(f'removing {callback} from {self} post-state-change callbacks')
                self.post_state_callbacks.remove(callback)

    def execute_callbacks(self) -> List:
        """executes any registered callbacks and returns their return values in order"""
        warnings.warn(  # v7.1.9
            'the method has been deprecated, call execute_pre_state_callbacks or execute_post_state_callbacks directly',
            DeprecationWarning,
            stacklevel=2,
        )
        return self.execute_pre_state_callbacks()

    def execute_pre_state_callbacks(self) -> List:
        """executes any registered pre-state-change callbacks and returns their values in order"""
        out = []
        for callback in self.pre_state_callbacks:
            out.append(callback())
        return out

    def execute_post_state_callbacks(self) -> List:
        """executes any registered post-state-change callbacks and returns their values in order"""
        out = []
        for callback in self.post_state_callbacks:
            out.append(callback())
        return out


class StateSet(Enum):
    """A pseudo-IntEnum abstract base class which also supports State instances as values"""

    @classmethod
    def _missing_(cls, value):
        """missing hook for the Enum class which supports the State class"""
        for name, state in cls._member_map_.items():
            # match value to state value
            if value == state.value:
                return state
        raise ValueError(f'{value} is not a valid {cls.__name__}')

    def __lt__(self, other: Union[int, 'StateSet']):
        if isinstance(other, StateSet):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other: Union[int, 'StateSet']):
        if isinstance(other, StateSet):
            return self.value > other.value
        return self.value > other

    def __eq__(self, other: Union[int, 'StateSet']):
        if isinstance(other, StateSet):
            return self.value == other.value
        return self.value == other

    def __le__(self, other: Union[int, 'StateSet']):
        return self < other or self == other

    def __ge__(self, other: Union[int, 'StateSet']):
        return self > other or self == other

    @property
    def has_pre_state_change_callbacks(self) -> bool:
        """whether the value has defined pre-state-change callbacks"""
        if isinstance(self.value, State):
            return self.value.has_pre_state_change_callbacks
        return False

    @property
    def has_post_state_change_callbacks(self) -> bool:
        """whether the value has defined post-state-change callbacks"""
        if isinstance(self.value, State):
            return self.value.has_post_state_change_callbacks
        return False

    @property
    def has_callbacks(self) -> bool:
        """whether the value has callbacks registered"""
        return self.has_post_state_change_callbacks or self.has_pre_state_change_callbacks

    def get_name(self) -> str:
        """retrieves the name or alias of the state"""
        if isinstance(self.value, State):
            return self.value.alias or self._name_
        return self.name

    def set_alias(self, alias: str = None):
        """sets the alias for the StateSet instance"""
        if isinstance(self.value, State) is False:
            raise TypeError(f'the {self.__class__.__name__} value is not a State instance')
        self.value.alias = alias

    def register_callbacks(self, *callbacks: Callable, pre_state: bool = True):
        """
        Pass through for registering callbacks with the associated State instance. These callbacks will be executed
        when a Component state manager switches to this state.

        :param callbacks: callbacks to register
        :param pre_state: whether the callbacks should be before or after the state change
        """
        if isinstance(self.value, State) is False:
            raise TypeError(f'the {self.__class__.__name__} value is not a State instance')
        self.value.register_callbacks(*callbacks, pre_state=pre_state)

    def register_pre_state_callbacks(self, *callbacks):
        """
        Pass through for registering callbacks with the associated State instance. These callbacks will be executed
        before a Component state manager switches to this state.

        :param callbacks: callbacks to register
        """
        return self.register_callbacks(*callbacks, pre_state=True)

    def register_post_state_callbacks(self, *callbacks):
        """
        Pass through for registering callbacks with the associated State instance. These callbacks will be executed
        after a Component state manager switches to this state.

        :param callbacks: callbacks to register
        """
        return self.register_callbacks(*callbacks, pre_state=False)

    def deregister_callbacks(self, *callbacks: Callable):
        """
        Pass through for de-registering callbacks with the associated State instance.

        :param callbacks: callbacks to remove from the instance
        """
        if isinstance(self.value, State) is False:
            raise TypeError(f'the {self.__class__.__name__} value is not a State instance')
        self.value.deregister_callbacks(*callbacks)

    def execute_callbacks(self) -> List:
        """
        executes any registered callbacks and returns their return values in order. If the value is not a State
        instance, no action will be taken
        """
        warnings.warn(  # v7.1.9
            'call execute_pre_state_callbacks or execute_post_state_callbacks directly',
            DeprecationWarning,
            stacklevel=2,
        )
        return self.execute_pre_state_callbacks()

    def execute_pre_state_callbacks(self) -> List:
        """
        executes any registered pre-state-change callbacks and returns their return values in order. If the value is
        not a State instance, no action will be taken
        """
        if isinstance(self.value, State):
            return self.value.execute_pre_state_callbacks()
        return []

    def execute_post_state_callbacks(self) -> List:
        """
        executes any registered post-state-change callbacks and returns their return values in order. If the value is
        not a State instance, no action will be taken
        """
        if isinstance(self.value, State):
            return self.value.execute_post_state_callbacks()
        return []


class OperationalState(StateSet):
    """
    operational state tracker for components. By convention, use 0 to indicate offline, negative values for
    error states, and positive values for online states
    """
    ERROR = State(-1)
    OFFLINE = State(0)
    ONLINE = State(1)


class GenericActionState(StateSet):
    """
    Basic action state tracker for component. By convention, use 0 to represent an inactive state for the inactive
    state check decorator to function.
    """
    IDLE = State(0)
    ACTIVE = State(1)



