"""
Single create time: 0.23 sec
Bulk create time: 0.11 sec
"""

import time

from cryptoarchive.exchanges.models import Exchange

# Number of objects to insert
NUM_OBJECTS = 1000

# Prepare test data
data = [Exchange(lp="value", type=123) for _ in range(NUM_OBJECTS)]


# 1. Benchmark single instance create
def benchmark_single_create():
    Exchange.objects.all().delete()  # Clean up
    start_time = time.time()

    for obj in data:
        obj.save()

    end_time = time.time()
    print(f"Single create time: {end_time - start_time:.2f} sec")  # noqa: T201


# 2. Benchmark bulk_create
def benchmark_bulk_create():
    Exchange.objects.all().delete()  # Clean up
    start_time = time.time()

    Exchange.objects.bulk_create(data)

    end_time = time.time()
    print(f"Bulk create time: {end_time - start_time:.2f} sec")  # noqa: T201


# Run benchmarks
benchmark_single_create()
benchmark_bulk_create()
