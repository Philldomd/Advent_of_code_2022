def fileReader(input_path):
    try:
        return open(input_path,'r')
    except FileNotFoundError:
        print("File not found exception: ",input_path)
    except NameError:
        print("Could not evaluate input path, not correct name: ",input_path)

def fileWriter(output_path):
    try:
        return open(output_path,'x')
    except FileNotFoundError:
        print("File not found exception: ",output_path)
    except NameError:
        print("Could not evaluate input path, not correct name: ",output_path)
    except FileExistsError:
        print("Could not create file: ",output_path," file already exists")
