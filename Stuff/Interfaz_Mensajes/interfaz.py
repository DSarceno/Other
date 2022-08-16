#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 1.7.2020
#
#
#
# -----------------------
# Graphic interface used to send -whatsapp- messages


# Libraries/Modules
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

# class
class messages(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = 'Messages')
        self.set_default_size(350,100)
        self.set_resizable(False)
        self.box = Gtk.VBox()
        self.add(self.box)

        # GRID
        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(1)
        self.grid.set_column_spacing(1)
        self.box.pack_start(self.grid,True,True,0)


        # ------------------------------------------------
        # MENU
        mainMenuB = Gtk.MenuBar()

        # Help
        helpMenu = Gtk.Menu()
        helpMenuName = Gtk.MenuItem('Ayuda')
            # Items
        helpAD = Gtk.MenuItem('Acerca de...')

        helpMenuName.set_submenu(helpMenu)
        helpMenu.append(helpAD)

        # Add menu to the grid
        mainMenuB.append(helpMenuName)
        self.grid.attach(mainMenuB,0,0,5,1)


        # Menu actions
        helpAD.connect('activate', self.helpAD_activate)
        # -----------------------------------------------

        '''
        # -----------------------------------------------
        # Text Entry
        self.messageEntry = Gtk.Entry()
        self.messageEntry.set_text('Ingrese Mensaje')

        # Add to the grid
        self.grid.attach(self.messageEntry,10,10,100,10)

        # Text actions

        # ----------------------------------------------
        '''

        # ----------------------------------------------
        # Good Morning/Night
        self.radioGM = Gtk.RadioButton.new_with_label_from_widget(None, 'Buenos Días')
        self.radioGM.connect('toggled', self.radioGM_toggled)
        self.radioGA = Gtk.RadioButton.new_from_widget(self.radioGM)
        self.radioGA.set_label('Buenas Tardes')
        self.radioGA.connect('toggled', self.radioGA_toggled)

        # Add to the Grid
        self.grid.attach(self.radioGM,10,10,1,3)
        self.grid.attach_next_to(self.radioGA, self.radioGM, Gtk.PositionType.RIGHT,1,3)

        self.saludo = ''
        # ----------------------------------------------


        # ----------------------------------------------
        # Text send button
        self.msj1 = Gtk.Button('Mensaje 1')

        # Add to the grid below the text Entry
        self.grid.attach_next_to(self.msj1, self.radioGM, Gtk.PositionType.BOTTOM, 2, 10)

        # Button actions
        self.msj1.connect('clicked', self.msj1_clicked)
        # ----------------------------------------------


        # ----------------------------------------------
        # Text send button
        self.msj2 = Gtk.Button('Mensaje 2')

        # Add to the grid below the text Entry
        self.grid.attach_next_to(self.msj2, self.msj1, Gtk.PositionType.BOTTOM, 2, 10)

        # Button actions
        self.msj2.connect('clicked', self.msj2_clicked)
        # ----------------------------------------------


        # ----------------------------------------------
        # Text send button
        self.msj3 = Gtk.Button('Mensaje 3')

        # Add to the grid below the text Entry
        self.grid.attach_next_to(self.msj3, self.msj2, Gtk.PositionType.BOTTOM, 2, 10)

        # Button actions
        self.msj3.connect('clicked', self.msj3_clicked)
        # ----------------------------------------------


        # ----------------------------------------------
        # Text send button
        self.msj4 = Gtk.Button('Mensaje 4')

        # Add to the grid below the text Entry
        self.grid.attach_next_to(self.msj4, self.msj3, Gtk.PositionType.BOTTOM, 2, 10)

        # Button actions
        self.msj4.connect('clicked', self.msj4_clicked)
        # ----------------------------------------------
    def radioGM_toggled(self, widget):
        self.saludo = 'Buenos Días'

    def radioGA_toggled(self, widget):
        self.saludo = 'Buenas Tardes'

    def msj1_clicked(self, widget):
        msj1 = self.saludo + ' Puto'
        print(msj1)

    def msj2_clicked(self, widget):
        msj2 = self.saludo + ' Pendejo'
        print(msj2)

    def msj3_clicked(self, widget):
        msj3 = self.saludo + ' Larry'
        print(msj3)

    def msj4_clicked(self, widget):
        msj4 = self.saludo + ' Bob'
        print(msj4)

    def helpAD_activate(self, widget):
        #acerca de dialogo
        vbox = Gtk.VBox()
        adD = Gtk.AboutDialog()
        adD.set_program_name('Whatsapp Extension')
        adD.set_version('2.0.1')
        #adD.set_authors('DSR')
        adD.set_copyright('Copyright © 2021 Diego Sarceño')
        adD.set_comments('Description/how to')
        adD.set_logo_icon_name(None)
        adD.set_website('https://github.com/DSarceno/programacionMatematica1/blob/master/Proyecto/proyecto.py')
        adD.set_website_label('Codigo Fuente')
        vbox.pack_start(adD, False, False, 0)
        self.add(vbox)
        adD.run()
        adD.destroy()



ventana = messages()
ventana.connect('delete-event', Gtk.main_quit)
ventana.show_all()
Gtk.main()
