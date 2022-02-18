from new_gui import MyGui
from chemical_program import ChemProgram
from check_input import CheckInput

import tkinter.messagebox as tk_messagebox

def main():
    chem_object = ChemProgram()
    ChemProgram.split_chem(chem_object)

    gui_object = MyGui.__init__
    gui_object.chem_object = chem_object
    MyGui.first_root(gui_object)
    try:
        print(gui_object.chem_formula)
        print(gui_object.chem_name)
        print(gui_object.cyklo_or_not)
        print(gui_object.output_path)
            
        check_object = gui_object
        CheckInput.__init__(check_object, gui_object)
        CheckInput.check_gui_output(check_object, chem_object)
        print(check_object.boolean_list)
            
        ChemProgram.my_chemical_list(chem_object)
        if check_object.boolean_list[0] == False:
            ChemProgram.turtle_writer(chem_object)
        elif check_object.boolean_list[0] == True:
            ChemProgram.cyklo_turtle(chem_object)
        ChemProgram.find_online(chem_object)

    except AttributeError:
        tk_messagebox.showerror(
            title="Something went wrong!", message="Please try it again.")
        return
    
    ChemProgram.save_image(chem_object)

main()
