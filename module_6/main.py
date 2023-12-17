def write_nested_list_to_file(nested_list, filename):
    with open(filename, 'w') as file:
        for inner_list in nested_list:
            # Join the elements of the inner list into a single string
            line = ', '.join(inner_list)
            # Write the line to the file
            file.write(line + '\n')

# Example nested list
employee_list = [['Robert Stivenson,28'], ['Alex Denver,30'], ['Drake Mikelsson,19']]

# Specify the filename
output_filename = 'output.txt'

# Call the function to write the nested list to the file
write_nested_list_to_file(employee_list, output_filename)