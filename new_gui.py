import webbrowser
import sys
import os
import tkinter as tk

import tkinter.filedialog
from pathlib import Path

# Add tkdesigner to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Path to asset files for this GUI gui_object.root.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

# Required in order to add data files to roots executable
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

class MyGui():  
    def __init__(gui_object) -> None:
        try:
            gui_object.chem_formula = chem_formula.get()
        except:
            gui_object.chem_formula = ""
        try:
            gui_object.chem_name = chem_name.get()
        except:
            gui_object.chem_name = ""
        try:
            gui_object.cyklo_or_not = cyklo_or_not.get()
        except:
            gui_object.cyklo_or_not = ""   
        try:    
            gui_object.output_path = output_path
        except:
            gui_object.output_path = ""
        gui_object.root.destroy()
   

    def know_more_clicked(gui_object):
        instructions = "https://www.google.cz/search?q="
        webbrowser.open_new_tab(instructions)


    def select_path():
        global output_path
        output_path = tk.filedialog.askdirectory()
        path_entry.delete(0, tk.END)
        path_entry.insert(0, output_path)


    def first_root(gui_object):
        gui_object.root = tk.Tk()

        logo = tk.PhotoImage(file=ASSETS_PATH / "logo_chem_program.png")
        gui_object.root.call('wm', 'iconphoto', gui_object.root._w, logo)
        gui_object.root.title("Chemical program")
        gui_object.root.geometry("862x519")
        gui_object.root.configure(bg="#3A7FF6")        
        
        canvas = tk.Canvas(
            gui_object.root, bg="#fac618", height=519, width=862,
            bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#000000", outline="")
        canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#fac618", outline="")

        text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
        cyklo_or_not_img = canvas.create_image(650.5, 126.5, image=text_box_bg)
        Chemical_Formula_img = canvas.create_image(650.5, 207.5, image=text_box_bg)
        Name_of_Compound_img = canvas.create_image(650.5, 288.5, image=text_box_bg)
        filePath_entry_img = canvas.create_image(650.5, 369.5, image=text_box_bg)
                
        global cyklo_or_not
        cyklo_or_not = tk.StringVar()
        cyklo_or_not_entry = tk.Entry(bd=0, bg="#fafafa", highlightthickness=0, text="yes/no", textvariable=cyklo_or_not)
        cyklo_or_not_entry.place(x=490.0, y=96+25, width=321.0, height=35)

        global chem_formula
        chem_formula = tk.StringVar()
        Chemical_Formula = tk.Entry(bd=0, bg="#fafafa", highlightthickness=0, textvariable=chem_formula)
        Chemical_Formula.place(x=490.0, y=177+25, width=321.0, height=35)

        global chem_name
        chem_name = tk.StringVar()
        Name_of_Compound = tk.Entry(bd=0, bg="#fafafa", highlightthickness=0, textvariable=chem_name)
        Name_of_Compound.place(x=490.0, y=258+25, width=321.0, height=35)

        global path_entry
        path_entry = tk.Entry(bd=0, bg="#fafafa", highlightthickness=0)
        path_entry.place(x=490.0, y=339+25, width=321.0, height=35)

        path_picker_img = tk.PhotoImage(file = ASSETS_PATH / "path_picker.png")
        path_picker_button = tk.Button(
            image = path_picker_img,
            text = '',
            compound = 'center',
            fg = 'white',
            borderwidth = 0,
            highlightthickness = 0,
            command = MyGui.select_path,
            relief = 'flat')

        path_picker_button.place(
            x = 783, y = 359,
            width = 24,
            height = 22)

        canvas.create_text(
            490.0, 82.0, text="Cyklo or Not", fill="#fafafa",
            font=("Arial-BoldMT", int(13.0)), anchor="w")
        canvas.create_text(
            490.0, 165.0, text="Chemical Formula", fill="#fafafa",
            font=("Arial-BoldMT", int(13.0)), anchor="w")
        canvas.create_text(
            490.0, 247.0, text="Name of Compound", fill="#fafafa",
            font=("Arial-BoldMT", int(13.0)), anchor="w")
        canvas.create_text(
            490.0, 328.0, text="Output Path",
            fill="#fafafa", font=("Arial-BoldMT", int(13.0)), anchor="w")

        canvas.create_text(
            615.5, 40.0, text="Please enter the details.",
            fill="#fafafa", font=("Arial-BoldMT", int(22.0)))

        title = tk.Label(
            text="Welcome to Chemical program", bg="#fac618",
            fg="white", font=("Arial-BoldMT", int(20.0)))
        title.place(x=27.0, y=20.0)

        title = tk.Label(
            text="Basic offer:", bg="#fac618",
            fg="white", font=("Arial-BoldMT", int(16.0)))
        title.place(x=27.0, y=70.0)

        info_text = tk.Label(
            text="Names of Compounds: " + "\n" +
            str(gui_object.chem_object.basic_list) + "\n" +
            str(gui_object.chem_object.non_basic_list) + "\n" +
            str(gui_object.chem_object.non_non_basic_list) + "\n" +
            str(gui_object.chem_object.cyklo_list) + "\n" +
            str(gui_object.chem_object.cyklo_non_basic_list) + "\n" +
            str(gui_object.chem_object.cyklo_non_non_basic_list) + "\n" +
            "\n" +
            "Chemical Formulas: " + "\n" +
            str(gui_object.chem_object.v_basic_list[0] + "    " + gui_object.chem_object.v_basic_list[5]) + "\n" +
            str(gui_object.chem_object.v_non_basic_list[0] + "    " + gui_object.chem_object.v_non_basic_list[4]) + "\n" +
            str(gui_object.chem_object.v_non_non_basic_list[0]) + "\n" +
            str(gui_object.chem_object.v_cyklo_list[0] + "    " +  gui_object.chem_object.v_cyklo_list[3]) + "\n" +
            str(gui_object.chem_object.v_cyklo_non_basic_list[0] + "    " +  gui_object.chem_object.v_cyklo_non_basic_list[3]) + "\n" +
            str(gui_object.chem_object.v_cyklo_non_non_basic_list[0]) + "\n" +
            "\n" +
            "This GUI was created\n"
            "using Tkinter Designer.",
            bg="#fac618", fg="white", justify="left",
            font=("Georgia", int(12.0)))

        info_text.place(x=27.0, y=100.0)
        """
        "Chemical program uses python turtle\n"
        "to draw chemical structures of organic\n"
        " compounds.\n\n"

        """        
        know_more = tk.Label(
            text="Click here for Github source code",
            bg="#fac618", fg="white", cursor="hand2")
        know_more.place(x=27, y=450)
        know_more.bind('<Button-1>', MyGui.know_more_clicked)

        generate_btn_img = tk.PhotoImage(file=ASSETS_PATH / "generate.png")
        button = tk.Button(
            gui_object.root, image=generate_btn_img, text="Get Chem", borderwidth=0,
            highlightthickness=0, font=40, command=lambda: MyGui.__init__(gui_object), relief="flat")
        button.place(x=557, y=421, width=180, height=55)

        gui_object.root.resizable(False, False)
        gui_object.root.mainloop()