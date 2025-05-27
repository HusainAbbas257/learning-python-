import json
from datetime import datetime
from decimal import Decimal

# ============================================================================
# CORE JSON OPERATIONS 
# ============================================================================

# json.dump(obj, fp, **kwargs) - Write Python object to file as JSON
# obj: The Python object to convert (dict, list, string, number, bool, None)
# fp: File pointer (opened file object)
# **kwargs: Optional formatting parameters (indent, sort_keys, etc.)
data = {"name": "Husain", "age": 16, "skills": ["Python", "JSON"]}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)  # indent=2 makes it readable (use for config files)

# json.load(fp, **kwargs) - Read JSON from file into Python object
# fp: File pointer (opened file object)
# Returns: Python object (dict, list, etc.)
with open('data.json', 'r') as f:
    loaded = json.load(f)  # Now 'loaded' is a Python dict you can use

# json.dumps(obj, **kwargs) - Convert Python object to JSON string
# obj: The Python object to convert
# Returns: JSON string
# Use this for: API requests, storing in databases, sending over network
json_str = json.dumps(data)              # Dict to JSON string (for sending to APIs)

# json.loads(s, **kwargs) - Parse JSON string into Python object  
# s: JSON string to parse
# Returns: Python object
# Use this for: API responses, reading from databases, receiving data
parsed = json.loads(json_str)            # JSON string back to dict (from API responses)

# Example: API workflow
api_response = '{"status": "success", "data": {"user_id": 123}}'
response_data = json.loads(api_response)  # Parse the API response
user_id = response_data["data"]["user_id"]  # Extract what you need


# indent (int or str): Number of spaces for each indentation level
#   - None (default): Compact, no formatting
#   - int: Number of spaces (2 or 4 recommended)  
#   - str: Use this string for indentation (e.g., '\t' for tabs)


# sort_keys (bool): Whether to sort dictionary keys alphabetically
#   - False (default): Keep original order
#   - True: Sort keys alphabetically


# separators (tuple): Control spacing around separators
#   - (',', ': ') (default): Normal spacing
#   - (',', ':'): Compact, no spaces (saves bandwidth/storage)
#   - When to use: APIs, data transmission, storage optimization
with open("data.json",'w') as file:
    json.dump(data, file, indent=2, sort_keys=True)  # Pretty print with sorted keys
json.dumps(data, separators=(',', ':'))  # Compact - no spaces = smaller file size

# Example: Different use cases
settings = {"theme": "dark", "lang": "en", "notifications": True}

# For config files users might edit manually
with open('settings.json', 'w') as f:
    json.dump(settings, f, indent=4, sort_keys=True)  # Easy to read and edit

# For API responses or data storage  
compact_json = json.dumps(settings, separators=(',', ':'))  # Minimal size


# json.JSONEncoder.default(self, obj) - Override this to handle custom types
# obj: The object that JSON can't normally serialize
# Returns: JSON-serializable version of the object
# Built-in JSON types: str, int, float, bool, None, list, dict
# Must convert: datetime, Decimal, set, tuple, custom classes

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert to ISO string: "2024-01-15T10:30:00"
        if isinstance(obj, Decimal):
            return float(obj)       # Convert to regular float
        if isinstance(obj, (set, tuple)):
            return list(obj)        # Convert to list
        return super().default(obj)  # Let parent handle other types or raise error

# cls parameter: Specify custom encoder class
# json.dumps(obj, cls=CustomEncoder) - Use your custom encoder
# json.dump(obj, file, cls=CustomEncoder) - Same for file writing

# Example: Log entry with timestamp
log_entry = {
    "timestamp": datetime.now(),     # datetime object - normally fails
    "price": Decimal('99.99'),       # Decimal object - normally fails  
    "tags": {"urgent", "api", "bug"} # set object - normally fails
}
json_str = json.dumps(log_entry, cls=JSONEncoder)  # Now it works!
print(json_str)  # {"timestamp": "2024-01-15T10:30:00.123456", "price": 99.99, "tags": ["urgent", "api", "bug"]}

# ============================================================================
# ERROR HANDLING - UNDERSTAND THE EXCEPTION AND ITS ATTRIBUTES
# ============================================================================

# json.JSONDecodeError - Exception raised when JSON parsing fails
# Attributes you need to know:
#   .msg: Human-readable error message
#   .pos: Character position where error occurred  
#   .lineno: Line number of error (in multi-line JSON)
#   .colno: Column number of error

def safe_json_load(text):
    """
    Safely parse JSON string with detailed error information
    Args:
        text (str): JSON string to parse
    Returns:
        tuple: (data, error_message) - data is None if error occurred
    """
    try:
        return json.loads(text), None  # Success: return data and no error
    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON at position {e.pos}: {e.msg}"
        if hasattr(e, 'lineno'):  # Multi-line JSON error details
            error_msg += f" (line {e.lineno}, column {e.colno})"
        return None, error_msg

# Example: Handle bad API response
api_data = '{"name": "test", "value": 123,}'  # Invalid: trailing comma
data, error = safe_json_load(api_data)
if error:
    print(f"API Error: {error}")  # Shows exactly where the problem is
    # Handle the error: retry, use defaults, log, etc.
else:
    print(f"Success: {data}")     # Use the data safely

# ============================================================================
# VALIDATION FUNCTION
# ============================================================================

# Check if JSON file is valid before trying to use it
def validate_json_file(filepath):
    try:
        with open(filepath, 'r') as f:
            json.load(f)  # Try to parse it
        return True       # Success = valid JSON
    except (json.JSONDecodeError, FileNotFoundError):
        return False      # Any error = invalid

# Example: Validate config before loading
if validate_json_file('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)  # Safe to load
else:
    print("Config file is corrupted!")  # Handle the problem

# ============================================================================
# MERGE FUNCTION (USEFUL FOR CONFIGS)
# ============================================================================

# Combine two JSON objects intelligently - useful for updating configs
def merge_json(base, update):
    if isinstance(base, dict) and isinstance(update, dict):
        result = base.copy()  # Don't modify original
        for key, value in update.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_json(result[key], value)  # Recursive merge for nested dicts
            else:
                result[key] = value  # Replace or add new key
        return result
    return update  # If not both dicts, just return the update

# Example: Update app settings
default_settings = {"theme": "light", "features": {"auth": True, "cache": False}}
user_settings = {"theme": "dark", "features": {"cache": True, "notifications": True}}
final_settings = merge_json(default_settings, user_settings)
# Result: {"theme": "dark", "features": {"auth": True, "cache": True, "notifications": True}}

