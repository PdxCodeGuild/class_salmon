# Radio Utilities for Python (RUPy)

## What does it do?
The libray contains 3 files:
- gps.py
- wl2k.py
- rupy.py

The goal is to interface with the Winlink Express radio-over-high frequency radio email program and provide a means
of updating station information when off-grid or otherwise in an unconnected environment.  There is an excellent library
for handling GPS functions called gpsd, however it is not available for Windows.  As a result, functionality had to be 
developed from scratch.

### gps.py
This file contains functions that allow a user to connect to an external GPS device and gather information,
including speed, heading, time, and of course, GPS information.  It also contains functions for converting GPS
coordinates into Maidenhead grid squares and vice-versa.  Finally, this can also check the Winlink Express configuration
file to determine what grid square is currently set.  This code will work with any serial GPS device that follows the 
NMEA 0183 format.  Some devices, such as the inexpensive Ublox-based units, will **NOT** work.

#### Functions:

- *get_current_grid_square()*: Takes no arguments.  Checks the existing Winlink config file and returns the current 
  Maindenhead grid square.
  
- *get_gps_coordinates()*: Takes the connected GPS unit's COM port as the only argument.  If no port is specified, it uses
  the default of COM7.
  
- *convert_to_grid()*: Takes a coordinate pair (lattitude & longintude), coverts to a 6-character Maindehead grid square and 
  returns the value.
  
- *convert_to_latlon()*:  Takes a 6-character grid square and converts that to a set of decimal coordinates.  Note that because 
  of the design of the Maidenhead system, GPS coordinates returned will always represent the center point of the grid square.
  
- *get_geo_distance()*: This takes 2 6-character grid squares and calculates the distance (in miles) between the center point
  of each grid square.
  
#### Usage:
```
    # Get current grid square:
    get_current_grid_square()
    
    # Get coordinates from the GPS unit:
    get_gps_coordinates('COM7')
    
    # Convert coordinates to grid square:
    lat = 47.28486807633567 
    lon = -122.37259876762998
    convert_to_grid(lat, lon)
    
    # Find the distance between 2 grid squares
    grid1 = 'CN87tg'
    grid2 = 'CN85qm'
    get_geo_distance(gird1, grid2)
```

### wl2k.py
This file contains functions specifically for interacting with the Winlink Express web API and the application config file
directly.  It enables dynamic updates based on current GPS position without having to open Winlink directly.  It also provides access
to the local list of WInlink nodes.

#### Functions:
- *update_winlink_config()*: Requires a 6-character Maidenhead grid square and replaces the current one in the Winlink Express
  config.
  
- *update_winlink_node_list()*: Will generate an updated list of Winlink Express nodes.  Requires standard internet access to run
  however the resulting data is stored in the data folder as a CSV that can be accessed offline.

- *get_close_nodes*: Utilizing the local CSV file, returns a list of all Winlink nodes from the closest to the farthest.

- *get_close_nodes_by_mode*: Utilizing the local CSV file, will supply a list of the 25 closest nodes in a given mode. The
  mode is supplied as an integer number representing the mode as described in the Winlink documentation.
  
#### Usage:
```
    # Update winlink to current grid square:
    gridsq = 'CN87tg'
    update_winlink_config(grid_sq)
    
    # update Winlink node list:
    update_winlink_node_list()
    
    # get all nodes:
    gridsq = 'CN87tg'
    get_close_nodes(grid_sq)
    
    # get close nodes by mode:
    mode = 51  # 51 is the mode for VARA FM
    get_close_nodes_by_mode(mode)
```

### rupy.py
This is the demo script.  Running it requires Winlink Express be installed.  For full functionality, a serial GPS is also required.

### Libraries Used
#### Standard Python libraries required:
- os: For building file paths
- requests: for use with the Winlink Express API.
- shutil: for creating and deleting files.
- csv: for creating the csv file.
- serial: for accessing the GPS via serial port operations.

#### Non-standard libraries required:
- pynmeagps: for interpreting data sent from the GPS unit.
- geopy: for calculating the distance between 2 grid squares.

### Further development:
#### Planned features, in development
- Storing node information in a database instead of CSV.
- Allowing user to configure ports and file paths at first run/installation
- Syncing system clock to GPS clock

#### Planned features, not yet implemented:
- Web server: for remote access to the system without requiring a computer
- Full send/receive capabilities: sending and receiving email without having to use the Winlink client
- Generate a list of the closest nodes for all modes.

