import re
import tkinter.messagebox as tk_messagebox
from pathlib import Path
import tkinter as tk

class CheckInput():
    def __init__(check_object, gui_object) -> None:
        check_object.cyklo_or_not = gui_object.cyklo_or_not.strip().lower()
        check_object.chem_formula = gui_object.chem_formula.strip()
        check_object.chem_name = gui_object.chem_name.strip().lower()
        check_object.output_path = gui_object.output_path.strip()
        #if input is correct and not in chemical_dictionary => True in check_object.boolean_list possitions:
        #0 = cyklo_or_not (or False if it is not cyklo), 1 = chem_formula, 2 = chem_name
        check_object.boolean_list = [None, None, None]
        check_object.try_again = 0


    def check_gui_output(check_object, chem_object):
        if check_object.cyklo_or_not == "no" or check_object.chem_name in chem_object.basic_list or check_object.chem_name in chem_object.non_basic_list or check_object.chem_name in chem_object.non_non_basic_list:
            check_object.boolean_list[0] = False
            check_object.cyklo_or_not = "no"
        elif check_object.cyklo_or_not == "yes" or check_object.chem_name in chem_object.cyklo_list or check_object.chem_name in chem_object.cyklo_non_basic_list or check_object.chem_name in chem_object.cyklo_non_non_basic_list:
            check_object.boolean_list[0] = True
            check_object.cyklo_or_not = "yes"

        if check_object.chem_name != "":
            check_object.boolean_list[2] = True
        
        CheckInput.try_except_block(check_object, chem_object)

        if check_object.boolean_list[0] == None or check_object.boolean_list[1] == None and check_object.boolean_list[2] == None:
            tk_messagebox.showerror(
                title="Not enough details!", message="Please enter more details.")
            return
        
        if check_object.chem_name in chem_object.basic_list or check_object.chem_name in chem_object.non_basic_list or check_object.chem_name in chem_object.non_non_basic_list and check_object.cyklo_or_not == "yes":
            tk_messagebox.showerror(
                title="Bad details!", message="Please enter valid cyklo details.")
            return
        elif check_object.chem_name in chem_object.cyklo_list or check_object.chem_name in chem_object.cyklo_non_basic_list or check_object.chem_name in chem_object.cyklo_non_non_basic_list and check_object.cyklo_or_not == "no":
            tk_messagebox.showerror(
                title="Bad details!", message="Please enter valid noncyklo details.")
            return
        """
        if check_object.chem_formula == "" and check_object.chem_name == "":
            tk_messagebox.showerror(
                title="Empty Input!", message="Please enter Chemical_Formula or Name_of_Compound.")
            return
        """
        if check_object.chem_formula == "" and check_object.chem_name not in chem_object.list_of_keys:
            tk_messagebox.showerror(
                title="Invalid Input!", message="Please enter a valid Chemical_Formula.")
            return
        elif check_object.chem_formula == "" and check_object.chem_name in chem_object.list_of_keys:
            check_object.chem_formula = chem_object.chemical_dictionary[check_object.chem_name]
        
        if check_object.chem_name == "" and check_object.chem_formula not in chem_object.list_of_values:
            tk_messagebox.showerror(
                title="Invalid Input!", message="Please enter a valid Name_of_Compound.")
            return
        elif check_object.chem_name == "" and check_object.chem_formula in chem_object.list_of_values:
            check_object.chem_name = chem_object.list_of_keys[chem_object.list_of_values.index(check_object.chem_formula)]

        if check_object.output_path == "":
            tk_messagebox.showerror(
                title="Invalid Path!", message="Enter a valid output path.")
            return
            
        output = Path(check_object.output_path + "/chem").expanduser().resolve()

        if output.exists() and not output.is_dir():
            tk_messagebox.showerror(
                "Exists!",
                f"{output} already exists and is not a directory.\n"
                "Enter a valid output directory.")
        elif output.exists() and output.is_dir() and tuple(output.glob('*')):
            response = tk_messagebox.askyesno(
                "Continue?",
                f"Directory {output} is not empty.\n"
                "Do you want to continue and overwrite?")
            if not response:
                return

        if check_object.try_again == 1:
            CheckInput.try_except_block(check_object, chem_object)

        if check_object.boolean_list[0] != None:
            chem_object.cyklo_or_not = check_object.cyklo_or_not     
        if check_object.boolean_list[1] != None:
            chem_object.chem_formula = check_object.chem_formula
        if check_object.boolean_list[2] != None:
            chem_object.chem_name = check_object.chem_name
        chem_object.output_path = check_object.output_path
        return


    def try_except_block(check_object, chem_object):
        try:
            if check_object.chem_formula != "" and check_object.chem_formula[len(check_object.chem_formula) - 1] == "-" or check_object.chem_formula[len(check_object.chem_formula) - 1] == "=" or check_object.chem_formula[len(check_object.chem_formula) - 1] == "/" and check_object.cyklo_or_not == "yes":
                check_object.boolean_list[1] = True

            elif check_object.chem_formula != "" and check_object.chem_formula[len(check_object.chem_formula) - 1] != "-" and check_object.chem_formula[len(check_object.chem_formula) - 1] != "=" and check_object.chem_formula[len(check_object.chem_formula) - 1] != "/" and check_object.cyklo_or_not == "yes":
                if check_object.chem_formula + "-" == chem_object.chemical_dictionary[check_object.chem_name]:
                    check_object.chem_formula = check_object.chem_formula + "-"
                elif check_object.chem_formula + "=" == (chem_object.chemical_dictionary[check_object.chem_name]):
                    check_object.chem_formula = check_object.chem_formula + "="
                elif check_object.chem_formula + "/" == (chem_object.chemical_dictionary[check_object.chem_name]):
                    check_object.chem_formula = check_object.chem_formula + "/"
                check_object.boolean_list[1] = True

            elif check_object.chem_formula != "" and check_object.chem_formula[len(check_object.chem_formula) - 1].isalpha() or check_object.chem_formula[len(check_object.chem_formula) - 1].isnumeric() and check_object.cyklo_or_not == "yes":
                check_object.boolean_list[1] = True
            check_object.try_again = 0
        except IndexError:
            check_object.try_again = check_object.try_again + 1
        except KeyError:
            pass