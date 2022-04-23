The purpose of this lab is to help guide through the usage of the Viptela 
Config-Sync tool.

Viptela ConfigSync is a common framework being developed intended to give a 
standards based approach to working with REST API for configuration tasks with 
network equipment.  ConfigSync comes pre-built with a few functions to serve 
as examples on building new purposes for the tool.  

Viptela ConfigSync is composed of four files that will be used when interacting
 with devices: config_sync.py, viptela.py, helpers.py, and viptela.cfg. Each file 
has a unique purpose in this framework.

### config_sync.py
This file is the main program for the framework, and the file which will be launched
when the application is ready.  All three other files are pulled into this file (.py files with 
import statements and .cfg file is being read as a YAML file into a dictionary).

Launching the example config_sync will do a few automatic functions:
1. Pull any arguments from the command line using the argparse library
2. Enable logging using the logging library.  CLI argument --debug offers enhanced logging.
3. Instantiate the ConfigSync object using the .cfg file specified on CLI or
   'viptela.cfg' will be used as default.
4. Run Example Commands:
    * Get Device info for vedges and controllers
      * Print vedge and controller data using table output in helper function
    * Get all template info
      * Print template info using helper function
    * Get all running-config for vedge and controllers
      * Save vedge and controller info to text file
    
### viptela.py
This file houses all of the viptela related functions.  Any function, whether using 
the SDK or generic REST API calls should be made here.  Put any new functions under 
the ViptelaClient class to fully utilize common elements.  Initializing this class 
only instantiates the object.  You have to call the class function login() to get 
cookies and proper XSRF/CSRF tokens.  

### helpers.py
This file is used to contain all of the functions that manipulate data received.  This 
can be but not limited to saving data to files, printing data to console, exporting 
to CSV or Excel, or just computational functions.  The main purpose of helpers.py 
is to keep config_sync.py cleaner.

### viptela.cfg
All config parameters are kept in the .cfg file currently.  Future iterations will 
include getpass and environmental variable support.  Specify any required variables 
and include any additional variables that may be needed for your project.  This file 
is treated as a YAML file when imported into the application, and then converted to a 
dictionary.  Default configuration is shown below.  Variable names must be exact.
```
---
viptela_host: '198.18.133.200'
viptela_username: 'admin'
viptela_password: 'admin'
viptela_port: 8443
```

Lab guides have been created using Jupyter Labs and are located in the /Labs folder.
Jupyter Labs must be installed using 'pip install jupyterlab'.  Once installed, run the 
application using CLI command 'jupter lab'.  Once Jupyter lab is running 
it will open a browser for you in the project root directory.  Browse the directory in /Labs
to find .ipynb files which are the Jupyter Lab files.  


