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
    assert 'localhost' in out
    assert 'rundeck' in out


def test_ssh_key(host):
    assert host.file('/var/lib/rundeck/.ssh/id_rsa').exists


def test_static_token_exists(host):
    token_file = host.file('/etc/rundeck/tokens.properties')
    assert token_file.exists
    assert 'test-api: sekrit' in token_file.content


def test_structured_acl(host):
    my_policy = host.file('/etc/rundeck/my_policy.aclpolicy')
    assert my_policy.exists
    assert 'group: somegroup' in my_policy.content


def test_acl_perms(host):
    acl = host.file('/etc/rundeck/my_policy.aclpolicy')
    assert acl.user == 'rundeck'
    assert acl.group == 'rundeck'
    assert acl.mode == 0o640


def test_raw_acl(host):
    raw_acl = host.file('/etc/rundeck/test-api.aclpolicy')
    assert raw_acl.exists
    assert 'username: test-api' in raw_acl.content
