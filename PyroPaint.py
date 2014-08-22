"""
--- Pyro Paint v1.0 ---

Pyro Paint is a minimalistic graphical drawing program
Copyright (C) 2014  Eric Sund

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.



See License.txt for more information.

Pyro Paint was written as a simple experiment.  Commits from initial developer
may be limited.  Please clone http://www.github.com/Altazon/PyroPaint/ for updates.

Contact:  Eric Sund
	  ericsund@ericsund.tk
"""

import pygame, pygame.locals, sys, easygui
from easygui import *
from pygame.locals import *
from pygame import *

#set up objects--------------------------------------------------
def objects():
    eraser = pygame.image.load("imgs/eraser.png").convert_alpha()
    tools = pygame.image.load("imgs/wrench.png").convert_alpha()
    pencil = pygame.image.load("imgs/pencil.png").convert_alpha()
    stamp = pygame.image.load("imgs/stamp.png").convert_alpha()  
    paint_brush = pygame.image.load("imgs/paint brush.png").convert_alpha()
    rainbow = pygame.image.load("imgs/rainbow.jpg").convert()
    _new_ = pygame.image.load("imgs/new.png").convert_alpha()
    _open_ = pygame.image.load("imgs/open.png").convert_alpha()
    _save_ = pygame.image.load("imgs/save.png").convert_alpha()
    _about_ = pygame.image.load("imgs/about.png").convert_alpha()
    
    eraser = pygame.transform.scale(eraser, (20,20))
    stamp = pygame.transform.scale(stamp, (20,20))
    tools = pygame.transform.scale(tools, (20,20))
    pencil = pygame.transform.scale(pencil, (20,20))
    paint_brush = pygame.transform.scale(paint_brush, (20,20))
    rainbow = pygame.transform.scale(rainbow, (100,100))
    _new_ = pygame.transform.scale(_new_, (150,25))
    _open_ = pygame.transform.scale(_open_, (150,25))
    _save_ = pygame.transform.scale(_save_, (150,25))
    _about_ = pygame.transform.scale(_about_, (150,25))
    
    canvas.blit(_new_, (0,0))
    canvas.blit(_open_, (150,0))
    canvas.blit(_save_, (300,0))
    canvas.blit(_about_, (450,0))
    canvas.blit(rainbow, (500,25))
    canvas.blit(pencil, (0,25))
    canvas.blit(paint_brush, (0,45))
    canvas.blit(eraser, (0,65))
    canvas.blit(tools, (0, 85))
    canvas.blit(stamp, (0,105))
    pygame.display.update()
#-----------------------------------------------------------------

#MAIN-------------------------------------------------------------
pygame.init()
canvas = pygame.display.set_caption("Pyro Paint")
canvas = pygame.display.set_mode((600,600),0,32)
canvas.fill((255,255,255))
pygame.display.update()
objects()
#-----------------------------------------------------------------

#define buttons and their functions-------------------------------

#defaults...
clock = pygame.time.Clock() #initialize clock
z = 0 #mouse is lifted
stamp_type = (None) #default stamp type
draw_type = ("pencil") #pencil is enabled
colour = (0,0,0) #pencil is black
utencil_size = (10) #utencil size is 10

