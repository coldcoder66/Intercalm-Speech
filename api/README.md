
# Database Setup
1. Install SQL Server Developer Edition

Download [Windows SQL Server 2022 Express edition](https://www.microsoft.com/en-us/download/details.aspx?id=104781) or install via Winget by opening Powershell and running:

```
winget install Microsoft.SQLServer.2022.Express  
```

2. In powershell, run:

```
sqlcmd
```

Then run
```
SELECT Name
FROM sys.databases;
GO
```

This is the databases on the system. Let's create the developer database named  `intercalmdbdev`:

```
CREATE DATABASE intercalmdev
GO
```

# VSCode Extension
MSSQL extension for Visual Studio Code: In Visual Studio Code, open the Extensions view by selecting the Extensions icon in the Activity Bar on the side of the window. Search for `mssql` and select Install to add the extension. Then hit CTRL+alt+D to open the SQL Server view.

Now using Windows authenticaiton, connect to the local database `intercalmdev`