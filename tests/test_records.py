import copy
import pytest
from pathlib import Path

from src.records import Records


@pytest.fixture
def lines():

    run = Path(__file__).parent / 'data' / 'recs.txt'
    with open(run, 'r') as f:
        rr = []
        while True:
            r = f.readline()
            if r == '' or r[0] == '\n':
                break
            rr.append(r)
    return rr


@pytest.fixture
def fill(lines):

    rs = Records()
    for a in lines:
        rs.add(a)

    yield rs


def test_readin(lines):

    rs = Records()
    ll = lines
    rs.add(ll[1])
    rs.add(ll[3])

    for a, b in zip(rs.inds, [15000, 17000]):
        assert a == b
    for a, b in zip(rs.time, [2.208320e+01, 2.516416e+01]):
        assert a == b
    for a, b in zip(rs.tau, [1.175051e-03, 8.124064e-04]):
        assert a == b
    for a, b in zip(rs.rt['code'], [0, 1]):
        assert a == b
    for a, b in zip(rs.rt['str'], ['fission', 'fusion']):
        assert a == b
    for a, b in zip(rs.n[0]['val'], [57, 47]):
        assert a == b
    for a, b in zip(rs.n[1]['val'], [128, 130]):
        assert a == b
    for a, b in zip(rs.n[2]['val'], [29, 31]):
        assert a == b
    for a, b in zip(rs.m['11'], [7, 9]):
        assert a == b
    for a, b in zip(rs.m['22'], [0, 0]):
        assert a == b
    for a, b in zip(rs.m['13'], [43, 29]):
        assert a == b
    for a, b in zip(rs.m['33'], [22, 32]):
        assert a == b
    for a, b in zip(rs.mtm, [200, 200]):
        assert a == b
    for a, b in zip(rs.mtn, [72, 70]):
        assert a == b
    for a, b in zip(rs.cln, [15, 11]):
        assert a == b
    for a, b in zip(rs.score['fission']['num'], [7502, 8499]):
        assert a == b
    for a, b in zip(rs.score['fission']['val'], [3.430000e+02, 3.530000e+02]):
        assert a == b
    for a, b in zip(rs.score['fusion11']['num'], [5641, 6394]):
        assert a == b
    for a, b in zip(rs.score['fusion11']['val'], [2.196000e+02, 1.599000e+02]):
        assert a == b
    for a, b in zip(rs.score['fusion12']['num'], [1856, 2106]):
        assert a == b
    for a, b in zip(rs.score['fusion12']['val'], [7.501000e+01, 6.252000e+01]):
        assert a == b
    for a, b in zip(rs.score['fusion1L']['num'], [1, 1]):
        assert a == b
    for a, b in zip(rs.score['fusion1L']['val'], [ 0.000000e+00,  0.000000e+00]):
        assert a == b


def test_len(fill):

    assert len(fill.time) == 5


def test_scale_time_to(fill):

    rs = fill

    td = [t / 3600 / 24 for t in rs.time]
    Records.scale_time_to([rs], 'd')
    for t, e in zip(rs.t, td):
        assert t == e

    th = [t / 3600 for t in rs.time]
    Records.scale_time_to([rs], 'hours')
    for t, e in zip(rs.t, th):
        assert t == e

    ts = copy.copy(rs.time)
    Records.scale_time_to([rs], 's')
    for t, e in zip(rs.t, ts):
        assert t == e