while 1:
    clock.tick(60)
    x,y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #x
            optns = ["Yes", "No", "Back"]
            saveornot=buttonbox("Save if you haven't already?", "Quit Pyro Paint", optns)
            if saveornot == "Yes":
                save_location = filesavebox("", "Save File - Pyro Paint")
                pygame.image.save(canvas, save_location)        
                pygame.display.quit()
                sys.exit()
            elif saveornot == "No":
                pygame.display.quit()
                sys.exit()
            elif saveornot == "Back":
                pass
        elif event.type == MOUSEBUTTONDOWN: #functions of menu buttons - happen right away
            z = 1
            if x >= 0 and x <= 150 and y >= 0 and y <= 25: #new button
                canvas = pygame.display.set_caption("Pyro Paint")
                canvas = pygame.display.set_mode((600,600),0,32)
                canvas.fill((255,255,255))
                pygame.display.update()
                objects()
            elif x >= 151 and x <= 300 and y >= 0 and y <= 25: #open button
                picture_location = fileopenbox("", "Open Your File - Pyro Paint")
                picture = pygame.image.load(picture_location).convert_alpha()
                canvas.blit(picture, (0,0))
                objects()
                pass
            elif x >= 301 and x <= 450 and y >= 0 and y <= 25: #save button
                save_location = filesavebox("", "Save Your File - Pyro Paint", default = "My Drawing.png")
                pygame.image.save(canvas, save_location)
                save = 1
            elif x >= 451 and x <= 600 and y >= 0 and y <= 25: #about button
	        license = open("License.txt", "r").read()
	        pygameC = "\nPygame Copyright (C) 2000-2001  Pete Shinners"
	        easyguiC = "\nEasyGUI Copyright (c) 2010, Stephen Raymond Ferg"
                textbox("Pyro Paint is a minimalistic graphical drawing program originally started by Eric Sund.  Pyro Paint Copyright (C) 2013  Eric Sund" + pygameC, "About - Pyro Paintv.1.0", license)
            elif x >= 500 and x <= 600 and y >=26 and y <= 125: #colour getter thingy button
                pos = pygame.mouse.get_pos()
                colour = canvas.get_at(pos)
                pygame.draw.circle(canvas, colour, (550, 150), 20, 20)
                pygame.display.update()
            #establish that the user clicked on the other (non-menu) buttons
            elif x >= 0 and x <= 20 and y >= 26 and y <= 45: #pencil button
                draw_type = ("pencil")
            elif x >= 0 and x <= 20 and y >= 46 and y <= 65: #paint brush button
                draw_type = ("paint brush")
            elif x >= 0 and x <= 20 and y >= 66 and y <= 85: #eraser button
                draw_type = ("eraser")
            elif x >= 0 and x <= 20 and y >= 86 and y <= 105: #tools button
                draw_type = ("tools")
            elif x >=0 and x <=20 and y >= 105 and y <= 125: #stamps button (code below to open it)
                draw_type = ("stamps")
                heart = pygame.image.load("imgs/heart.png").convert_alpha()
                heart = pygame.transform.scale(heart, (20,20))
                happy = pygame.image.load("imgs/happy.png").convert_alpha()
                happy = pygame.transform.scale(happy, (20,20))
                star = pygame.image.load("imgs/star.png").convert_alpha()
                star = pygame.transform.scale(star, (20,20))
                close = pygame.image.load("imgs/close.png")
                close = pygame.transform.scale(close, (20,20))
                canvas.blit(heart, (21,105))
                canvas.blit(happy, (41,105))
                canvas.blit(star, (61,105))
                canvas.blit(close, (81, 105))
                pygame.display.update()
	    #stamps sub-menu
            if x >= 21 and x <= 40 and y >= 105 and y <= 125:
                stamp_type = ("heart")
            if x >= 41 and x <= 60 and y >= 105 and y <= 125:
                stamp_type = ("happy")
            if x >= 61 and x <= 80 and y >= 105 and y <= 125:
                stamp_type = ("star")
            if x >= 81 and x <= 100 and y >= 105 and y <= 125: #close stamps
                draw_type = ("pencil")
                stamp_type = None
                stamps_void = pygame.image.load("imgs/stamps_void.png").convert_alpha()
                canvas.blit(stamps_void, (21,105))
                pygame.display.update()
        elif event.type == MOUSEBUTTONUP:
            z = 0
        if z == 1: #what the buttons do... (this is after Pyro Paint knows the user clicked the button)
            if stamp_type == ("heart"):
                if x >= 0 and x <= 500 and y >= 130 and y <= 600:
                    canvas.blit(heart, (x,y))
                    pygame.display.update()
            if stamp_type == ("happy"):
                if x >= 0 and x <= 500 and y >= 130 and y <= 600:
                    canvas.blit(happy, (x,y))
                    pygame.display.update()
            if stamp_type == ("star"):
                if x >= 0 and x <= 500 and y >= 130 and y <= 600:
                    canvas.blit(star, (x,y))
                    pygame.display.update()
            elif draw_type == ("pencil"): #draw in the canvas space (pencil)
                if x >= 0 and x <= 500 and y >= 130 and y <= 600:
                    pygame.draw.circle(canvas, colour, (x,y), utencil_size, utencil_size)
                    pygame.display.update()
            elif draw_type == ("paint brush"): #draw in the canvas space (paint brush)
                if x >= 0 and x <= 500 and y >= 130 and y <= 600:
                    pygame.draw.line(canvas, colour, (x,y), (x,y), utencil_size)
                    pygame.display.update()
            elif draw_type == ("eraser"): #erase in the canvas space (eraser)
                if x >= 0 and x <= 500 and y >= 130 and y <= 600:
                    pygame.draw.circle(canvas, (255,255,255), (x,y), utencil_size, utencil_size)
                    pygame.display.update()
            elif draw_type == ("tools"): #open the tools menu               
                usingTools = True
                while usingTools:
                    tools_avail = ["Utencil Size", "Tint", "Back"]
                    tools_avail_CHOICE = buttonbox("What do you want to do?", "Tools", tools_avail)
                    if tools_avail_CHOICE == "Back":
                        usingTools = False
                        draw_type = ("pencil")
                    elif tools_avail_CHOICE == "Tint":
                        changingColour = True
                        while changingColour:
                            tint_kinds = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Custom", "Back"]
                            tints = buttonbox("Which Tint?", "Tools", tint_kinds)
                            if tints == "Back":
                                changingColour = False
                            elif tints == "Custom":
				tintcolour = multenterbox("Enter RBG values for a tint.", "Custom Tint - Options", ("R", "B", "G"))
                                R = int(tintcolour[0])
				B = int(tintcolour[1])
				G = int(tintcolour[2])
				tintcolour = (R,B,G)
				tint_template = pygame.image.load("imgs/tint_template.png").convert_alpha()
                                tint_template = pygame.transform.scale(tint_template, (500,475))
                                tint_template.set_alpha(80)
                                pxarray = pygame.PixelArray(tint_template)
				white = (255,255,255)
                                pxarray.replace(white, tintcolour)
                                del pxarray
                                canvas.blit(tint_template, (0,126))
                                changingColour = False
                                pygame.display.update()
                            elif tints == "Red":
                                red = pygame.image.load("imgs/red.png").convert()
                                red = pygame.transform.scale(red, (500,475))
                                red.set_alpha(80)
                                canvas.blit(red, (0,126))
                                changingColour = False
                                pygame.display.update()
                            elif tints == "Orange":
                                orange = pygame.image.load("imgs/orange.png").convert()
                                orange = pygame.transform.scale(orange, (500,475))
                                orange.set_alpha(80)
                                canvas.blit(orange, (0,126))
                                changingColour = False
                                pygame.display.update()
                            elif tints == "Yellow":
                                yellow = pygame.image.load("imgs/yellow.png").convert()
                                yellow = pygame.transform.scale(yellow, (500,475))
                                yellow.set_alpha(80)
                                canvas.blit(yellow, (0,126))
                                changingColour = False
                                pygame.display.update()
                            elif tints == "Green":
                                green = pygame.image.load("imgs/green.png").convert()
                                green = pygame.transform.scale(green, (500,475))
                                green.set_alpha(80)
                                canvas.blit(green, (0,126))
                                changingColour = False
                                pygame.display.update()
                            elif tints == "Blue":
                                blue = pygame.image.load("imgs/blue.png").convert()
                                blue = pygame.transform.scale(blue, (500,475))
                                blue.set_alpha(80)
                                canvas.blit(blue, (0,126))
                                changingColour = False
                                pygame.display.update()
                            elif tints == "Purple":
                                purple = pygame.image.load("imgs/purple.png").convert()
                                purple = pygame.transform.scale(purple, (500,475))
                                purple.set_alpha(80)
                                canvas.blit(purple, (0,126))
                                changingColour = False
                                pygame.display.update()
                    elif tools_avail_CHOICE == "Utencil Size":
                        changingSize = True
                        while changingSize:
                            how_to_change_OPTIONS = ["Manual", "Auto", "Back"]
                            how_to_change = buttonbox("How do you want to change the size?", "Utencil Size", how_to_change_OPTIONS)
                            if how_to_change == "Back":
                                changingSize = False
                            if how_to_change == "Manual":
                                changingManual = True
                                while changingManual:
                                    title = "Utencil Size"
                                    utencil_size = enterbox("Enter a utencil size below as a number.", title)
                                    utencil_size = int(utencil_size)
                                    changingSize = False
                                    changingManual = False
                                    usingTools = False
                                    draw_type = ("pencil")
                            if how_to_change == "Auto":
                                changingAuto = True
                                while changingAuto:
                                    utencil_size_CHOICE = buttonbox("What size?", "Utencil Size", ["Small", "Medium", "Large", "Back"])
                                    if utencil_size_CHOICE == "Back":
                                        changingAuto = False
                                    if utencil_size_CHOICE == "Small":
                                        utencil_size = int(5) 
                                        changingSize = False
                                        changingAuto = False
                                        usingTools = False
                                        draw_type = ("pencil")
                                    if utencil_size_CHOICE == "Medium":
                                        utencil_size = int(20)
                                        changingSize = False
                                        changingAuto = False
                                        usingTools = False
                                        draw_type = ("pencil")
                                    if utencil_size_CHOICE == "Large":
                                        utencil_size = int(35)
                                        changingSize = False
                                        changingAuto = False
                                        usingTools = False
                                        draw_type = ("pencil")

"""
Please leave this here.  For use with original developer.

Times told to stop by Dad: 5
Times told to stop by Mom: 2
Total times told to stop coding: 7
"""
