# Securing the Development Environment

## Development Tools

* Opt for reputable IDEs and ensure the security of cloud-based IDEs through regular updates to the infrastructure and vulnerability assessments.
* Verify the source of plugins prior to installation, and conduct regular audits of installed plugins for their utility and updates.
* Routinely audit for unused plugins and uninstall them.

## Secret Management

* Secrets should not be stored in readable or easily accessible files. Local secret scanning tools should be used to identify and secure secrets stored in shell profiles and other configuration files.
* Regularly scan for secrets in shell history.
