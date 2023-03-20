import PySimpleGUI as sg
import zip_extractor as zp
import pathlib

# Variable Declarations

# Zip file Label
source_label = sg.Text('Select Archive', size=(13, 1))

# Zip file Path
source = sg.Input()

# Zip file Source Button
source_button = sg.FileBrowse('Choose', key='-ARCHIVE-')

# File Destination Label
destination_label = sg.Text('Select Destination', size=(13,1))

# File Destination Path
destination = sg.Input()

# File Destination Button
destination_button = sg.FolderBrowse('Choose', key='-DESTINATION-')

# Extract Button
extract = sg.Button('Extract')

# Exit Button
exit = sg.Button('Exit')

# Theme
sg.theme(new_theme='DarkGrey4')

# Text Label
output = sg.Text(key='-OUTPUT-')

# Window Creation
window = sg.Window('File Extraction Application', layout=[[source_label, source, source_button],
                                                          [destination_label, destination, destination_button],
                                                          [extract, exit, output]])

# While Loop to initiate the GUI
while True:
    event, values = window.read()

    # Variable Declaration (to store the paths to the zip file and destination directory)
    archive_path = values['-ARCHIVE-']
    destination_path = values['-DESTINATION-']
    
    # IF user presses on the Extract Button
    if event == 'Extract':
        # Extract archive through function call
        zp.archive_extractor(archive_path, destination_path)

        # Get the name of the file for a clean output
        archive_name = pathlib.Path(archive_path)

        # Update text label and create output statement
        window['-OUTPUT-'].update(value=f"The archive, {archive_name.name}, has been extracted!")

    # Else if user either closes the window or presses Exit
    elif event == sg.WINDOW_CLOSED or event =='Exit':
        break

window.close()