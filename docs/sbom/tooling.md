# Tooling Ecosystem for CycloneDX
This page introduces a selection of tools that can help **generate** SBOMs across different programming languages and ecosystems. While not exhaustive, it aims to offer a starting point for creating SBOMs in the CycloneDX format.

| **Environment**     | **Ecosystem/Build System** | **Tool**                                                      |
|---------------------|----------------------------|---------------------------------------------------------------|
| **Java**            | Maven                      | [cyclonedx-for-maven](#cyclonedx-for-maven)                   |
|                     | Gradle                     | [cyclonedx-for-gradle](#cyclonedx-for-gradle)                 |
| **Python**          | All                        | [cyclonedx-for-python](#cyclonedx-for-python)                 |
|                     | Github Actions             | [gh-python-generate-sbom](#gh-python-generate-sbom)|
| **Nodejs**          | All                        | [cyclonedx-bom](#cyclonedx-bom)                               |
|                     | NPM                        | [cyclonedx-npm](#cyclonedx-npm)                               |
|                     | Yarn                       | [yarn-plugin-cyclonedx](#yarn-plugin-cyclonedx)               |
|                     | React                      | [webpack-plugin with React](#webpack-plugin-with-react)       |
|                     | Github Actions             | [gh-node-module-generatebom](#gh-node-module-generatebom)     |
| **Go**              | Modules                    | [cyclonedx-gomod](#cyclonedx-gomod)                           |
| **Multi-Ecosystem** | All                        | [cdxgen](#cdxgen)                                             |
|                     | Github Actions             | [cdxgen-action](#cdxgen-action)         |

---
## Java
Java is a compiled language, meaning an SBOM should be generated whenever a release version of the project is built. Since Java build systems are responsible for downloading all the dependencies required to compile and package the project, the optimal choice is to generate an SBOM during the build process. 

## Maven
### CycloneDX for Maven

* Website: https://cyclonedx.github.io/cyclonedx-maven-plugin/
* Source: https://github.com/CycloneDX/cyclonedx-maven-plugin
* Supported data sources: `pom.xml` files

### Usage
CycloneDX plugin is available on Maven central. To start using it, add the following plugin into the `pom.xml` file:
```
<plugin>
    <groupId>org.cyclonedx</groupId>
    <artifactId>cyclonedx-maven-plugin</artifactId>
    <version>2.7.0</version>
</plugin>
```
To generate the SBOM, select the suitable `goal` and use the ```mvn cyclonedx:<goal>``` command. More details on goals can be found below.

### Integration
By integrating a plugin into the Maven setup, projects can automatically generate SBOMs for each release, as part of the CI pipeline. The plugin supports 3 different methods of generating the record (goals):
* [makeBom](https://cyclonedx.github.io/cyclonedx-maven-plugin/makeBom-mojo.html)
* [makeAggregateBom](https://cyclonedx.github.io/cyclonedx-maven-plugin/makeAggregateBom-mojo.html)
* [makePackageBom](https://cyclonedx.github.io/cyclonedx-maven-plugin/makePackageBom-mojo.html)

More details in can be found in the [official documentation](https://cyclonedx.github.io/cyclonedx-maven-plugin/index.html#goals).

```
<plugins>
   <plugin>
       <groupId>org.cyclonedx</groupId>
       <artifactId>cyclonedx-maven-plugin</artifactId>
       <executions>
           <execution>
               <phase>package</phase>
               <goals>
                   <goal>makeAggregateBom</goal>
               </goals>
           </execution>
       </executions>
   </plugin>
</plugins>
```

### Configuration
The CycloneDX Maven Plugin offers several configuration options that allow customization of how the SBOM is generated for the project, such as: tool version, output format, output location, whether to include license text, whether to include specific dependencies, whether to attach it to the build artifacts.

Below is an example of the **default** configuration:

```
<plugins>
    <plugin>
        <groupId>org.cyclonedx</groupId>
        <artifactId>cyclonedx-maven-plugin</artifactId>
        <configuration>
            <projectType>library</projectType>
            <schemaVersion>1.6</schemaVersion>
            <includeBomSerialNumber>true</includeBomSerialNumber>
            <includeCompileScope>true</includeCompileScope>
            <includeProvidedScope>true</includeProvidedScope>
            <includeRuntimeScope>true</includeRuntimeScope>
            <includeSystemScope>true</includeSystemScope>
            <includeTestScope>false</includeTestScope>
            <includeLicenseText>false</includeLicenseText>
            <outputReactorProjects>true</outputReactorProjects>
            <outputFormat>all</outputFormat>
            <outputName>bom</outputName>
            <outputDirectory>${project.build.directory}</outputDirectory><!-- usually target, if not redefined in pom.xml -->
            <verbose>false</verbose><!-- = ${cyclonedx.verbose} -->
        </configuration>
    </plugin>
</plugins>
```

### Additional Reading
* [Snyk Blog: How to create SBOMs in Java with Maven and Gradle](https://snyk.io/blog/create-sboms-java-maven-gradle/)
* [Learn SBOM: Tool Review: CycloneDX Maven](https://www.youtube.com/watch?v=YK9mHhegQV4)

## Gradle
### CycloneDX for Gradle
* Website: https://plugins.gradle.org/plugin/org.cyclonedx.bom
* Source: https://github.com/CycloneDX/cyclonedx-gradle-plugin
* Supported data sources: `build.gradle` or `build.gradle.kts` file

### Usage
To start using it, add the following plugin into the `build.gradle` file:
```
plugins {
  id("org.cyclonedx.bom") version "1.10.0"
}
```

To generate the SBOM, run the `gradle cyclonedxBom` command.

### Integration
In Gradle, SBOM generation with the CycloneDX plugin requires a manual setup within CI, as it doesn’t automatically align with predefined build phases like Maven does. The details depend on project specifics, but in broad terms, in order to integrate, invoking the cyclonedxBom task directly in the CI pipeline after successful builds is necessary. This ensures an SBOM is generated with each stable release.

As opposed to Maven's `goals`, Gradle relies on the single `cyclonedxBom` task, meaning it appears to be generating a single SBOM for the project, instead of one per artifact. For publishing, it requires some additional configuration, see [issue link](https://github.com/CycloneDX/cyclonedx-gradle-plugin/issues/388).

### Configuration
The CycloneDX Gradle Plugin offers several configuration options that allow customization of how the SBOM is generated for the project. More details about each configuration option can be found in the plugin [README](https://github.com/CycloneDX/cyclonedx-gradle-plugin). 

Below is an example of the a configuration. To customise the configuration for your project, simply append it to the `gradle` file.
```
cyclonedxBom {
    includeConfigs = ["runtimeClasspath"]
    skipConfigs = ["compileClasspath", "testCompileClasspath"]
    skipProjects = [rootProject.name, "yourTestSubProject"]
    projectType = "application"
    schemaVersion = "1.6"
    destination = file("build/reports")
    outputName = "bom"
    outputFormat = "json"
    includeBomSerialNumber = false
    includeLicenseText = false
    includeMetadataResolution = true
    componentVersion = "2.0.0"
    componentName = "my-component"
}
```

## Python
### CycloneDX for Python
* Website: https://pypi.org/project/cyclonedx-bom/
* Source: https://github.com/CycloneDX/cyclonedx-python
* Requirements: Python ```>=3.8,<4```

### Supported data sources
* Python (virtual) environment
* Poetry manifest and lockfile
* Pipenv manifest and lockfile
* Pip's `requirements.txt` format
* PDM's Python virtual environments 
* conda's Python environments

### Installation
* Install via pip: `python -m pip install cyclonedx-bom`
* Install via pipx: `pipx install cyclonedx-bom`
* Install via poetry: `poetry add cyclonedx-bom`

### Usage
* Call script: `cyclonedx-py <source> -o sbom.json`
* Call python module CLI: `python3 -m cyclonedx_py <source> -o sbom.json`

### Integration
In order to automate SBOM generation and publishing for new releases, depending on the CI tool you're using, the next step is to add a command that generates the SBOM as part of your build process. 

For projects that use GitHub Actions, a workflow can be defined with steps for:
* Generation
```
- name: Install cyclonedx-py
  run: pipx install cyclonedx-bom
- name: Generate sbom
  run: cyclonedx-py poetry -o bom.json
```
* Upload
```
- name: Upload sbom
        uses: actions/upload-artifact@b4b15b8c7c6ac21ea08fcf65892d2ee8f75cf882 # v4.4.3
        with:
          name: bom.json
          path: bom.json
```
A complete workflow example for SBOM generation and upload to DependencyTrack can be found here: [generate-sbom.yml](https://github.com/eclipse-csi/otterdog/blob/main/.github/workflows/generate-sbom.yml).

---
### gh-python-generate-sbom
* Website: https://github.com/marketplace/actions/cyclonedx-python-generate-sbom
* Source: https://github.com/CycloneDX/gh-python-generate-sbom
* Supported data sources: Pip's `requirements.txt` format
* Requirements: cyclonedx-bom```>=1.4.0,<4```

### Usage
```
- name: Generate Python SBOM
  uses: CycloneDX/gh-python-generate-sbom@v2
  with:
    input: ./requirements.txt
    output: ./bom.json
    format: json
```

## Nodejs
### CycloneDX BOM
* Website: https://www.npmjs.com/package/@cyclonedx/bom?activeTab=readme
* Source: https://github.com/CycloneDX/cyclonedx-node-module

As per the official website above, CycloneDX BOM is a "meta-package", a collection of optional dependencies. The dependencies are tools with the common purpose of generating SBOMs for node-based projects. To identify the optimal tooling for your ecosystem, check the table bellow or the [README](https://github.com/CycloneDX/cyclonedx-node-module/blob/master/README.md) of the project for the most up to date information about available tooling.

| Ecosystem/System | Actual Tool                          |
|-----------|--------------------------------------|
| npm       | [cyclonedx/cyclonedx-npm](https://www.npmjs.com/package/%40cyclonedx/cyclonedx-npm)            |
| yarn      | [cyclonedx/yarn-plugin-cyclonedx](https://www.npmjs.com/package/%40cyclonedx/yarn-plugin-cyclonedx)    |
| Angular          | [cyclonedx/webpack-plugin with Angular](https://www.npmjs.com/package/%40cyclonedx/webpack-plugin?activeTab=readme#user-content-use-with-angular)              |
| React            | [cyclonedx/webpack-plugin with React](https://www.npmjs.com/package/%40cyclonedx/webpack-plugin?activeTab=readme#user-content-use-with-react)               |
| Rollup           | [rollup-plugin-sbom](https://www.npmjs.com/package/rollup-plugin-sbom?activeTab=readme)                                  |
| Vite             | [rollup-plugin-sbom with Vite](https://www.npmjs.com/package/rollup-plugin-sbom?activeTab=readme#usage-with-vite)                        |
| webpack          | [cyclonedx/webpack-plugin](https://www.npmjs.com/package/%40cyclonedx/webpack-plugin) 

## Nodejs: npm
### cyclonedx-npm
* Website: https://www.npmjs.com/package/%40cyclonedx/cyclonedx-npm?activeTab=readme
* Requirements: node ```>=14```, npm ```in range 6 - 10```

### Supported data sources
As per [cyclonedx-node-npm/docs/how.md](https://github.com/CycloneDX/cyclonedx-node-npm/blob/main/docs/how.md):
>This tool utilizes npm-ls on the target project and parses its output.  
>This way the tool does not depend on libraries that are already part of npm. All logic and analysis is done by npm itself, the output is just interpreted and used.  
>Sometimes npm-ls got hiccups - caused by individual broken project installation or bugs with npm. Then, this tool may also read `package.json` files inside the node_module directory as an additional information source.

### Installation
* Install as a global tool via npm: `npm install --global @cyclonedx/cyclonedx-npm`
* Install as a global tool via npx: `npx --package @cyclonedx/cyclonedx-npm --call exit`
* Install as a development dependency of the current project: `npm install --save-dev @cyclonedx/cyclonedx-npm`

### Usage
* If installed via npm: `cyclonedx-npm --help`
* If installed via npx/project dependency: `npx @cyclonedx/cyclonedx-npm --help`

### Integration
Integration steps depend on project details and CI tools. In broad terms, when using Github Actions a new workflow can be set up, similar to the Python example above. For Jenkins usage, including a new stage in the pipeline can help with SBOM generation and artifact upload.

## Nodejs: yarn
### yarn-plugin-cyclonedx
* Website: https://www.npmjs.com/package/%40cyclonedx/yarn-plugin-cyclonedx
* Requirements: node ```>=18```, yarn ```>=3 (berry)```

### Installation
* Zero-install
* Install as a development dependency of the current project (cli-wrapper):  
 `yarn add --dev @cyclonedx/yarn-plugin-cyclonedx`
* Install the [latest version from Github](https://github.com/CycloneDX/cyclonedx-node-yarn/releases/tag/v1.0.2):  
```yarn plugin import https://github.com/CycloneDX/cyclonedx-node-yarn/releases/latest/download/yarn-plugin-cyclonedx.cjs```

### Usage
* Zero-install via dlx-wrapper: `yarn dlx -q @cyclonedx/yarn-plugin-cyclonedx --help`
* Cli-wrapper: `yarn exec cyclonedx-yarn --help`
* Plugin: `yarn cyclonedx --help`

### Integration
Depends on installation method, project details and CI tools.

## Nodejs: React
### webpack-plugin with React
* Website: https://github.com/CycloneDX/cyclonedx-node-module
* Requirements:  Node.js ```>=14```, webpack ```^5```;
* Requirements (older plugin versions): Node.js ```v8.0.0 or higher```, webpack ```v4.0.0 or higher```;

### Installation
* Install via npm: `npm i -D @cyclonedx/webpack-plugin`
* Install via yarn: `yarn add -D @cyclonedx/webpack-plugin`

### Usage
Initialize and configure the plugin through:  
```new CycloneDxWebpackPlugin(options?: object)```

### Configuration
Configuration options can be found in this [table](https://www.npmjs.com/package/%40cyclonedx/webpack-plugin?activeTab=readme#options--configuration).

An example of configuring the CycloneDX plugin in `webpack config` can be found in [the plugin documentation](https://www.npmjs.com/package/%40cyclonedx/webpack-plugin?activeTab=readme#options--configuration):

```
const { CycloneDxWebpackPlugin } = require('@cyclonedx/webpack-plugin');

/** @type {import('@cyclonedx/webpack-plugin').CycloneDxWebpackPluginOptions} */
const cycloneDxWebpackPluginOptions = {
  includeWellknown: true,
  wellknownLocation: './.well-known'
}

module.exports = {
  // ...
  plugins: [
    new CycloneDxWebpackPlugin(cycloneDxWebpackPluginOptions)
  ]
}
```
See [extended examples](https://github.com/CycloneDX/cyclonedx-webpack-plugin/tree/master/examples).

## Nodejs
### gh-node-module-generatebom
* Website: https://github.com/marketplace/actions/cyclonedx-node-js-generate-sbom
* Source: https://github.com/CycloneDX/gh-node-module-generatebom
* Requirements:  @cyclonedx/bom@ ```<4```
* Supported data sources: 
>This GitHub action requires a `node_modules` directory so this action will typically need to run after an npm build.

### Usage
* Simple usage:  
```
uses: CycloneDX/gh-node-module-generatebom@v1
```
* Usage with defining output and path:  
```
- name: Create SBOM step
  uses: CycloneDX/gh-node-module-generatebom@v1
  with:
    path: './node_project/'
    output: './bom_directory/bom.xml'
```

### Configuration
* `path` to a node.js project, default is `./`
* `output` output filename, default is `bom.xml`

## Go: Modules
### cyclonedx-gomod
* Source: https://github.com/CycloneDX/cyclonedx-gomod

### Installation
* Install via Homebrew: `brew install cyclonedx/cyclonedx/cyclonedx-gomod`
* Install from source: `go install github.com/CycloneDX/cyclonedx-gomod/cmd/cyclonedx-gomod@latest`

### Usage
* Simple usage:  
```
cyclonedx-gomod <SUBCOMMAND> [FLAGS...] [<ARG>...]
```

Subcommands:
* `app`: Generate SBOMs for applications, include only those modules that the target application
  actually depends on
* `mod`: Generate SBOMs for modules, include the aggregate of modules required by all 
  packages in the target module (optionally includes modules required by
  tests and test packages)
* `bin`: Generate SBOMs for binaries
* `version`: Show version information

More info about subcommands and usage can be found in [README:Usage](https://github.com/CycloneDX/cyclonedx-gomod?tab=readme-ov-file#usage).
SBOM examples for each subcommand can be found in the [examples](https://github.com/CycloneDX/cyclonedx-gomod/tree/main/examples) directory. 

### Integration
Support with integrating the plugin with various tools:
* Github Actions: [ gh-gomod-generate-sbom](https://github.com/marketplace/actions/cyclonedx-gomod-generate-sbom) on GitHub marketplace
* [GoReleaser](https://github.com/CycloneDX/cyclonedx-gomod?tab=readme-ov-file#goreleaser-)
* [Docker](https://github.com/CycloneDX/cyclonedx-gomod?tab=readme-ov-file#docker-)

### Configuration
Options can be configured through flags, depending on the subcommand of choice. See [README:Subcommands](https://github.com/CycloneDX/cyclonedx-gomod?tab=readme-ov-file#subcommands) for the full list of options.

## Multi-Ecosystem Tools
### cdxgen
* Website: https://cyclonedx.github.io/cdxgen
* Source: https://github.com/CycloneDX/cdxgen

### Supported Languages/Platforms: [Comprehensive List](https://cyclonedx.github.io/cdxgen/#/PROJECT_TYPES)
* Java (Maven, Gradle, sbt, more)
* Node.js
* Python
* Golang
* Rust
* PHP
* .NET
* C++
* Container (docker, podman)
* Container files (docker, podman)
* Swift
* OpenAPI

### Installation: [Instructions](https://cyclonedx.github.io/cdxgen/#/CLI?id=installing)
* Via Npm: ```npm install -g @cyclonedx/cdxgen```
* Via Homebrew: ```brew install cdxgen```

### Usage
* Generate an SBOM for cwd: `cdxgen -t <lang> .`
* Generate an SBOM for cwd for a Multi-Language project: `cdxgen -t <lang> -t <lang> .`  
---

### cdxgen-action
* Website: https://github.com/marketplace/actions/cdxgen
* Source: https://github.com/CycloneDX/cdxgen-action

### Supported Languages/Platforms: [Comprehensive List](https://cyclonedx.github.io/cdxgen/#/PROJECT_TYPES)
* Java (Maven, Gradle, sbt, more)
* Node.js
* Python
* Golang
* Rust
* PHP
* .NET
* C++
* Container (docker, podman)
* Container files (docker, podman)
* Swift
* OpenAPI

### Usage
To simply print the SBOM to console, add the following step to a workflow:
```
uses: AppThreat/cdxgen-action@v1
```
### Integration
Workflows can be defined that integrate a variation of the following steps:
* Upload to dependency track server
```
- uses: AppThreat/cdxgen-action@v1
  with:
    output: "./bom.xml"
    serverUrl: "<server_url>"
    apiKey: ${{ secrets.apiKey }}
```
* Upload to dependency track server and store artefacts:
```
- uses: AppThreat/cdxgen-action@v1
  with:
    output: "./sboms/bom.xml"
    serverUrl: "<server_url>"
    apiKey: ${{ secrets.apiKey }}
- uses: actions/upload-artifact@v1
  with:
    name: sboms
    path: sboms
```
