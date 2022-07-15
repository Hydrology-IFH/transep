import pytest
from transep import transep
import numpy as np


@pytest.fixture
def input():
    arr = np.zeros((3,))
    arr[0] = 30
    return arr


def test_dm(input):
    output = transep.simulate(input, transep.dispersion_function, 1, p_d=0.1, mtt=10)
    assert output == pytest.approx(0.1797795615308425, rel=1e-4)


def test_epm(input):
    output = transep.simulate(input, transep.exponential_piston_function, 1, mtt=100, eta=0.1)
    assert output == pytest.approx(0.1797795615308425, rel=1e-4)


def test_gm(input):
    output = transep.simulate(input, transep.gamma_function, 1, alpha=1, beta=1)
    assert output == pytest.approx(0.1797795615308425, rel=1e-4)


def test_lrm(input):
    output = transep.simulate(input, transep.linear_reservoir_function, 1, mtt=40)
    assert output == pytest.approx(0.1797795615308425, rel=1e-4)


def test_plrm(input):
    output = transep.simulate(input, transep.parallel_linear_reservoir_function, 1, mtt_slow=60, mtt_fast=10, frac_fast=0.1)
    assert output == pytest.approx(0.1797795615308425, rel=1e-4)
