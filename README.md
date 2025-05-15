# Intercalm-Speech
Install dependencies using pip:

```bash
pip install -r requirements.txt
```


To launch the server, change to api directory and install requirements, then run main.py
```bash
cd api
pip install -r requirements.txt
python main.py
# Then navigate to localhost:8000 in a browser to view home endpoint
```

To launch the kivy app, change to the app directory, install requirements, and then run main.py
```bash
cd app
pip install -r requirements.txt
python main.py
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