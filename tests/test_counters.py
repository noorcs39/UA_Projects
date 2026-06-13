import random

from ua_projects.counters import approximate_count, counter_estimate, increment_counter


def test_counter_estimate_at_zero():
    assert counter_estimate(0, 30) == 0


def test_increment_counter_never_negative():
    rng = random.Random(42)
    value = 0
    for _ in range(100):
        value = increment_counter(value, 10, rng)
        assert value >= 0


def test_approximate_count_within_tolerance():
    estimate = approximate_count(1000, 30, seed=7)
    assert abs(estimate - 1000) / 1000 < 0.15
