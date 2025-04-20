# Intercalm-Speech
Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Package the Application
Build the application using `PyInstaller`:

```bash
python -m PyInstaller .\intercalm.spec
```

Now zip the `intercalm` directory and distribute the zip for others to run, 
just unzip the file at destination and run the `intercalm.exe` file, no installation required!