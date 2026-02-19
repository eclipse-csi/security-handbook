# How to opt in for vulnerability alerts

Once SBOMs are uploaded to the SBOM Registry, projects gain immediate visibility into their security posture through automated vulnerability tracking. However, to proactively manage security risks, projects should configure automated alerts that provide real-time notifications when new vulnerabilities are discovered in their dependencies. 

Alerts enable project committers to respond quickly to emerging threats by notifying designated channels, whenever vulnerabilities are identified. By setting up automated alerting, projects can shift from reactive to proactive vulnerability management, ensuring that security issues are addressed promptly before they impact end users.

Our SBOM Registry alerting capabilities leverage the [Dependency-Track notification system](https://docs.dependencytrack.org/integrations/notifications/), providing projects with access to a predetermined range of features and customization options. 

To opt in for vulnerability alerts, open a [HelpDesk](https://gitlab.eclipse.org/eclipsefdn/helpdesk/-/issues/?sort=created_date&state=opened&first_page_size=100) with the following:
- title: `[PROJECT NAME]: Setup Dependency-Track notifications`
- labels: `service:dependencytrack` and `team:security`
- selected alert types 
- selected publishers

## Publishers

We currently support the following notifications delivery mechanisms:
- **Email**
- **Slack**
- **Teams**

For email alerts, the default destination is the **project security mailing list**. All committers part of a projects Security team are automatically subscribed to this mailing list and will receive notifications. Custom destination can be set up on explicit request.

For Slack and Teams, the destination should be an incoming webhook URL for a channel. This must be provided through a secure private channel to the Eclipse Foundation Security Team (see [sharing secrets](https://gitlab.eclipse.org/eclipsefdn/helpdesk/-/wikis/Sharing-secrets)).

## Alert types

- **NEW_VULNERABILITY**

This is an event notification that generates an alert whenever a newly published vulnerability affects any component within a project. Notifications apply to all released versions of a project, not only the latest version.

At present, vulnerability notifications cannot be filtered by severity (see the [related feature request](https://github.com/DependencyTrack/dependency-track/issues/3767
)). As a result, vulnerabilities of all severity levels will create alerts.

- **NEW_VULNERABILITIES_SUMMARY**

This is a scheduled notification that generates an alert at a defined cadence (by default, once per week). It provides a summary of newly published vulnerabilities affecting components across all released versions of the project.

Each alert includes only vulnerabilities that were not reported in the previous summary. If no new vulnerabilities are identified since the last notification, no alert is generated.

## FAQ

- **Can I automatically opt-in for alerts on SBOM upload?**

Notification settings are managed within the administration interface. As a result, project-level access cannot be granted to automatically opt in for notifications. 

We are currently developing a mechanism that will allow automatic alert opt-in through upload integrations, which will eventually replace the need for manual requests.

- **Can I opt-in for other types of alerts?**

While the alerts listed above are the most commonly required for projects, additional alert types can be considered upon request with appropriate justification. 

Please note that available options are limited to those supported by Dependency-Track.