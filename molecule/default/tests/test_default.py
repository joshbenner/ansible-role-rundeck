import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rundeck_package(host):
    package = host.package('rundeck')
    assert package.is_installed
    assert package.version == '2.11.5'


def test_rundeck_service(host):
    service = host.service('rundeckd')
    assert service.is_running
    assert service.is_enabled


def test_trusted_cert(host):
    out = host.check_output('keytool -list '
                            '-keystore /etc/rundeck/ssl/truststore '
                            '-storepass adminadmin')
    assert 'snakeoil' in out
    assert 'rundeck' in out


def test_ssh_key(host):
    assert host.file('/var/lib/rundeck/.ssh/id_rsa').exists
