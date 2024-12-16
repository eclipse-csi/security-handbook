# Securing Development Branches

A critical step in securing development branches involves implementing proactive measures to **detect, analyze and mitigate vulnerabilities in dependencies** before they reach production. 

This section covers best practices and a selection of tools that can support in dealing with potentially insecure dependencies in the development phase of a project.

**Development Stage**
- Dependency Management
    - Use a dependency lock file to ensure consistent dependency versions.
    - Regularly audit and remove unused or unnecessary dependencies.
    - Prefer stable releases over pre-release versions.
- Automated Security Scanning
    - Integrate SCA tools (e.g. Dependabot) into CI/CD pipelines.
    - Enable real-time alerts for vulnerabilities from Github, Gitlab.
    - Scan dependencies on every pull request or branch update.

- Policy Enforcement
    - Block merging with unresolved critical vulnerabilities.

- Continuous Monitor and Updates
    - Regularly update scanning tools and dependency frameworks.

For **project releases**, to mitigate the risk associated with insecure dependencies, we highly recommend implementing Software Bill of Materials (SBOM). More on the topic can be found at [Introduction to SBOM](../sbom/introduction.md). Available tooling and implementation steps can be found at [Tooling Ecosystem for CycloneDX](../sbom/tooling.md).

**Release Stage**
- SBOM and Dependency Visualization
    - Generate SBOMs at least for each new release.
    - Upload SBOMs to Dependency-Track.
    - Monitor and mitigate dependency risks.

## Dependabot
Dependabot is a Github-native tool designed to help developers automatically manage and secure their project dependencies. It reduces the risk associated with vulnerable dependencies, ensuring up-to-date software and allowing teams to focus on development without manual dependency management overhead.

