from typing import Union, Dict, List


def clear_none_values(d: Union[List, Dict]):
    if d is None:
        return None
    elif isinstance(d, list):
        return list(filter(lambda x: x is not None, map(clear_none_values, d)))
    elif not isinstance(d, dict):
        return d
    else:
        r = dict(
            filter(lambda x: x[1] is not None,
                   map(lambda x: (x[0], clear_none_values(x[1])),
                       d.items())))
        if not bool(r):
            return None
        return r
