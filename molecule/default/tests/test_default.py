import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rundeck_package(host):
    package = host.package('rundeck')
    assert package.is_installed
    assert package.version == '2.11.5


def test_rundeck_service(host):
    service = host.service('rundeckd')
    assert service.is_running
    assert service.is_enabled
