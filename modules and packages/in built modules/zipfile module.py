
import zipfile
import os
import datetime


# ============================================================================
#  BASIC ZIP FILE CREATION AND READING
# ============================================================================


    
# Create sample files first (you need something to zip)
os.makedirs('sample_files')
    
# Write some test files
with open('sample_files/readme1.txt', 'w') as f:
    f.write("This is a sample readme1 file.")
    
with open('sample_files/readme2.txt', 'w') as f:
    f.write("This is a sample readme2 file.")
    
    
# METHOD 1: write() - Add files to zip
print("=== CREATING ZIP FILE ===")
with zipfile.ZipFile('example_basic.zip', 'w') as zipf:
    # write(filename, arcname=None, compress_type=None, compresslevel=None)
    # filename: file to add
    # arcname: name inside zip (optional)
    # compress_type: compression method
    # compresslevel: compression level 
        
    zipf.write('sample_files/readme1.txt', 'docs/readme1.txt')  # Store with different path
    zipf.write('sample_files/readme2.txt')  # Store with same name
        
    # Add string data directly using writestr(file name,data)
    zipf.writestr('generated/info.txt', 'This file was created by writestr()!')
    zipf.writestr('generated/timestamp.txt', f'Created on: {datetime.datetime.now()}')
    
print("Basic zip created: example_basic.zip")


print("\n=== READING ZIP CONTENTS ===")
    
with zipfile.ZipFile('example_basic.zip', 'r') as zipf:
        
    # METHOD: namelist() - Get list of all file names
    print("Files in zip:")
    file_list = zipf.namelist()
    for filename in file_list:
        print(f" example_basic\{filename}")
        
    # METHOD: infolist() - Get detailed info about each file
    print("\nDetailed file information:")
    for file_info in zipf.infolist():
        print(f"\t{file_info.filename}")
        print(f"\tSize: {file_info.file_size} bytes")
        print(f"\tCompressed: {file_info.compress_size} bytes")
        print(f"\tModified: {datetime.datetime(*file_info.date_time)}")
        
    # METHOD: getinfo(file name) - Get info about specific file
    print("\nSpecific file info:")
    readme_info = zipf.getinfo('docs/readme1.txt')
    print(f"Readme1 file size: {readme_info.file_size} bytes")


    
print("\n=== EXTRACTING FILES ===")
    
with zipfile.ZipFile('example_basic.zip', 'r') as zipf:
        
    # METHOD: extractall(path) - Extract everything to path
    print("Extracting all files to 'extracted_all/'")
    zipf.extractall('extracted_all')
        
    # METHOD: extract(member,path) - Extract specific file(member) to path
    print("Extracting specific file to 'extracted_single/'")
    os.makedirs('extracted_single')
    zipf.extract('docs/readme1.txt', 'extracted_single')
        
    # METHOD: read() - Read file content as bytes (without extracting)
    print("Reading file content directly:")
    content = zipf.read('docs/readme1.txt')
    print(f"Content: {content.decode('utf-8')}")
        
    # METHOD: open() - Open file-like object
    print("Opening file as file-like object:")
    with zipf.open('generated/info.txt') as file:
        content = file.read().decode('utf-8')
        print(f"Generated file says: {content}")



print("\n=== ZIP FILE ANALYSIS ===")
    
with zipfile.ZipFile('example_basic.zip', 'r') as zipf:
        
    # METHOD: is_zipfile(filename) - Check if file is valid zip (static method)
    print(f"Is valid zip file: {zipfile.is_zipfile('example_basic.zip')}")
        
    # METHOD: testzip() - Test zip file integrity
    bad_file = zipf.testzip()
    if bad_file:
        print(f"Corrupted file found: {bad_file}")
    else:
        print("All files in zip are valid")        
    
