from string import ascii_lowercase
import turtle as t
import os
from tkinter import *
import tkinter.messagebox as tk_messagebox
import convertapi

class ChemProgram():
    def __init__(chem_object) -> None:
        chem_object.chemical_list = [[]]
        chem_object.position_chars = []
        chem_object.chem_name = ""
        chem_object.cyklo_or_not = ""
        chem_object.basic_list = []
        chem_object.non_basic_list = []
        chem_object.non_non_basic_list = []
        chem_object.cyklo_list = []
        chem_object.cyklo_non_basic_list = []
        chem_object.cyklo_non_non_basic_list = []
        chem_object.v_basic_list = []
        chem_object.v_non_basic_list = []
        chem_object.v_non_non_basic_list = []
        chem_object.v_cyklo_list = []
        chem_object.v_cyklo_non_basic_list = []
        chem_object.v_cyklo_non_non_basic_list = []
        chem_object.list_of_keys = []
        chem_object.list_of_values = []
        chem_object.chemical_dictionary = {
            "methan": "H4C", "ethan": "H3C-CH3", "propan": "H3C-CH2-CH3", "butan": "H3C-CH2-CH2-CH3", "pentan": "H3C-CH2-CH2-CH2-CH3", "hexan": "H3C-CH2-CH2-CH2-CH2-CH3",        #basic
            "ethen": "H2C=CH2", "propen": "H2C=CH-CH3", "buten": "H2C=CH-CH2-CH3", "penten": "H2C=CH-CH2-CH2-CH3", "hexen": "H2C=CH-CH2-CH2-CH2-CH3",                            #non_basic
            "ethyn": "HC/CH",                                                                                                                                                    #non_non_basic
            "cyklopropan": "H2C-CH2-CH2-", "cyklobutan": "H2C-CH2-CH2-CH2-", "cyklopentan": "H2C-CH2-CH2-CH2-CH2-", "cyklohexan": "H2C-CH2-CH2-CH2-CH2-CH2-",                    #cyklo
            "cyklopropen": "HC=CH-CH2-", "cyklobuten": "HC=CH-CH2-CH2-", "cyklopenten": "HC=CH-CH2-CH2-CH2-", "cyklohexen": "HC=CH-CH2-CH2-CH2-CH2-",                            #cyklo_nonbasic
            "cyklopropyn": "C/C-CH2-"                                                                                                                                            #cyklo_non_non_basic
        }


    def split_chem(chem_object):
        for keys in chem_object.chemical_dictionary:

            if "cyklo" in keys:
                keys_an = keys + "an"

                if "anan" in keys_an:
                    chem_object.cyklo_list.append(keys)
                    chem_object.v_cyklo_list.append(chem_object.chemical_dictionary[keys])

                elif "enan" in keys_an:
                    chem_object.cyklo_non_basic_list.append(keys)
                    chem_object.v_cyklo_non_basic_list.append(chem_object.chemical_dictionary[keys])

                else:
                    chem_object.cyklo_non_non_basic_list.append(keys)
                    chem_object.v_cyklo_non_non_basic_list.append(chem_object.chemical_dictionary[keys])

            else:
                keys_an = keys + "an"

                if "anan" in keys_an:
                    chem_object.basic_list.append(keys)
                    chem_object.v_basic_list.append(chem_object.chemical_dictionary[keys])

                elif "enan" in keys_an:
                    chem_object.non_basic_list.append(keys)
                    chem_object.v_non_basic_list.append(chem_object.chemical_dictionary[keys])

                else:
                    chem_object.non_non_basic_list.append(keys)
                    chem_object.v_non_non_basic_list.append(chem_object.chemical_dictionary[keys])

        for keys in chem_object.chemical_dictionary:
            chem_object.list_of_keys.append(keys)
            chem_object.list_of_values.append(chem_object.chemical_dictionary[keys])
        return


    def my_chemical_list(chem_object):
        try:
            for chars in chem_object.chem_formula:

                if chars.isalpha():
                    if chars in ascii_lowercase:
                        number_of_lists = len(chem_object.chemical_list)
                        chem_object.position_chars.append((chars, number_of_lists))
                        chem_object.chemical_list[number_of_lists - 1].append(chars)
                    else:
                        number_of_lists = len(chem_object.chemical_list)
                        chem_object.position_chars.append((chars, number_of_lists))
                        chem_object.chemical_list[number_of_lists - 1].append(chars)

                elif chars.isnumeric():
                    l = len(chem_object.position_chars) - 1
                    chem_object.chemical_list[chem_object.position_chars[l][1] - 1].append(chars)
                    del(chem_object.position_chars[l])

                elif chars == "-" or "=" or "/":
                    l = len(chem_object.position_chars) - 1
                    chem_object.chemical_list[chem_object.position_chars[l][1] - 1].append(chars)
                    chem_object.chemical_list.append([])
                    del(chem_object.position_chars[l])
                print(chem_object.chemical_list)
            print(chem_object.chemical_list)
        except:
            pass
        return
            

    def turtle_writer(chem_object):
        #t.bgcolor("black")
        #t.color("white")
        t.penup()
        t.goto(-350, 0)
        t.pendown()
        for lists in chem_object.chemical_list:
            for string in lists:
                style = ("Courier", 30, "italic")
                t.penup()

                if string.isalpha():                    
                    t.write(string, font = style, align = "left")
                    t.forward(30)

                elif string.isnumeric():                    
                    t.write(string, font = style, align = "left")
                    t.forward(30)

                elif string == "-" or "=" or "/":                    
                    t.write(string, font = style, align = "left")
                    t.forward(30)

                t.pendown()
        t.hideturtle()
        turtle_screen = t.getscreen()
        os.chdir(chem_object.output_path)
        turtle_screen.getcanvas().postscript(file = "chem.eps")
        t.done()
        return


    def cyklo_turtle(chem_object):
        colic_angle = len(chem_object.chemical_list)
        colic_angle = colic_angle - 1
        print(colic_angle)
        #t.bgcolor("black")
        #t.color("white")
        t.penup()
        t.goto(-150, -300)
        t.pendown()
        first_angle = t.heading()
        for lists in chem_object.chemical_list:
            t.forward(150)
            try:
                t.left(360 / colic_angle)
            except ZeroDivisionError:
                tk_messagebox.showerror(
                    title="Can not devide by zero!", message="Please enter valid details.")
                return
            position = t.position()
            angle = t.heading()
            for string in lists:
                style = ("Courier", 30, "italic")

                if string.isalpha() or string.isnumeric():
                    t.setheading(first_angle)
                    t.write(string, font = style, align = "left")
                    t.penup()
                    t.forward(30)
                    t.pendown()
                    
                elif string == "=":
                    t.penup()
                    t.setposition(position[0], position[1])
                    t.setheading(angle)
                    t.right(90)
                    t.forward(20)
                    t.left(90)
                    t.pendown()
                    t.forward(150)
                    t.penup()
                    t.setposition(position[0], position[1])
                    t.setheading(angle)
                    t.pendown

                elif string == "/":
                    t.penup()
                    t.setposition(position[0], position[1])
                    t.setheading(angle)
                    t.right(90)
                    t.forward(20)
                    t.left(90)
                    t.pendown()
                    t.forward(150)
                    t.setposition(position[0], position[1])
                    t.setheading(angle)

                else:
                    pass

            t.penup()
            t.setposition(position[0], position[1])
            t.setheading(angle)
            t.pendown()
        t.hideturtle()
        turtle_screen = t.getscreen()
        os.chdir(chem_object.output_path)
        turtle_screen.getcanvas().postscript(file = "chem.eps")
        t.done()
        return


    def find_online(chem_object):
        if chem_object.chem_name != "":
            google = "https://www.google.cz/search?q=" + chem_object.chem_name
            print(google)
            os.startfile(google)
        return
    

    def save_image(chem_object):
        file_path = chem_object.output_path + "/chem.eps"
        convertapi.api_secret = 'wHkfkm9XjAx5x8LN'
        convertapi.convert('png', {
            'File': file_path
        }, from_format = 'eps').save_files(chem_object.output_path)
        print("Saved, goodbye!")
        return
