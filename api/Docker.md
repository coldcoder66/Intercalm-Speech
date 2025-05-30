# In work, setup for Docker-based system

# Windows Subsystem for Linux
We need to install an environment for running the software for the Linux operating system within the Windows operating system. Windows provides this functionality through the Windows Subsystem for Linux (WSL). We'll need the latest version to be able to run Docker in the next step.

In Windows Powershell, run:

```
wsl --update
```

Now restart your computer for changes to take effect.

# Docker
First, we're installing [Docker Desktop]() which allows us to run containers, little computer instances, on our machine. 

Configur an account for Docker]().

Next, in Windows Powershell, run:

```
winget install Docker.DockerDesktop
```

Now open Docker Desktop and use the system defaults. Enter your Docker credentials.