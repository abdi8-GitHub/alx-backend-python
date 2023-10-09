#!/usr/bin/env python3
'''
Module: '2-measure_runtime'
Measures total run time
'''

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Returns the total runtime of the wait_n function'''
    start_time = time()
    asyncio.run(wait_n(n, max_delay))

    return (time() - start_time) / n
