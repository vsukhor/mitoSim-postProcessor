import pytest
from pathlib import Path

from src.config import Config


@pytest.fixture
def config55():
    run55 = Path(__file__).parent / 'data' / 'log_conf_55.txt'
    cf = Config()
    with open(run55, 'r') as f:
        cf.readin(f)
        yield cf


@pytest.fixture
def config56():
    run56 = Path(__file__).parent / 'data' / 'log_conf_56.txt'
    cf = Config()
    with open(run56, 'r') as f:
        cf.readin(f)
        yield cf


def test_readin(config55):

    cf = config55
    assert cf.working_dir_out == '"/Users/a/runs"'
    assert cf.run_start == 55
    assert cf.run_end == 56
    assert cf.time_total == 500
    assert cf.logfreq == 1000
    assert cf.savefreq == 50000
    assert cf.edge_length == 0.2
    assert cf.mtmassini == 200
    assert cf.segmassini == 20
    assert cf.use_fission == 1
    assert cf.rate_fission == 1.
    assert cf.use_11_fusion == 1
    assert cf.fusion_rate_11 == 0.1
    assert cf.use_12_fusion == 1
    assert cf.fusion_rate_12 == 0.01
    assert cf.use_1c_fusion == 1
    assert cf.fusion_rate_1c == 0.01


def test_eq(config55, config56):

    assert config55 == config55
    assert config55 != config56
