import collections
from typing import Deque, Iterable, TypeVar

T = TypeVar("T")


def delayed_iter(iterable: Iterable[T], delay: int) -> Iterable[T]:
    """Waits to yield the i'th element until after the (i+n)'th element has been
    materialized by the source iterator.
    """

    cache: Deque[T] = collections.deque([], maxlen=delay)

    for item in iterable:
        if len(cache) >= delay:
            yield cache.popleft()
        cache.append(item)

    while len(cache):
        yield cache.popleft()
