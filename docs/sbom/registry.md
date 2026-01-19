# SBOM Registry

The Eclipse Foundation SBOM registry is a shared platform where projects can upload and manage their SBOMs in one place, using our dedicated [DependencyTrack instance](https://sbom.eclipse.org/).

From a **maintainer** perspective, it removes the overhead of figuring out where and how to store SBOMs by providing a readily available solution with plug-and-play upload integrations.

From a **user** perspective, the registry offers a single location to explore SBOMs across all Eclipse Foundation projects, therefore improving transparency and making it easier to assess the software they depend on.

## How to view project SBOMs
The SBOM registry is available at [sbom.eclipse.org](https://sbom.eclipse.org/). To authenticate, use your **Eclipse Foundation account credentials**. If you do not already have an account, you can create one [here](https://accounts.eclipse.org). 

Once logged in, click on **Projects** and use the search bar on the right side of the platform to locate the project you wish to assess. 

Note that a single project may contain multiple products or components, so the hierarchy may vary between entries. In general, an SBOM should be generated and published by projects for each new release of every component. The registry also retains historical data, allowing users to view SBOMs for past releases as needed.

## How to upload project SBOMs
Documentation on how projects can upload their SBOMs to our SBOM Registraty can be found in the [How to generate and upload SBOMs](./howto.md) guide.