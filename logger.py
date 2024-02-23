import datetime

def export_log(module_name, message):
    file_name = make_logpath(module_name, "txt")
    save_file(file_name, message)

def save_file(file_name, content):
    # Open the file in write mode
    with open(file_name, "w") as file:
        # Write the content to the file
        file.write(content)

    # Print the file name
    print(f"file saved to {file_name}")

def make_logpath(module_name, extension):
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time as YYYY-MM-DD-HH-MM-SS
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")

    # Create the file name with the module name, timestamp, and extension
    file_name = f"outputs/{module_name}_{timestamp}.{extension}"

    return file_name
