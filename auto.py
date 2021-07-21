
import types

# https://stackoverflow.com/a/10967617/4295424
# https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access

class auto:

    def __init__(self,state):
        if not isinstance(state,types.ModuleType):
            print('FAIL did not pass in module: '+str(state))

        # https://stackoverflow.com/a/21885920/4295424
        for name, val in state.__dict__.items():        # iterate through every module's attributes
            if callable(val):                           # check if callable (normally functions)
                print('found in state: '+val.__name__)

    def __getattr__(self, name):
        print('get '+name)
        return ''
        # try:
        #     return self.__dict[name]
        # except KeyError:
        #     msg = "'{0}' object has no attribute '{1}'"
        #     raise AttributeError(msg.format(type(self).__name__, name))