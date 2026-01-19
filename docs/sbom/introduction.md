# Introduction to SBOM
This page provides an introduction into the concept of Software Bill of Materials (SBOM) and briefly explores its purpose, significance and role in enhancing software security. As open source projects are increasingly integrated into critical software and services, understanding and implementing SBOMs has become essential for maintainers and developers. 

This page outlines what an SBOM is, why it's crucial for project transparency and risk management and how it addresses key security considerations for software supply chains.

## What is an SBOM?
A Software Bill of Materials (SBOM) is a structured list detailing all components, libraries and dependencies within a software application, along with their version information. It provides a list of "ingredients" that make up a software product. 

This record provides visibility into every component comprised in an application, regardless of whether these components are proprietary, open source or third-party dependencies. It uniquely identifies each dependency, as well as provides insights into their hierarchical relationships.

## Purpose
The primary purpose of an SBOM is to ensure transparency and accountability in software development. By detailing every component in a project, an SBOM helps developers, security teams and users understand exactly what their software contains, making it easier to track dependencies and respond effectively to potential risks.

Additionally, SBOMs empower software consumers and contributors to evaluate the security, quality and license compliance of the software they use and develop, creating a more trustworthy open source ecosystem.

## Security Considerations
From a security perspective, SBOMs are invaluable due to their inherent trait, that of providing visibility into the elements that make up a software project. 

When facing supply chain concerns, these inventories enable organizations to quickly and efficiently answer questions such as "Am I affected?" and "Where am I affected?", providing support into identifying and mitigating vulnerabilities in a timely manner.

## Adoption
By integrating SBOM generation into your project workflow, you’re taking a proactive step toward ensuring a secure and resilient codebase. This practice not only enhances the transparency and integrity of your software but also aligns with modern standards for responsible software development. 

We encourage all open-source projects to adopt SBOM generation as a regular part of their development process, fostering a more secure, trustworthy ecosystem for developers and users alike.

## Further Reading
* [Eclipse Foundation Security Training 2025 | SBOMs, Dependency Tracking](https://www.youtube.com/watch?v=gotOnATJu4E&list=PLy7t4z5SYNaT7JN8FIVTGAy1QUnLTdv9R&index=8)
* [SBOM Resources Library - CISA](https://www.cisa.gov/topics/cyber-threats-and-advisories/sbom/sbomresourceslibrary)
* [SBOM at a Glance - NTIA](https://www.ntia.gov/sites/default/files/publications/sbom_at_a_glance_apr2021_0.pdf)
* [SBOM Explainer Videos on Youtube (2020-2021) - NTIAGov](https://www.youtube.com/playlist?list=PLO2lqCK7WyTDpVmcHsy6R2HWftFkUp6zG)
