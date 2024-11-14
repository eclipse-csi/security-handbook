# Tooling Ecosystem for CycloneDX
This page introduces a selection of tools that can help **generate** SBOMs across different programming languages and ecosystems. While not exhaustive, it aims to offer a starting point for creating SBOMs in the CycloneDX format.


| **Environment**                    | **Tool**                                           |
|---------------------|----------------------------------------------------|
| **Java: Maven**     | [CycloneDX Maven Plugin](#cyclonedx-for-maven)     |
| **Java: Gradle**    | [CycloneDX Gradle Plugin](#cyclonedx-for-gradle)|
| **Python**          | [CycloneDX for Python](#cyclonedx-for-python)|
|                     | [Github Action: CycloneDX for Python](#github-action-cyclonedx-for-python)|
| **Multi-Ecosystem** | [cdxgen](#cdxgen)|
|                     | [Github Action: cdxgen](#github-action-cdxgen)|

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
The CycloneDX Maven Plugin offers several configuration options that allow customization of how the SBOM is generated for the project, such as: tool version, output format, output location, whether to include license text, whether to include specific dependencies, whether attach it to the build artifacts.

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
A complete workflow example for SBOM generation and upload to DependencyTrack can be found here: [generate-sbom.yml](https://github.com/eclipse-csi/otterdog/blob/main/.github/workflows/generate-.sbom.yml).

---
### Github Action: CycloneDX for Python
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
---
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

### Github Action: cdxgen
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
Workflow can be defined that integrate a variation of following steps:
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
---