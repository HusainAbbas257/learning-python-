import shutil


# Asking for file path to copy
src_file = 'C:/Users/DELL/Desktop/test'
dst_file = 'C:/Users/DELL/Desktop/example'
try:
    shutil.copy(src_file, dst_file)
    print("File copied successfully.")
except Exception as e:
    print("Error copying file:", e)

# Copy with metadata
src_file = 'C:/Users/DELL/Desktop/test2'
dst_file = 'C:/Users/DELL/Desktop/example2'
try:
    shutil.copy2(src_file, dst_file)
    print("File copied with metadata.")
except Exception as e:
    print("Error copying file with metadata:", e)

# Copy entire directory
src_file = 'C:/Users/DELL/Desktop/test3'
dst_file = 'C:/Users/DELL/Desktop/example3'
try:
    shutil.copytree(src_file, dst_file)
    print("Folder copied successfully.")
except Exception as e:
    print("Error copying folder:", e)

# Move file or folder
src_file = 'C:/Users/DELL/Desktop/test'
dst_file = 'C:/Users/DELL/Desktop/example'
try:
    shutil.move(dst_file,src_file )
    print("Moved successfully.")
except Exception as e:
    print("Error moving file/folder:", e)

# Delete directory
del_dir = 'C:/Users/DELL/Desktop/deleteit'
try:
    shutil.rmtree(del_dir)
    print("Folder deleted successfully.")
except Exception as e:
    print("Error deleting folder:", e)

# Create a zip archive of a folder
folder_to_zip = 'C:/Users/DELL/Desktop/zipit'
zip_name = folder_to_zip +'is zipped'
try:
    archive_path = shutil.make_archive(zip_name, 'zip', folder_to_zip)
    print(f"Folder compressed to: {archive_path}")
except Exception as e:
    print("Error compressing folder:", e)

# Disk usage
path = 'C:/'
try:
    usage = shutil.disk_usage(path)
    print("Disk Usage Info:")
    print("Total:", usage.total, "bytes")
    print("Used:", usage.used, "bytes")
    print("Free:", usage.free, "bytes")
except Exception as e:
    print("Error getting disk usage:", e)
