"""
Tests for eink_refresh.py. Values independently verified with a
reference implementation before being written here.
"""
import pytest

from eink_refresh import (
    apply_partial_refresh,
    apply_full_refresh,
    ghost_score,
    partial_refreshes_to_converge,
)


def test_apply_partial_refresh_moves_toward_target():
    assert apply_partial_refresh([0, 0, 1], [1, 1, 1], gain=0.65) == pytest.approx([0.65, 0.65, 1.0])


def test_apply_partial_refresh_default_gain():
    result = apply_partial_refresh([0.0], [1.0])
    assert result == pytest.approx([0.65])


def test_apply_full_refresh_snaps_exactly():
    assert apply_full_refresh([1, 0, 1]) == [1, 0, 1]


def test_ghost_score_no_difference():
    assert ghost_score([1, 0, 1], [1, 0, 1]) == 0


def test_ghost_score_partial_difference():
    assert ghost_score([0.35, 0.35, 1], [1, 1, 1]) == pytest.approx(43.333333333333336)


def test_partial_refreshes_to_converge_typical():
    assert partial_refreshes_to_converge(1.0, 0.65, 0.05) == 3


def test_partial_refreshes_to_converge_slower_gain():
    assert partial_refreshes_to_converge(1.0, 0.5, 0.01) == 7


def test_partial_refreshes_to_converge_already_below_threshold():
    assert partial_refreshes_to_converge(0.01, 0.65, 0.05) == 0
