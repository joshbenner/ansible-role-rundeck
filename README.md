# joshbenner.rundeck

Install and configure Rundeck.

## Requirements

* java on target host

## Notes

* Installs python package `lxml` on target host if `rundeck_set_session_timeout` is `true` (default)

## Role Variables

See `defaults/main.yml`.

## Example Playbook

```yaml
---
- name: Install Rundeck
  hosts: rundeck_servers
  roles:
    - role: geerlingguy.java
      java_packages:
        - openjdk-8-jre-headless
    - role: joshbenner.rundeck
```

License
-------

BSD
