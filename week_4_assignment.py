def file_manipulation_rw():
   
    file_name = input("Enter the name of the file to read: ")

    try:
        
        with open(file_name, "r") as file:
            file_content = file.read()   

        modified_content = file_content.upper()

        output_filename = "modified_" + file_name

        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n Success! Modified content saved to '{output_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_name}' was not found.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read '{file_name}'.")
    except Exception as e:
        
        print(f"Unexpected error: {e}")


file_manipulation_rw()
