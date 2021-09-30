import datetime
import logging
from contextlib import contextmanager
from functools import wraps
from logging import Logger
from time import perf_counter
from typing import Any, Callable

import dateparser
import ujson as json

metrics_logger: Logger = logging.getLogger("METRICS")


def timeit(f: Callable[..., Any]) -> Any:
    @wraps(f)
    def w(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        rtn = f(*args, **kwargs)
        fin = perf_counter() - start
        metrics_logger.info(json.dumps({"fn": f"{f.__module__}:{f.__name__}", "time": f"{fin:.8f}"}))
        return rtn

    return w


def atimeit(f: Callable[..., Any]) -> Any:
    @wraps(f)
    async def w(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        rtn = await f(*args, **kwargs)
        fin = perf_counter() - start
        metrics_logger.info(json.dumps({"fn": f"{f.__module__}:{f.__name__}", "time": f"{fin:.8f}"}))
        return rtn

    return w


@contextmanager
def timed(name: str) -> Any:
    start = perf_counter()
    try:
        yield
    finally:
        fin = perf_counter() - start
        metrics_logger.info(json.dumps({"name": f"{name}", "time": f"{fin:.8f}"}))


def delta_in_seconds(time_string: str) -> int:
    """
    Convert a relative time string to seconds

    >> delta_in_seconds("30m")
    1800
    """
    return round((datetime.datetime.now() - (dateparser.parse(time_string))).total_seconds())  # type: ignore
