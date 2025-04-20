# Intercalm-Speech
Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Package the Application

### Windows
Build the application using `PyInstaller`. We use the `--log-level=ERROR` to build faster as only error level probalems will print to the console.

```bash
python -m PyInstaller --log-level=ERROR .\intercalm.spec
```

run the application under `.\dist\intercalm\intercalm.exe`.

Now zip the `intercalm` directory and distribute the zip for others to run, 
just unzip the file at destination and run the `intercalm.exe` file, no installation required!