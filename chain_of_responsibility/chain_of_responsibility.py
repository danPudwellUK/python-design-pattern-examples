from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            self._next_handler.handle(request)

        return None


class GrandmaHandler(AbstractHandler):
    def handle(self, request):
        if request == "Turkey":
            print(f"Grandma will have the turkey")
        else:
            super().handle(request)


class MomHandler(AbstractHandler):
    def handle(self, request):
        if request == "Carrots":
            print(f"Mom will have the carrots")
        else:
            super().handle(request)


class DadHandler(AbstractHandler):
    def handle(self, request):
        if request == "Stuffing":
            print(f"Dad will have the stuffing")
        else:
            super().handle(request)


grandma = GrandmaHandler()
mom = MomHandler()
dad = DadHandler()

grandma.set_next(mom).set_next(dad)

# The client should be able to send a request to any handler, not just the
# first one in the chain.
print("Chain: Grandma > Mom > Dad")
grandma.handle("Stuffing")
grandma.handle("Turkey")
