"""

The main parser interface resides here


"""

from lang.guy import AL
from lang.training import clear_data


def parse(raw_data):
    good_data = clear_data(raw_data)
    al = AL().get()
    return [al.respond(d) for d in good_data]

