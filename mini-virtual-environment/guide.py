# Virtual Environment in Python
# This script is just a guide with comments. It won’t run but will store how to use virtual environments step-by-step.

# Step 1: Check if venv is available (it's built-in from Python 3.3+)
# Open your terminal or command prompt and run the following command:
# python --version
# If Python 3.3+, you're good to go!

# Step 2: Create a virtual environment
# Syntax: python -m venv <name_of_virtual_env>
# Example:
# python -m venv myenv

# This will create a folder named 'myenv' in your current directory with isolated Python binaries and libraries

# Step 3: Activate the virtual environment
# On Windows:
# myenv\Scripts\activate
# On macOS/Linux:
# source myenv/bin/activate

# You’ll see your terminal prompt change to show that your virtual environment is active. Example:
# (myenv) C:\Users\You>

# Step 4: Install packages inside the virtual environment
# pip install requests
# pip install flask

# These packages are installed locally inside myenv, not globally

# Step 5: Freeze the environment (to share it)
# pip freeze > requirements.txt
# This saves a list of all installed packages so others can recreate the same environment

# Step 6: Recreate environment elsewhere
# python -m venv myenv
# source myenv/bin/activate  (or myenv\Scripts\activate on Windows)
# pip install -r requirements.txt

# Step 7: Deactivate the virtual environment
# deactivate

# That’s it! You now know how to manage a clean, isolated Python environment.
# Great for projects and avoiding conflicts with other packages.

print("This script only provides comments to guide you. Follow the steps in your terminal to practice!")
