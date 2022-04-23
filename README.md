# Viptela ConfigSync

## Overview
Viptela ConfigSync is a common framework being developed intended to give a 
standards based approach to working with REST API for configuration tasks with 
network equipment.  ConfigsSync already includes argument parsing from the CLI,
logging facilities, and a config file parser.  It also comes pre-built with a 
few functions to serve as examples on building new purposes for the tool.  

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

## Running Viptela ConfigSync

Steps to run the ConfigSync application are listed below.

1. Copy it locally to your computer.  You can 
download the .zip file from Github or install using 'git clone'.  This will create a subdirectory 
whereever you run it called 'Viptela-ConfigSync'.

```buildoutcfg
git clone https://github.com/tc45/Viptela-ConfigSync.git
```

2. Edit and update the connection parameters in the config file as necessary.
```
---
viptela_host: '198.18.133.200'
viptela_username: 'admin'
viptela_password: 'admin'
viptela_port: 8443
```

3. Launch config_sync.py from the command line.

```buildoutcfg
python config_sync.py
```

4.  Use CLI arguments to change behavior of the app.

```buildoutcfg
(venv) C:\PycharmProjects\Viptela-ConfigSync>python config_sync.py --help
usage: config_sync.py [-h] [--config CONFIG] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Path to the configuration file
  --debug, -d           Display debug logs


```

## Lab Info

The lab has been written to work with Cisco Dcloud out of the box.  It can also be ran on
Cisco DevNetSandbox with minimal modifications to the .cfg file. 

### Steps for running on Cisco Dcloud

1. Reserve a Dcloud session for Cisco SD-WAN POC Tool
Once logged into https://dcloud.cisco.com.
   
2. Click Catalog, and search for 'SD-WAN POC'.  This will bring you to a 
   series of Viptela SD-WAN sessions.  Cisco changes the revisions frequently, so use whatever is most current.  
   
3. Reserve the lab and wait for session to show active.  

4.  You can access the lab using Cisco AnyConnect VPN.  The credentials will be under the 'Details' heading when viewing the 
dcloud session.  Login using the specified host/port, username, and password.
    
5.  Once logged in you can either run the application on your host PC, or use the Jumpbox. All other steps are the same.

6.  (optional) - Login to the Jumphost using MS Terminal Services client (Start -> Run -> mstsc) on Windows. Enter IP 
'198.18.133.36'.  This IP may change in the future, so be sure to check dcloud for updates.  Username is admin.  
    Password is C1sco12345.
    
7. Go to starting directory (personal choice) and clone the Viptela ConfigSync github repository.

```commandline
cd c:\Users\Admin\PythonProjects\

git clone https://github.com/tc45/Viptela-ConfigSync.git

cd Viptela-ConfigSync
```

8. Run the application.  Debug is optional.

```commandline
python config-sync.py --debug
```

## Learning More 
To learn more about how to build new modules for this app, or are just curious, check out the Lab guides.
Lab guides have been created using Jupyter Labs and are located in the /Labs folder.
Jupyter Labs must be installed using 'pip install jupyterlab'.  Once installed, run the 
application using CLI command 'jupyter lab'.  Once Jupyter lab is running 
it will open a browser for you in the project root directory.  Browse the directory in /Labs
to find .ipynb files which are the Jupyter Lab files.  

1.  Install Jupyter Labs using pip

```commandline
pip install jupyterlab
```

2. Launch Jupyter Lab.  This will open a browser to the starting URL.  A link will also be displayed in the CLI.

```commandline
jupyter lab
```

3.  Locate the lab you want to do using the file explorer window.  Jupyter Lab files end in 
.ipynb
    
4.  Follow instructions in the lab





