"""Approximate counting utilities from DDA Assignment 2."""

from __future__ import annotations

import random


def counter_estimate(v: int, accuracy: float) -> float:
    """Return the estimated count for counter state ``v`` and accuracy ``a``."""
    return accuracy * ((1 + 1 / accuracy) ** v - 1)


def increment_counter(v: int, accuracy: float, rng: random.Random | None = None) -> int:
    """Probabilistically increment an approximate counter."""
    rng = rng or random
    delta = 1 / (counter_estimate(v + 1, accuracy) - counter_estimate(v, accuracy))
    return v + 1 if rng.random() <= delta else v


def approximate_count(n_items: int, accuracy: float, seed: int | None = None) -> float:
    """Simulate approximate counting for ``n_items`` increments."""
    rng = random.Random(seed)
    state = 0
    for _ in range(n_items):
        state = increment_counter(state, accuracy, rng)
    return counter_estimate(state, accuracy)
