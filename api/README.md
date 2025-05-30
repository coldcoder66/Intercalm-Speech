# VSCode Extension
MSSQL extension for Visual Studio Code: In Visual Studio Code, open the Extensions view by selecting the Extensions icon in the Activity Bar on the side of the window. Search for `mssql` and select Install to add the extension.

# Windows Subsystem for Linux
We need to install an environment for running the software for the Linux operating system within the Windows operating system. Windows provides this functionality through the Windows Subsystem for Linux (WSL). We'll need the latest version to be able to run Docker in the next step.

In Windows Powershell, run:

```
wsl --update
```

# Docker
First, we're installing [Docker Desktop]() which allows us to run containers, little computer instances, on our machine. In Windows Powershell, run:

```
winget install Docker.DockerDesktop
```

# Database Setup
1. Install SQL Server Developer Edition

Download [Windows SQL Server 2022 Express edition](https://www.microsoft.com/en-us/download/details.aspx?id=104781) or install via Winget by opening Powershell and running:

```
winget install Microsoft.SQLServer.2022.Express  
```

2. Open Microsoft SQL Server Management Studio
3. Authenticate using Windows auth (trust local certificate)
4. Create database named `intercalmdb-test`