from facade import Facade
from important_stuff import ImportantStuff
from more_important_stuff import MoreImportantStuff

facade_runner = Facade()
facade_runner.doStuff()

# can also give facade created objects
important_stuff = ImportantStuff()
more_important_stuff = MoreImportantStuff()
facade_runner_2 = Facade(important_stuff, more_important_stuff)
facade_runner_2.doStuff()
