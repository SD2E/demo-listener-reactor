from __future__ import unicode_literals
import json
import os
import sys

# Import various types we will assert against
from attrdict import AttrDict
# from agavepy.agave import Agave
# from builtins import str
# from logging import Logger

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT)
sys.path.append('/reactors')
sys.path.append('/')
from reactors.utils import Reactor

import pytest
from agavefixtures import credentials, agave
import testdata

# Import the 'reactor.py' file.
# TODO - Move this to individual tests to enable parameterization
import reactor


@pytest.fixture(scope='session')
def test_data():
    return testdata.TestData().data()


@pytest.fixture(scope='session')
def secrets_data():
    return testdata.Secrets().data()


def test_test_data(monkeypatch, test_data):
    '''Ensure test data loads OK'''
    execution = test_data
    assert isinstance(execution, list)
    # executions.json contains an array of dicts with env variables to set
    for k in execution[0].keys():
        monkeypatch.setenv(k, execution[0].get(k, ""))
    assert os.environ.get('_abaco_actor_id', None) == '2d1ed766bf9cc45977c'


def test_reactor_init():
    '''Ensure Reactor object can initialize'''
    r = reactor.Reactor()
    assert isinstance(r, Reactor)


def test_reactor_read_config():
    '''Validate config.yml loads config.yml properly'''
    r = reactor.Reactor()
    assert isinstance(r.settings, AttrDict)
    # it doesn't matter what keys one puts here - the idea is to ensure
    # that the config.yml is valid YAML and thus loadable as a dict
    assert 'logs' in r.settings
    assert r.settings.logs.level is not None


def test_reactor_main(monkeypatch, caplog,
                      test_data, secrets_data):
    '''emulate an execution directly from contents of executions.json'''
    execution = test_data
    for k in execution[0].keys():
        monkeypatch.setenv(k, execution[0].get(k, ""))
    # s/reactor.py/reactor/
    import reactor as r
    r.main()
    assert "Message" in caplog.text
    # This message is also plaintext so won't parse to JSON
    # this is acceptable - we just need to be defensive about handling it
    assert "Error parsing message" in caplog.text


def test_reactor_valid_json(monkeypatch, caplog,
                            test_data, secrets_data):
    '''emulate an execution directly from contents of executions.json'''
    execution = test_data
    for k in execution[1].keys():
        monkeypatch.setenv(k, execution[1].get(k, ""))
    # s/reactor.py/reactor/
    import reactor as r
    r.main()
    # This message is also plaintext so won't parse to JSON
    # this is acceptable - we just need to be defensive about handling it
    assert "Error parsing message" not in caplog.text


def test_reactor_sender_tag(monkeypatch, caplog,
                            test_data, secrets_data):
    '''Catch message that doesn't conform to schema'''
    execution = test_data
    for k in execution[0].keys():
        monkeypatch.setenv(k, execution[0].get(k, ""))
    monkeypatch.setenv('x_src_actor_id', 'abcdefg')
    monkeypatch.setenv('x_src_execution_id', '123456')
    # s/reactor.py/reactor/
    import reactor as r
    r.main()
    # parse log log
    assert "tag x_src_actor_id: abcdefg" in caplog.text
    assert "tag x_src_execution_id: 123456" in caplog.text