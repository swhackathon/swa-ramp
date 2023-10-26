import os

def list_folders_in_home():
    # Getting the home directory path for the current user
    home_directory = os.path.expanduser("~")

    try:
        # Listing all items in the home directory
        items_in_home = os.listdir(home_directory)

        # Filtering out only directories from the list of items
        directories = [item for item in items_in_home if os.path.isdir(os.path.join(home_directory, item))]

        # Printing the directories
        for dir_name in directories:
            print(dir_name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_folders_in_home()
    
