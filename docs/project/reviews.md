# Rapid Security Review

A Rapid Security Review is a lightweight security assessment designed to help projects strengthen their overall security posture. It provides an easy to use framework comprising checks from a wide variety of topics, such as: security automation and tooling, secure development practices, incident preparedness, monitoring and visibility, security policies and project setup.

The EF Security Team will be conducting Rapid Security Reviews with the goal of providing guidance and actionable recommendations to help projects strengthen their security posture. Rather than just identifying gaps, we focus on offering clear, practical steps maintainers can take to improve security in meaningful ways. 

We maintain a queue of projects for these reviews, and while we prioritize based on impact and need, we welcome projects that wish to volunteer for a review. If you're interested in having your project assessed, reach out to us and we will do our best to accommodate as many as possible. 

However, if you are eager to get started, we encourage to self-assess using the checklist below.

## Organization section

First section covers project organization level checks, encompassing setup, activity and security team members. Find below a list of these checks, with the one of highest priority marked in bold:

| **CATEGORY**               | **CHECK**                                    |
|----------------------------|----------------------------------------------|
| **Setup**                  | **Has own project GitHub organization**      |
| **Community Health Files** | Has .github repo                             |
|                            | Has .github/SECURITY.md file                 |
| **Otterdog**               | Enabled                                      |
| **Blueprints**             | (global) default-security-policy blueprint   |
|                            | (global) add-dot-github-repo blueprint       |
| **Contributions**          | Commits ~1y                                  |
|                            | Commit Authors ~1y                           |
|                            | Repositories                                 |
|                            | Inactive repositories                        |
|                            | Committers                                   |
|                            | **Inactive committers**                      |
| **Security Team**          | **Members**                                  |
|                            | Last Activity                                |
|                            | Previous Security Audits                     | 

To check `Otterdog: Blueprints` status, find the project in the [Otterdog Dashboard](https://otterdog.eclipse.org/index) and navigate to the `Blueprints` tab.

In terms of `Contributions`, whilst activity does not always directly influence the security posture of a project, it is a good practice to periodically monitor it. Relevant data can be retrieved from Github or from [Eclipse Metrics](https://metrics.eclipse.org/projects/) by looking up individual projects. Inactive committers should be reviewed on a periodic basis.

The `Project Security Team` members list can be viewed through the [PMI](https://projects.eclipse.org/). 

## Repository section

The second section covers repository specific checks, encompassing topics such as: Vulnerability Reporting and Management, SBOM generation, Static Code Analysis, CI/CD Tooling, Release processes.

| **CATEGORY**               | **CHECK**                                      |
|----------------------------|-----------------------------------------------|
| **Vulnerability Reporting** | Private Vulnerability Reporting: Enabled    |
|                            | Open Reports > 6 months                      |
|                            | Total Reports                                |
|                            | Total CVEs                                   |
| **Vulnerability Management** | Dependabot: Security Alerts Enabled        |
|                            | -- Resolution                                |
|                            | -- Triage time                               |
|                            | -- Unresolved Alerts                         |
|                            | -- Vulns in Deps: Severity: Critical         |
|                            | -- Vulns in Deps: Severity: High             |
| **SBOM**                   | Automated SBOM Generation                    |
|                            | Upload to DependencyTrack                    |
|                            | Check dependency tree                        |
| **Static Analysis**        | Linting                                      |
|                            | Secret Scanning                              |
|                            | Secret Exposure Response                     |
|                            | Unit/Integration Tests                       |
|                            | Code Coverage                                |
|                            | License Check                                |
|                            | Copyright Check                              |
|                            | ECA Validation                               |
| **CI/CD: Releases**        | Releases ~1y                                 |
|                            | Hotfix release practice                      |
|                            | Stable release policy                        |
|                            | Publishing destination in README             |
| **CI/CD: Tools**           | CI/CD Tool/Location enabled                  |
|                            | Github/Gitlab workflow: Build                |
|                            | -- zizmor score                              |
|                            | Eclipse hosted Jenkins                       |
|                            | Other                                        |
| **Security Posture**       | Aware of Scorecard report                    |
|                            | OpenSSF Scorecard Otterdog Integration       |
|                            | OpenSSF Scorecard                            |
|                            | -- Branch Protection                         |
|                            | -- Token-Permissions                         |
|                            | -- Security Policy (Project specific)        |
|                            | -- Pinned-Dependencies                       |

While `Vulnerability Reporting` evaluates how the project handles security issues, including the existence of private vulnerability reporting channels, the volume of open reports, and the management of CVEs, `Vulnerability Management` focuses on the project's approach to addressing security risks in its dependencies. This includes the resolution of Dependabot security alerts, the speed of triaging and updating dependencies, and the severity of unresolved issues within the project's supply chain. Together, these categories provide insight into both the project's internal security responsiveness and its proactive stance on dependency security.

The `SBOM` category assesses the project's ability to generate and manage an inventory of its dependencies. This includes automated SBOM generation and integration with our DependencyTrack instance for tracking vulnerabilities and ensuring visibility into the project's dependency tree. 

>If you want to start generating SBOMs for your project, make sure to check out our [How to generate and upload SBOMs](./../sbom/howto.md) guide. There are a lot of other resource available to get your project started, such as [Introduction to SBOM](./../sbom/introduction.md) and [Tooling Ecosystem for CycloneDXM](./../sbom/tooling.md). The EF Security Team is here to support with any SBOM related questions.

The `Static Analysis` category assesses automated tools for linting, secret scanning, unit/integration tests, code coverage, and license/compliance checks. It helps ensure code quality and security by identifying issues early. This category serves as a self-evaluation tool—it's aim is not to provide "good" or "bad" answers, but rather highlight areas where improvements can be made, guiding towards better practices for the project.

The `Releases` category evaluates release periodicity, processes or policies. While we recommend maintaining a regular release schedule, we understand there can be exceptions based on a project's specific needs. This self-evaluation helps projects assess release practices, ensuring that stable policies and clear documentation of publishing destinations are in place, even if releases occur less frequently.

The `CI/CD Tools` category should evaluate the security of tools and workflows used for automating builds and deployments, such as GitHub/GitLab workflows or Jenkins. This self-evaluation does not dictate a specific solution—it highlights the importance of keeping an inventory of such tools as well as evaluating if security best practices are followed. We also encourage using scoring tools specific to your CI/CD tools of choice (example [Zizmor](https://github.com/woodruffw/zizmor) for Github Actions workflows) to evaluate and enhance projects' pipeline security.

The use of automated scoring tools can help in painting the picture of the overall security posture of a project. Such a tool is `OpenSSF Scorecard`, which provides an assessment of areas such as branch protection, token permissions and security policy. For more details on how to use the tool, visit the [OpenSSF Scorecard page](https://github.com/ossf/scorecard). To read more about what each check means and how the score is computed, review the [Check Documentation](https://github.com/ossf/scorecard/blob/main/docs/checks.md). To integrate Scorecard with the self-service, check out [Otterdog Scorecard Integration](https://otterdog.readthedocs.io/en/latest/reference/blueprints/scorecard-integration/).
