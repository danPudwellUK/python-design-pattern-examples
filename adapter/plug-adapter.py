from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "not implemented"

CONNECTED = "{} connected"
POWERING = "{} powering"

class PowerTemplate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def power(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class FormatUK(PowerTemplate):
    __name__ = "UK"

    @abstractmethod
    def use_uk_plug(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class FormatEU(PowerTemplate):
    __name__ = "EU"

    @abstractmethod
    def use_eu_plug(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class UKPlug(FormatUK):
    def use_uk_plug(self):
        print(CONNECTED.format(self.__name__))

    def power(self):
        print(POWERING.format(self.__name__))

class EUPlug(FormatEU):
    def use_eu_plug(self):
        print(CONNECTED.format(self.__name__))

    def power(self):
        print(POWERING.format(self.__name__))


class EUAppliance:
    def __init__(self):
        self.plug = EUPlug()
        self.plug.use_eu_plug()
        self.plug.power()

class UKAppliance:
    def __init__(self):
        self.plug = UKPlug()
        self.plug.use_uk_plug()
        self.plug.power()

class UKAdapter(FormatEU):
    def __init__(self, plug):
        self.plug = plug

    def power(self):
        self.plug.power()

    def use_eu_plug(self):
        print(CONNECTED.format(self.__name__))
        self.plug.use_uk_plug()

class HairDryerinSpain:
    def __init__(self):
        self.plug = UKPlug()
        self.plug_adapter = UKAdapter(self.plug)
        self.plug_adapter.use_eu_plug()
        self.plug_adapter.power()



EUAppliance()
print()

UKAppliance()
print()

HairDryerinSpain()
