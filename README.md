# joshbenner.rundeck

Install and configure Rundeck.

Right now this role only targets Ubuntu 16.04.

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
