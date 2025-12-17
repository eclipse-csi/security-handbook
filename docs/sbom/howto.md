# How to generate and upload SBOMs

This page aims to provide an example approach on how to start generating SBOMs for projects and upload them to our DependencyTrack instance.

## How to generate an SBOM
Depending on project specifics, one project repository may contain the source code for one or more products. Start by creating a list of products to generate SBOMs for, alongside their corresponding ecosystems and dependency files.

For projects hosted on Github, an easy way to start generating SBOMs, that does not interfere with existing build or releases processes, is through creating a new Github Actions workflow. 

In broad terms, the workflow should:
* Trigger for:
    * New releases
    * Depedency files modified
* Prepare setup
    * Checkout the repository
    * Setup ecosystem specific tooling
* Generate the SBOM
    * Use ecosystem specific SBOM generation tooling 
* Extract metadata
    * Get product version from SBOM
* Upload the SBOM as artifact

The implementation of some of the steps above may depend on:
* product ecosystem
* project specifics 
* sbom generation tooling used

SBOMs can be of multiple formats. We recommend generating one in the CycloneDX format as well, as it is the format supported by DependencyTrack platform. For sbom generation, there is a great variety of tooling available that can create the SBOM for you, make sure to take a look at our [Tooling Ecosystem for CycloneDX](tooling.md) guide to choose the tool that best suits your projects' use case. 

For projects that have multiple products, it is advisable to also generate multiple SBOMs, especially if the ecosystems differ. To achieve that, multiple ecosystem specific Github Actions workflows can be created.


### Example Workflow: Maven
This is an example pattern of a Github Actions workflow that creates an SBOM for one maven based product using the [cyclonedx-maven-plugin](https://cyclonedx.github.io/cyclonedx-maven-plugin/):

```
name: Generate Maven SBOM

# Trigger on new tags created/deps files changes
on:
  push:
    branches: 
      - "main"
    paths:
      - '<PRODUCT_PATH>/pom.xml'
    tags:
      - "v*"
  workflow_dispatch:
    inputs:
      version:
        description: 'Version'
        default: 'main'
        required: true

# Product specific settings
env:
  JAVA_VERSION: '<java_version>'     # java version used by the product
  JAVA_DISTRO: '<java_distro>'       # java distro used by the product
  PRODUCT_PATH: '<PRODUCT_PATH>'     # path within project repository for product source
  PLUGIN_VERSION: '<plugin_version>' # cyclonedx-maven-plugin version to use
  SBOM_TYPE: '<makeBom|makeAggregateBom|makePackageBom>' # cyclonedx plugin goal

permissions:
  contents: read

jobs:
  generate-sbom:
    runs-on: ubuntu-latest
    outputs:
      project-version: ${{ steps.version.outputs.PROJECT_VERSION }} # required for DependencyTrack upload
    steps:
      - name: Checkout repository
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          fetch-depth: 0
          ref: ${{ github.event.inputs.version }}

      - name: Setup Java SDK
        uses: actions/setup-java@3a4f6e1af504cf6a31855fa899c6aa5355ba6c12 # v4.7.0
        with:
          java-version: ${{ env.JAVA_VERSION }}
          distribution: ${{ env.JAVA_DISTRO }}

      - name: Generate sbom
        run: |
          mvn org.cyclonedx:cyclonedx-maven-plugin:$PLUGIN_VERSION:$SBOM_TYPE -f "$PRODUCT_PATH/pom.xml" --settings settings.xml # adapt to project
        
      - name: Extract product version
        id: version
        shell: bash
        run: |
          event="${{ github.event_name }}"
          ref="${{ github.ref }}"
          input="${{ github.event.inputs.version }}"
          VERSION="$(jq -r '.metadata.component.version' < ./${{ env.PRODUCT_PATH }}/target/bom.json)"
          if [[ "$event" == "push" && "$ref" == refs/heads/* ]] || \
            [[ "$event" == "workflow_dispatch" && ! "$input" =~ ^v ]]; then
            VERSION="${VERSION}@dev"
          fi
          echo "PROJECT_VERSION=$VERSION" >> $GITHUB_OUTPUT

      - name: Upload sbom
        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
        with:
          name: <artifact_name>
          path: ${{ env.PRODUCT_PATH }}/target/bom.json
```

>Make sure dependencies are pinned in Github Actions workflows, as this ensures stability and security by preventing unexpected updates or potential supply chain attacks. An alternative tool that can help in with pinning to commit SHAs is [Octopin](https://github.com/eclipse-csi/octopin)

The `project-version` output is then used in a subsequent job to upload the SBOM to our DependencyTrack instance.

More examples of SBOM Generation workflows for various ecosystems can be found in: [eclipse-csi/workflows](https://github.com/eclipse-csi/workflows)


## How to upload an SBOM to DependencyTrack

Once a functional workflow to generate SBOMs is created, the next question that arises is: what to do with them? The SBOM is now uploaded as an artifact for individual workflow runs, however with time searching for specific SBOMs can become tedious.

Our DependencyTrack instance is a centralized place where all EF projects can upload their SBOMs. This way they are easier to find through a web interface, have versioning and are enriched with vulnerability data.

To upload an SBOM to our DependencyTrack instance, first reach out to the EF Security Team with your desired project hierarchy i.e. number of products, their names. We will generate entries and get back to you with a list of `parentProject` IDs. 

> **Note**: Due to Dependency-Track limitations, no two (non-SBOM) entries across the platform can have the same name, even if their parents differ (see [this issue](https://gitlab.eclipse.org/eclipsefdn/helpdesk/-/issues/6352#note_4632960) for more details). We highly encourage choosing names that are unique to the project across the entire hierarchy.

Then, simply append the below at the end of the SBOM generation workflow. Make sure the job that generates the SBOM has the name `generate-sbom` and outputs `project-version` with the version of the product.

```
  store-sbom-data: 
    needs: ['generate-sbom']
    uses: eclipse-csi/workflows/.github/workflows/store-sbom-data.yml@main
    with:
      projectName: '<product_name>' # display name
      projectVersion: ${{ needs.generate-sbom.outputs.project-version }}
      bomArtifact: '<artifact_name>' # name from upload in generate-sbom job
      bomFilename: 'bom.json'
      parentProject: '<parentProject_ID>' # provisioned by us
```

> **Note**: Although SBOM entries may share the same name (`projectName`) across multiple projects, due to Dependency-Track limitations, UI issues might appear (see [this issue](https://gitlab.eclipse.org/eclipsefdn/helpdesk/-/issues/6956) for more details). We highly encourage using project specific `projectName` values. For example, instead of using `milestone` as a name for your project SBOMs, consider choosing a unique value, such as `<project>-milestone`.

`store-sbom-data` stores the SBOM and additional metadata in a predefined format. Otterdog picks the artifacts up upon workflow completion and automatically uploads the SBOM to the DependencyTrack instance.