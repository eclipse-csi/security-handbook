# SBOM Early Adopters

The Eclipse Foundation Security Team is leading an ongoing initiative to support projects in adopting Software Bill of Materials (SBOM). Our aim is to enable project in pursuing independent implementations of SBOM generation and upload workflows into their existing release pipelines. 

As such, we have been collaborating with Early Adopter projects and offering our hands-on support to design and implement such workflows tailored to their specific ecosystems and release processes. These engagements helped identify common challenges as well as effective solutions, which we are now sharing to accelerate broader adoption. 

The examples in the table below illustrate a variety of successful implementation strategies developed as a result of these collaborations. They are intended to serve as practical inspiration for projects looking to integrate SBOM generation into their own release workflows.

| Project            | Ecosystem        | SBOM Workflow                                                                                                           |
|--------------------|------------------|-------------------------------------------------------------------------------------------------------------------------|
| Eclipse Che        | NPM              | [chectl/generate-npm-sbom.yml](https://github.com/che-incubator/chectl/blob/main/.github/workflows/generate-sbom.yml)   |
| Eclipse SysON      | NPM              | [syson/generate-npm-sbom.yml](https://github.com/eclipse-syson/syson/blob/main/.github/workflows/generate-npm-sbom.yml) |
| Eclipse Theia      | NPM (monorepo)   | [theia/generate-sbom.yml](https://github.com/eclipse-theia/theia/blob/master/.github/workflows/generate-sbom.yml)       |
| Eclipse Langium    | NPM (monorepo)   | [langium/generate-sbom.yml](https://github.com/eclipse-langium/langium/blob/main/.github/workflows/generate-sbom.yml)   |
| Eclipse SysON      | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-syson/syson/blob/main/.github/workflows/generate-maven-sbom.yml)   |
| Eclipse JKube      | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-jkube/jkube/blob/master/.github/workflows/generate-maven-sbom.yml) |
| Eclipse Che        | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-che/che-server/blob/main/.github/workflows/generate-maven-sbom.yml)|
| Eclipse Milo       | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-milo/milo/blob/main/.github/workflows/generate-maven-sbom.yml)     |
| Eclipse Store      | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-store/store/blob/main/.github/workflows/generate-maven-sbom.yml)   |
| Eclipse Serializer | Maven            | [generate-maven-sbom.yml](https://github.com/eclipse-serializer/serializer/blob/main/.github/workflows/generate-maven-sbom.yml) |
| Eclipse Kura       | Maven, Tycho     | [target-platform-sbom.yml](https://github.com/eclipse-kura/kura/blob/develop/.github/workflows/target-platform-sbom.yml)|
| Eclipse CSI        | Python           | [generate-sbom.yml](https://github.com/eclipse-csi/otterdog/blob/main/.github/workflows/generate-sbom.yml)              |
| Eclipse Kuksa      | Python           | [generate-python-sbom.yml](https://github.com/eclipse-kuksa/kuksa-python-sdk/blob/main/.github/workflows/generate-python-sbom.yml) |
| Eclipse LMOS       | Gradle           | [generate-gradle-sbom.yml](https://github.com/eclipse-lmos/arc/blob/main/.github/workflows/generate-gradle-sbom.yml)    |

We strongly encourage all projects to take an active role in integrating SBOM generation into their release processes. To support this, we provide a comprehensive set of internally developed resources, including detailed documentation, implementation examples, and plug-and-play integrations, enabling projects to adopt SBOM practices independently. 

Should a project require additional guidance or hands-on assistance, the Eclipse Foundation Security Team is available to provide support. Please feel free to reach out with the following details:
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