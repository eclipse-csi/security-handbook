# Security Advisories

Security advisories allow projects to communicate security information to users. They contain a description of a vulnerability (or a class of vulnerabilities) and solutions to follow. They usually contain information on which versions of the product are affected and which ones contain a fix; they mention possible workarounds if available.

This document presents recommendations on handling advisories by Eclipse Foundation projects. In general, projects should adhere to the [Eclipse Foundation Vulnerability Reporting Policy](https://www.eclipse.org/security/policy/); this document provides additional guidelines and best practices. Each project might decide to act differently if the situation, and security of their users, requires this.

Readers of this document should be familiar with terms and definitions of the [Eclipse Foundation Development Process](https://www.eclipse.org/projects/dev_process) and the [Eclipse Foundation Vulnerability Reporting Process](https://www.eclipse.org/security/policy/). Please review them if needed.

## What is the difference between a CVE entry and a security advisory?

Security advisories extend and organize vulnerability descriptions like CVEs (Common Vulnerability Enumeration). CVEs have strict format and concentrate on the vulnerabilities discovered: their cause, severity, exploitation possibilities. They are designed to help security researchers to talk about issues precisely. A CVE describes a single vulnerability only.

On the other hand, security advisories are more user-oriented, and more detailed. They might include a detailed discussion about situations or configurations that are vulnerable, and offer a list of possible workarounds. An advisory might also provide a detailed description of the related vulnerability (or vulnerabilities) and describe a series of related vulnerabilities (example: the same vulnerable code pattern) in different modules of the same project or related projects.

Both CVE entries and advisories can be released in a machine-readable format.

## Process

Security advisories are generally released when a fix and release with the fix is available (for other use-cases see later in this document).  When managing individual vulnerabilities projects should follow the Vulnerability management process from the [Eclipse Foundation Project Handbook](https://www.eclipse.org/projects/handbook/#vulnerability).

Projects should consider releasing a security advisory in addition to a CVE entry in the following situations:

* Multiple high- or medium-impact security issues are fixed in one release, and the project wants to urge all users to upgrade.
* Multiple security issues of the same type are fixed in the same release. For example multiple buffer overflows or cross-scripting issues.
* A high impact security vulnerability that requires more explanation to users than what is present is a CVE entry.
* A security-focused release with multiple issues fixed is available and the project wants to explain the work at high level to its users.
* A cross-project issue, including a similar issue fixed in multiple projects, or an issue in a commonly used dependency.
* Addressing a new important security best practice (for example recommended use of a specific configuration option).
* Addressing an issue found in a number of projects to state the Project’s status (example: stating that the Project is not affected by a given CVE and providing reasons for this statement).
* Addressing an unfixed issue in a version that is no longer supported, urging users to perform the update.
* Addressing a yet-unfixed issue that is being exploited in practice, with suggestions on workarounds and mitigations.

A security advisory is typically released at the time of a release (of a fixed version, the CVE publication, embargo end) or shortly thereafter. It references resolved issues, with rare exceptions for deprecated versions.

## Pre-advisories and advisories without fixes

As a general rule, security advisories should be released when a release with the fix is available. There are some specific cases, however, when projects might decide to release an advisory without an available release.

### Pre-advisories

For some issue projects might want to release pre-advisories, messages stating that there is a pending release with important security fixes. Such a pre-advisory should give the exact date of the release. Pre-advisories help system administrators to plan maintenance and incite them to install updates.

On the other hand, if a fix is already available in the version control system, attackers can usually figure out which commit brings the fix and could develop and deploy exploitation before the official release.

Because of the risk of exploitation, pre-advisories should have a short time frame (eg. pre-advisory on Wednesday with a bug-fix release the following Tuesday) and do not give any details on the fixed vulnerability. In addition, when a project decides to make a pre-advisory, they should push or merge fixes to public repositories as close to the release date as possible and after extensive testing to avoid regressions.

An example pre-advisory text could be like follows:

    To: Project C users
    Title: Important security release on <date>

    Dear project C users,
    The Project C will be releasing an important security release on <date>.
    There will be backports to <version> and <version>. All users should upgrade.

    Sincerely,
    Project team

### Deprecated versions

Projects might want to release an advisory when an issue is found in a deprecated version of the project that will not receive a fix. In this case, users should be urged to upgrade.

### Emergency statement

In some rare cases, projects might need to release an emergency statement. Possible cases include: an important exploitation in progress (and no fix yet), an industry-wide issue (in a network protocol, hardware etc), or an important issue that has been published before being fixed. In this case the project should give any known workarounds and the timeline of the expected fix.

## Reference content

The Eclipse Foundation security team recommends that the advisory should include:

- An informative title.
- A description of the issue.
- A description of possible workarounds, if applicable.
- The severity and impact of the issue.
- A list of affected products (projects) along with the version numbers affected. If a project maintains multiple branches, each should be listed separately, specifying the exact version containing a solution or clearly indicating if a particular version is deprecated.
- The list of related CVEs, if any.
- Contact information for inquiries or questions.
- The name of the issuing authority (e.g., Eclipse Foundation, the project itself, etc.).
- A list of changes to the advisory, if applicable, in reverse chronological order.

## Technical means

To support advisories in Eclipse Foundation projects, the following resources are necessary:

- An announcement mailing list (the Eclipse Foundation provides a security-announcements@ mailing list, open for everyone to subscribe. Projects may opt to create their own announcement mailing list or use their usual communication channels directed towards their users).
- A central Eclipse Foundation website that lists all advisories in text format and machine readable standard format (when available), similar to the CVE listing at https://www.eclipse.org/security/known/.

Additionally, projects may choose to publish their advisories on their own website, typically on the 'Security' page.

## Standard formats

Eclipse Foundation projects may decide to generate their advisories in a machine-readable format like the CSAF advisory format.

## Frequently asked question

- Should we release advisories at regular intervals (monthly, weekly)?

If you have enough information to do so. Monthly or weekly advisories are often used by big projects or Linux distributions performing regular bugfix releases. In most cases, for projects hosted under the Eclipse Foundation, an advisory linked to each (especially bugfix) release is a good target.

- Can I use GitHub advisories?

Yes. However, please note that GitHub advisories work best for one single CVE number. If you plan to release an advisory linking to multiple CVEs, add connections manually.
