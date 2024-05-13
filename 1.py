import os
#1
def list_contents(path):
    try:
       
        if not os.path.exists(path):
            print("Error: The specified path does not exist.")
            return
        
       
        if not os.path.isdir(path):
            print("Error: The specified path is not a directory.")
            return

        
        print(f"Contents of directory '{path}':")
        for item in os.listdir(path):
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")

path=input("please enter directory path")
list_contents(path)

#2

def report_file_sizes(directory):
    try:
        
        if not os.path.exists(directory):
            print("Error: The specified directory does not exist.")
            return
        
        
        if not os.path.isdir(directory):
            print("Error: The specified path is not a directory.")
            return

        
        print(f"Files in directory '{directory}':")
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):  
                size = os.path.getsize(item_path)
                print(f"Name: {item}, Size: {size} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = input("Enter the directory path: ")


report_file_sizes(directory_path)


#3

def count_file_extensions(directory):
    try:
        
        if not os.path.exists(directory):
            print("Error: The specified directory does not exist.")
            return
        
        
        if not os.path.isdir(directory):
            print("Error: The specified path is not a directory.")
            return

        
        extension_counts = {}

        
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):  
                _, extension = os.path.splitext(item)
                extension = extension.lower()  
                if extension not in extension_counts:
                    extension_counts[extension] = 1
                else:
                    extension_counts[extension] += 1

        
        print("Number of files by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = input("Enter the directory path: ")


count_file_extensions(directory_path)
