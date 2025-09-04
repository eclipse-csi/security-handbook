# Best Practices Related to Embargoes

This document presents recommendations on handling embargoes by Eclipse Foundation projects. In general, projects should adhere to the [Eclipse Foundation Vulnerability Reporting Policy](https://www.eclipse.org/security/policy/); this document provides additional guidelines and best practices when handling embargoes. Each project might decide to act differently if the situation, and security of their users, requires this.

Readers of this document should be familiar with terms and definitions of the [Eclipse Foundation Development Process](https://www.eclipse.org/projects/dev_process) and the [Eclipse Foundation Vulnerability Reporting Process](https://www.eclipse.org/security/policy/). Please review them if needed.

## What is an embargo?

An *embargo* is a term used to name the period of time from the moment a vulnerability is disclosed to the vendor, to the moment it is made public by the announcement of the CVE number (Common Vulnerabilities and Exposures), a fix in the release notes, a security advisory, or any other public communication.

The period of embargo allows the affected project to investigate, prepare the fix, test it, and prepare documentation. People who have access to the information on the vulnerability during the embargo period *must* keep it confidential. An embargo can last from a few hours (when the fix is easy low-risk, and the project releases a bugfix release immediately) to months or sometimes even years (usually for complex hardware vulnerabilities).

## Single-project embargoes

In the most common case, a vulnerability affects one Project. The embargo then includes the reporter or reporters of the vulnerability and the Project's Security Team. In this case, the Eclipse Foundation Vulnerability Reporting Process applies directly and there is no need for any special procedures.

## Multi-project embargoes

Sometimes an embargo affects multiple projects. It might be because of a common vulnerable dependency, common shared code, or a common implementation flaw.

Note: Examples for common implementation flaws include HTTP/2 implementation issues from 2023 and 2024. A good illustration is the [advisory for the HTTP/2 CONTINUATION frame](https://kb.cert.org/vuls/id/421644) issue with the list of allocated CVEs and vendor responses.

Multi-project embargoes are usually used for high impact issues that could cause serious harm to users if the vulnerability gets disclosed without a fix from all (or at least most) of the affected parties.

In a case of a wide embargo, Projects need to synchronize on release dates, and if it makes sense, also share test cases, and prepare a common advisory. They either communicate using an ad-hoc distribution list, or use a dedicated disclosure platform.

An invitation to such a disclosure group usually arrives to the Projects security contact, or to some specific developer directly if they are known to deal with security issues. In case of Eclipse Foundation projects (also other projects hosted by foundations), such an invitation also often comes to the generic security contact of the Foundation. In the case of Eclipse Foundation, this will be the EF Security Team that will forward it to the affected project or projects. Note the importance of *up-to-date security contacts* known both publicly and by the EF Security Team. If the researcher cannot find the contact information, your Project might miss the notification and learn about the vulnerability late.

During the embargo time, it is important to not post any information of the vulnerability, nor a suggestion of one, in any channels. This includes references to security fixes in commit messages, release notes, announcements or even a Project-specific chat. All involved Projects release their bugfix versions at the same date or shortly after. Only then the Project can put information on the vulnerability in the documentation.

It is usually acceptable to announce a pending security release a few days before the final date. In case of a doubt, check with the embargo organizers.

If your Project needs to organize a multi-project embargo, contact the EF Security team for possible technical assistance.

Note: There exist also specific, long-term embargo lists that get used for embargoes in a specific ecosystem. An example includes the [OSS-distros mailing list](https://oss-security.openwall.org/wiki/mailing-lists/distros) that includes various well-known Linux distributions. The conditions for inclusions in those mailing lists are specific to each of those lists.

## Developing a fix under an embargo

If you are developing a fix for an issue under an embargo, you should use private forks and private CI (continuous integration). As a general guideline:

* Do not push fixes under embargo to public branches or repositories until agreed with the disclosure coordinator;
* Use a local CI copy. It can be either a setup running on the developer's machine, an in-premises copy, or a special private CI run spawned by the Eclipse Foundation IT team;
* If the vulnerability is potentially severe and has a high risk of rapid exploitation, avoid creating tickets (even private ones) in development forges.

The Project should review the potential severity of the issue and adjust measures as needed. If unsure, ask the disclosure coordinator or the EF Security team for guidance. In this case, you do not need to disclose details of the vulnerability that has a fix under development.

At the moment the embargo is lifted, the Project should make public all previously-private issues and tickets related to the issue.

## The Traffic Light Protocol (TLP)

Projects might want to use the Traffic Light Protocol (TLP) for communication about undisclosed vulnerabilities. TLP allows clear marking of confidentiality of an issue and the intended audience. For a general description of the TLP, refer to the [CISA's document](https://www.cisa.gov/news-events/news/traffic-light-protocol-tlp-definitions-and-usage).

In the case of Open Source projects, a restricted number of levels is useful. The Eclipse Foundation Security team recommends the usage of the following levels:

* *TLP:Red* - the information poses significant risk and is available to a specific list of individuals only. It must not be shared with any other person without a clear agreement of the source of this information. The restriction also applies to employers, managers and IT personnel.
* *TLP:Amber* - this information poses risk and is restricted and can be shared with Project Security Team and Security Teams of possibly affected projects. This sharing should be always done using confidential means.
* *TLP:Clear* - the information is public and accessible to everyone

## Frequently asked questions

- I get a request to join a disclosure platform like [Vince](https://kb.cert.org/vince/) to discuss disclosure. What to do?

Contact the Eclipse Foundation Security team that likely already has access to that platform and can add Project representatives to the case.

- How do we get notified about a multi-project embargo?

Make sure your Project has clearly marked security contacts, for example in the ``SECURITY.md`` files. Researchers may also contact some project members directly in such cases, based on their known involvement and previous interactions.

- Does a vulnerability under a multi-project embargo get one or multiple CVEs?

It depends. If it is a common dependency, there will likely be one CVE. If there is a common implementation flaw, but in different code, projects might decide to issue one CVE per project. This is one of the subjects discussed during the embargo.

- I do not understand parts of the process or terms in the discussion with security researchers.

Ask the EF Security team for assistance.
