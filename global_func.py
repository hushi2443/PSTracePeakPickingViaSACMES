#!/usr/bin/env python3

from config import cg

########################
# Global Functions ###
########################


##############################
# Retrieve the file name ###
##############################
def _retrieve_file(file, electrode, frequency):
    try:
        if cg.method == "Continuous Scan":

            if cg.e_var == "single":
                filename = "%s%dHz_%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename2 = "%s%dHz__%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename3 = "%s%dHz_#%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename4 = "%s%dHz__#%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )

            elif cg.e_var == "multiple":
                filename = "E%s_%s%sHz_%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename2 = "E%s_%s%sHz__%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename3 = "E%s_%s%sHz_#%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename4 = "E%s_%s%sHz__#%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )

            return filename, filename2, filename3, filename4

        if cg.method == "Frequency Map":

            if cg.e_var == "single":
                filename = "%s%dHz%s" % (cg.handle_variable, frequency, cg.extension)
                filename2 = "%s%dHz_%s" % (cg.handle_variable, frequency, cg.extension)
                filename3 = "%s%dHz_%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename4 = "%s%dHz__%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename5 = "%s%dHz_#%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename6 = "%s%dHz__#%d%s" % (
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )

            elif cg.e_var == "multiple":
                filename = "E%s_%s%sHz%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    cg.extension,
                )
                filename2 = "E%s_%s%sHz_%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    cg.extension,
                )
                filename3 = "E%s_%s%sHz_%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename4 = "E%s_%s%sHz__%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename5 = "E%s_%s%sHz_#%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )
                filename6 = "E%s_%s%sHz__#%d%s" % (
                    electrode,
                    cg.handle_variable,
                    frequency,
                    file,
                    cg.extension,
                )

            return filename, filename2, filename3, filename4, filename5, filename6
    except Exception:
        print("\nError in retrieve_file\n")


def ReadData(myfile, electrode):

    try:
        ###############################################################
        # Get the index value of the data depending on if the     ###
        # electrodes are in the same .txt file or separate files  ###
        ###############################################################
        if cg.e_var == "single":
            cg.list_val = cg.current_column_index + (electrode - 1) * cg.spacing_index
        elif cg.e_var == "multiple":
            cg.list_val = cg.current_column_index
        #print("a")
        #####################
        # Read the data ###
        #####################
        try:
            # ---Preallocate Potential and Current lists---#
            print("Attempting to open file:", myfile)
            with open(myfile, "r", encoding="utf-16") as mydata:
                print("File opened successfully.")
                cg.encoding = "utf-16"
                #print("g")
                file_contents = mydata.read()  # Read the entire file contents for debugging
                #print("File contents length:", len(file_contents))  # Print the length of the file contents
                #print("First 100 characters of file contents:", file_contents[:100])  # Print the first 100 characters
                variables = len(file_contents.splitlines())  # Count the number of lines in the file
                #print("Number of lines in the file:", variables)
                potentials = ["hold"] * variables
                data_dict = {}
                currents = [0] * variables
            #print("b")
        except Exception:
            # ---Preallocate Potential and Current lists---#
            #print("b1")
            with open(myfile, "r", encoding="utf-8") as mydata:
                #print("b2")
                cg.encoding = "utf-8"
                print("b3")

                file_contents = mydata.read()  # Read the entire file contents for debugging
                print("File contents length:", len(file_contents))  # Print the length of the file contents
                print("First 100 characters of file contents:", file_contents[:100])  # Print the first 100 characters
                variables = len(file_contents.splitlines()) 
                #print(variables)
                #variables = len(mydata.readlines())
                #print(variables)
                #print("b4")
                potentials = ["hold"] * variables
                #print("b5")
                # key: potential; value: current ##
                data_dict = {}
                #print("b6")
                print(variables)
                currents = [0] * variables
                #print("b7")
            print("c")


        # ---Extract data and dump into lists---#
        with open(myfile, "r", encoding=cg.encoding) as mydata:
            list_num = 0
            print("c1")
            for line in mydata:
                check_split_list = line.split(cg.delimiter)
                print("c2")
                # delete any spaces that may come before the first value #
                while True:
                    if check_split_list[0] == "":
                        del check_split_list[0]
                        print("c3")
                    else:
                        break

                # delete any tabs that may come before the first value #
                while True:
                    print("c4")
                    if check_split_list[0] == " ":
                        del check_split_list[0]
                        print("c5")
                    else:
                        break
                print("c6")
                check_split = check_split_list[0]
                check_split = check_split.replace(",", "")
                print("c7")
                try:
                    check_split = float(check_split)
                    print("c8")
                    check_split = True
                    print("c9")
                except Exception:
                    print("c10a")
                    check_split = False
                    print("c10")
                if check_split:
                    # ---Currents---#
                    print("c11")
                    print(check_split_list)
                    print(cg.list_val)
                    print("c11")
                    print("cg.list_val:", cg.list_val)
                    print("check_split_list:", check_split_list)

                    # Check if cg.list_val is an integer
                    print("Is cg.list_val an integer?", isinstance(cg.list_val, int))

                    # Check if cg.list_val is within the range of check_split_list
                    print("Is cg.list_val within range of check_split_list?", 0 <= cg.list_val < len(check_split_list))

                    if check_split:
                        try:
                            current_value = check_split_list[cg.list_val]  # list_val is the index value of the given electrode
                            print("c12")
                            current_value = current_value.replace(",", "")
                            print("c13")
                        except Exception as e:
                            print("An error occurred:", e)

                    current_value = check_split_list[cg.list_val]  # list_val is the index value of the given electrode
                    print("c12")
                    current_value = current_value.replace(",", "")
                    print("c13")
                    current_value = float(current_value)
                    print("c14")
                    current_value = current_value * 1000000
                    print("c15")
                    currents[list_num] = current_value
                    print("c16")
                    # ---Potentials---#
                    potential_value = line.split(cg.delimiter)[cg.voltage_column_index]
                    print("c17")
                    potential_value = potential_value.strip(",")
                    print("c18")
                    potential_value = float(potential_value)
                    print("c19")
                    potentials[list_num] = potential_value
                    print("c20")
                    data_dict.setdefault(potential_value, []).append(current_value)
                    print("c21")
                    list_num = list_num + 1
        print("d")
        # if there are 0's in the list (if the preallocation added to many)
        # then remove them
        cut_value = 0
        for value in potentials:
            if value == "hold":
                cut_value += 1
        print("e")
        if cut_value > 0:
            potentials = potentials[:-cut_value]
            currents = currents[:-cut_value]
        print("f")
        #######################
        # Return the data ###
        #######################
        return potentials, currents, data_dict
    except Exception:
        print("\nError in ReadData()\n")


#######################################
# Retrieve the column index value ###
#######################################
def _get_listval(electrode):
    try:
        if cg.e_var == "single":
            cg.list_val = cg.current_column_index + (electrode - 1) * cg.spacing_index

        elif cg.e_var == "multiple":
            cg.list_val = cg.current_column_index

            return cg.list_val
    except Exception:
        print("\nError in _get_listval\n")
