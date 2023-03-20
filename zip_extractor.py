# Import Statements
import zipfile 

# Function Declarations
def archive_extractor(archive_path, destination):
    with zipfile.ZipFile(archive_path) as zf:
        
        # Extracting ALL files of the zip file (provided through its path in archive_path) to a 
        # destination directory
        zf.extractall(destination)