Dependabot can be enabled by going to your **Github repository** -> **Settings** -> **Code Security**. Features can be enabled individually by clicking the associated **Enable** button. For a quickstart tutorial on Dependabot, check out [Enabling Dependabot for your repository](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#enabling-dependabot-for-your-repository).

A summarized version of Dependabot's main features:
- **Security Alerts**
    - Dependabot creates alerts for reported vulnerabilities affecting project dependencies
    - Alert triage can be be performed manually or automated through rules
    - Alerts can be dismissed or fixed
    - Automated resolution options are available through additional Dependabot features 
    - Notification preferences can be customised
- **Security Updates**
    - Dependabot automatically raises Pull Requests to update vulnerable dependencies to a patched version
    - All required information for review is available directly in the PR
    - Alerts are automatically closed upon a merged PR
    - Tests can be set up to ensure compatibility
- **Version Updates**
    - Dependabot automatically raises Pull Requests to update outdated dependencies to newer versions
    - Highly customizable through schedule options and exclusion lists
    - Tests can be set up to ensure compatibility

### Security Alerts
#### Setup
To enable Dependabot alerts, go to **Github repository** -> **Settings** -> **Code Security** and click Enable for **Dependabot alerts**. A pre-requisite is to also have **Dependency graph** enabled.

>**Dependabot alerts**  
>Receive alerts for vulnerabilities that affect your dependencies and manually generate Dependabot pull requests to resolve these vulnerabilities.  

For steps on how to enable Dependabot alerts at different levels, check out [Configuring dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts).

#### Configuration
Low-impact alerts for development dependencies are disabled by default, if you need to enable them, go to **Github repository** -> **Settings** -> **Code Security** -> **Dependabot alerts** -> **Dependabot rules** and toggle **Dismiss low-impact alerts for development-scoped dependencies** to Enabled.

To configure notifications options for security alerts, go to **Your Profile icon** -> **Settings** -> **Notifications** -> **Dependabot alerts: New vulnerabilities** and select notification channel preferences and cadence.

#### Triage
To view the security alerts that have triggered for a repository, go to  **Github repository** -> **Security** -> **Dependabot**. Alerts can be filtered by Package, Ecosystem, Manifest, Severity, Status. 

To triage the alerts, an individual assessment can be performed on the alert content. Most security alerts include the following information: whether Dependabot created a Pull Request to fix it, package involved, affected versions, patched version, brief description of the vulnerabilit. Additionally, CVE data such as: Severity, CVSS score, CWEs (Weaknesses), Github Advisory is included.

#### Resolution
After completing the alert analysis, you can choose to fix or dismiss it.
- To **Dismiss**:
    - Navigate to the alert details page
    - Select a reason for dismissing it from the dropdown
    - Click **Dismiss alert** on the top right corner
- To **Fix**:
    - (Option 1) Manually update the vulnerable dependencies to a patched version
    - (Option 2) Merge the suggested security update by Dependabot 
        - Click **Review security update**
        - A PR generated by Dependabot with the security fix will be created
        - If the PR looks good, merge it.

A quickstart tutorial on Dependabot Security Alerts can be found at [Dependabot Quickstart Guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#prerequisites).

### Security Updates
#### Setup
To enable Dependabot Security Updates, go to **Github repository** -> **Settings** -> **Code Security** and click Enable for **Dependabot security updates**. A pre-requisite is to also have **Dependency graph** and **Dependabot alerts** enabled. 

>**Dependabot security updates**  
>Enabling this option will result in Dependabot automatically attempting to open pull requests to resolve every open Dependabot alert with an available patch. If you would like more specific configuration options, leave this disabled and use [Dependabot auto triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules).

Alternatively, a `dependabot.yml` file can be added in the `.github` directory of the repository to configure Dependabot security alerts.

#### Workflow
Dependabot security updates are automated pull requests that help you update dependencies with known vulnerabilities.

>Dependabot checks whether it's possible to upgrade the vulnerable dependency to a fixed version without disrupting the dependency graph for the repository. Then Dependabot raises a pull request to update the dependency to the minimum version that includes the patch and links the pull request to the Dependabot alert, or reports an error on the alert.

Pull requests should contain everything needed to safely review and merge a proposed fix to a vulnerable dependency in your project. It is however recommended to have integration and acceptance tests in place that run before the PR is merged.

When a security update PR is merged, the corresponding Dependabot alert is automatically marked as resolved for your repository.

#### Environment
For a repository that has GitHub Actions enabled, Dependabot will security updates jobs on GitHub Actions by default. Otherwise, security updates will run on the legacy application in Github.

For performance, visibility and control considerations, it is recommended to enable running Dependabot Security Updates as GitHub Actions jobs. To do so, enable **GitHub Actions** and **Dependabot on Actions runners** from the repository's **Code security and analysis** settings page.

#### Configuration
>To reduce the number of Pull Requests opened by this feature, grouped security updates can be enabled to group sets of dependencies together (per package ecosystem). Dependabot will then create a single PR to update as many vulnerable dependencies as possible in the group to secure versions at the same time. 

To read more about it check out [About grouped security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates#about-grouped-security-updates).

#### Auto-triage rules
>When Dependabot security updates are enabled for a repository, Dependabot will automatically try to open pull requests to resolve every open Dependabot alert that has an available patch. If you prefer to customize which alerts Dependabot opens pull requests for, you should leave Dependabot security updates disabled and create an auto-triage rule.

To learn more about customizing auto-triage rules, check out [Customizing auto-triage rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts).

### Version Updates
#### Setup
To enable Dependabot Version Updates, go to **Github repository** -> **Settings** -> **Code Security** and click Enable for **Dependabot version updates**. This will lead to creating a `dependabot.yml` file in the `.github` directory of the repository. Through `dependabot.yml`, you can define the dependencies to monitor by specifying package managers. Bellow is an example of the default file:
```
version: 2
updates:
  - package-ecosystem: "" # See documentation for possible values
    directory: "/" # Location of package manifests
    schedule:
      interval: "weekly"
```

#### Configuration
Dependabot is highly configurable via the `dependabot.yml` file. It allows defining:
* Update schedules: how often to check for newer versions
* Target dependencies: which dependencies to monitor for updates
* Ignored versions: exclude specific versions or version ranges 

For all configuration options, check out [Configuration options for the dependabot.yml file](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file).

#### Workflow
Dependabot detects outdated dependencies or security issues (see Security Updates above) and creates PRs to update the dependencies to newer versions. If set up, CI tests run on the PR to ensure compatibility. After review, the PR can be merged into the default branch.

## Mend Renovate
Mend Renovate is a powerful tool that supports developers in keeping projects secure and free of vulnerable or outdated dependencies. It seamlessly integrates with source control systems like Github, GitLab, Bitbucket and provides automated updates for dependencies, reducing the manual effort required to manage them. It supports various workflows, including cloud-hosted, self-hosted and CLI-based setups.

#### Supported ecosystems
Renovate supports more than 90 types of package files. Exceptions might exist and are usually due to:
* The package manager/file format is not supported, or
* The file format is not a standard or is proprietary

#### Setup
There are 3 ways in which Mend Renovate can run:
* Mend Renovate App
* Self-administer/host own instance
* Self-administered by third party, configure for own repositories

For more information about self-hosting and available distributions, check out [Self Hosting Renovate](https://docs.renovatebot.com/getting-started/running/#self-hosting-renovate). For how to properly configure your own instance, the official documentation provides [Self-Hosting Examples](https://docs.renovatebot.com/examples/self-hosting/).

#### Workflow
A few usual operations that Renovate performs are:
* Cloning the repository
* Scanning files to extract dependencies
* Checking for available dependency updates
* Applying/grouping defined rules
* Raising pull requests
* Pushing branches

For more details about how Renovate works under the hood, check out [How Renovate Works](https://docs.renovatebot.com/key-concepts/how-renovate-works/).

#### Configuration
The Github Mend Renovate App offers a wide range of configurations options to tailor its behaviour to project specific needs. At its core, configuration is managed through a `renovate.json` file (or altenatives) or directly via the repository settings in the Renovate Dashboard.

Some options might include: schedules updates to avoid disruptions, grouping dependencies by type, customizing PR settings such as branch naming and titles. Advanced features allow exclusions of dependencies, defining update intervals, overriding default behaviour for specific package managers. Additionally, the app can integrate with GitHub's Dependabot alerts.

For more details check out the official documentation at [Configuration options](https://docs.renovatebot.com/configuration-options/).