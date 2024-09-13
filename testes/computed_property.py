import functools
import inspect

class computed_property:
    def __init__(self, *dependencies):
        self.dependencies = dependencies
        self._getter = None
        self._setter = None
        self._deleter = None
        self.__doc__ = None

    def __call__(self, func):
        self._getter = func
        self.__doc__ = func.__doc__

        @functools.wraps(func)
        def wrapped_getter(instance):
            if not hasattr(instance, '_cache'):
                instance._cache = {}
            if not hasattr(instance, '_dependency_cache'):
                instance._dependency_cache = {}

            dependency_values = tuple(getattr(instance, dep, None) for dep in self.dependencies)

            if self.dependencies not in instance._dependency_cache or instance._dependency_cache[self.dependencies] != dependency_values:
                instance._cache[self._getter.__name__] = func(instance)
                instance._dependency_cache[self.dependencies] = dependency_values
            
            return instance._cache[self._getter.__name__]

        self._getter = wrapped_getter
        return self

    def setter(self, setter):
        self._setter = setter
        return self

    def deleter(self, deleter):
        self._deleter = deleter
        return self

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._getter(instance)

    def __set__(self, instance, value):
        if self._setter is None:
            raise AttributeError("Não é possível setar o valor. Setter não definido.")
        self._setter(instance, value)

    def __delete__(self, instance):
        if self._deleter is None:
            raise AttributeError("Não é possível deletar o valor. Deleter não definido.")
        self._deleter(instance)

