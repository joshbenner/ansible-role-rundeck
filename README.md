# joshbenner.rundeck

Install and configure Rundeck.

Right now this role only targets Ubuntu 16.04.

## Role Features

* Installs OpenJDK (optional).
* Pins the Rundeck apt package version if set (optional).
* Allows for injection of arbitrary Rundeck configuration.
* Controls execution mode (default: active).
* Configures Rundeck CLI (optional).
* Sets Rundeck global variables.
* Configures Java VM parameters.
* Configures SSL keystore (just provide the cert/key).
* Configures TLS truststore (just provide certs to trust).
* Configures LDAP integration (optional).
* Deploys a custom SSH key (optional).
* Installs Rundeck plugins (optional).
* Configures Rundeck on-disk ACLs.
* Can configure a cleanup script to remove old job logs (optional; default off).

## Notes

* OpenJDK JRE 8 headless is installed, but this can be disabled by setting `rundeck_install_java` to `false`.
* Installs python package `lxml` if `rundeck_set_session_timeout` is `true` (default).
* Installs `openssl` if SSL or trusted cert handling is used.

## Role Variables

See `defaults/main.yml`.

## Example Playbook

```yaml
---
- name: Install Rundeck
  hosts: rundeck_servers
  roles:
    - role: joshbenner.rundeck
```

License
-------

BSD
