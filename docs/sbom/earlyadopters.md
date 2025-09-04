# SBOM Early Adopters

The Eclipse Foundation Security Team is leading an ongoing initiative to support projects in adopting Software Bill of Materials (SBOM), with a particular focus on designing and implementing Github Actions workflows that:
- automatically generate SBOMs for new project releases, and
- publish them to our DependencyTrack [instance](https://sbom.eclipse.org)

As part of this initiative, we are collaborating with early adopter groups to design and implement such workflows tailored to their specific ecosystems and release processes. 

These engagements helped identify common challenges as well as effective solutions, which we are now sharing to accelerate broader adoption. The examples in the table below illustrate a variety of successful implementation strategies developed as a result of these collaborations. They are intended to serve as practical inspiration for projects looking to integrate SBOM generation into their own release workflows.

| Project        | Ecosystem        | SBOM Workflow                                                                 |
|----------------|------------------|-------------------------------------------------------------------------------------------|
| Eclipse CSI    | Python           | [generate-sbom.yml](https://github.com/eclipse-csi/otterdog/blob/main/.github/workflows/generate-sbom.yml) |
| Eclipse SysON  | NPM              | [generate-npm-sbom.yml](https://github.com/eclipse-syson/syson/blob/main/.github/workflows/generate-npm-sbom.yml) |
|                | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-syson/syson/blob/main/.github/workflows/generate-maven-sbom.yml) |
| Eclipse Kuksa  | Python           | [generate-python-sbom.yml](https://github.com/eclipse-kuksa/kuksa-python-sdk/blob/main/.github/workflows/generate-python-sbom.yml) |
| Eclipse LMOS   | Gradle           | [generate-gradle-sbom.yml](https://github.com/eclipse-lmos/arc/blob/main/.github/workflows/generate-gradle-sbom.yml) |
| Eclipse JKube  | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-jkube/jkube/blob/master/.github/workflows/generate-maven-sbom.yml) |

We strongly encourage all projects to take an active role in implementing SBOM in their own release processes. While our initiative provides examples and resources to help projects get started independently, we also maintain a queue of early adopter projects that we are directly supporting. If your project would benefit from our guidance, we welcome you to reach out to the Eclipse Foundation Security Team with the details below.
- **Sent to**: security@eclipse-foundation.org
- **Subject**: "SBOM Early Adopters"
- **Project context**:
  - Repository link
  - Description of products
  - Publishing locations
  - Ecosystems
  - Versioning strategy
  - Release process

Please note that support availability may depend on current capacity, but we are always happy to engage and assist where possible.