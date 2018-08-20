import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# Test dir structure

def test_config_dir(host):
    f = host.file('/srv/gitlab/config')
    assert f.is_directory


def test_data_dir(host):
    f = host.file('/srv/gitlab/data')
    assert f.is_directory


def test_logs_dir(host):
    f = host.file('/srv/gitlab/logs')
    assert f.is_directory
