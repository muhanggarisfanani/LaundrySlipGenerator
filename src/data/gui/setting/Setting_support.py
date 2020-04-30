#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 10, 2020 09:28:47 PM +07  platform: Windows NT

import sys
import os.path
import easygui
import re

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import data.gui.setting.Setting
import data.gui.about.About
import data.util.dbcontroller

def loadDatabase():
    global database
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    database = data.util.dbcontroller.dbConnect(os.path.join(prog_location,"data/db/database.db"))

def closeDatabase():
    data.util.dbcontroller.dbDisconnect(database)

def set_Tk_var():
    loadDatabase()
    query = 'SELECT * FROM setting WHERE id=0'
    Tuple = data.util.dbcontroller.getTuple(database,query)
    global AlamatSaatIniVar
    AlamatSaatIniVar = tk.StringVar()
    AlamatSaatIniVar.set(Tuple[1])
    global WebsiteSaatIniVar
    WebsiteSaatIniVar = tk.StringVar()
    WebsiteSaatIniVar.set(Tuple[2])
    global KabirSaatIniVar
    KabirSaatIniVar = tk.StringVar()
    KabirSaatIniVar.set(Tuple[3])
    global GajiSaatIniVar
    GajiSaatIniVar = tk.StringVar()
    GajiSaatIniVar.set('Rp' + str(Tuple[5]))
    global LogoSaatIniVar
    LogoSaatIniVar = tk.StringVar()
    if (Tuple[4] == 'default'):
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        LogoSaatIniVar.set(simplifiedLogoName(os.path.join(prog_location,"data/logo.jpg")))
    else:
        LogoSaatIniVar.set(simplifiedLogoName(Tuple[4]))
    global TlabelStatusVar
    TlabelStatusVar = tk.StringVar()
    TlabelStatusVar.set('Database successfully initialized.')
    global EntryAlamatVar
    EntryAlamatVar = tk.StringVar()
    global EntryWebsiteVar
    EntryWebsiteVar = tk.StringVar()
    global EntryKabirVar
    EntryKabirVar = tk.StringVar()
    global EntryGajiVar
    EntryGajiVar = tk.StringVar()
    global logoPath
    logoPath = tk.StringVar()
    logoPath.set('')
    closeDatabase()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def tButtonBackCommand():
    TlabelStatusVar.set('Back to title page.')
    # Menutup halaman setting
    destroy_window()
    # Membuka halaman start
    data.gui.start.Start.vp_start_gui()

def tButtonSaveCommand():
    TlabelStatusVar.set('Save button clicked.')
    # Mengambil nilai masing" Entry
    alamat = EntryAlamatVar.get()
    website = EntryWebsiteVar.get()
    kabir = EntryKabirVar.get()
    gaji = EntryGajiVar.get()
    logo = logoPath.get()
    # Memodifikasi database
    loadDatabase()
    if (alamat != ''):
        data.util.dbcontroller.updateTuple(database, 'setting', "alamat='"+alamat+"'", 'id=0')
        AlamatSaatIniVar.set(alamat)
        EntryAlamatVar.set('')
    if (website != ''):
        data.util.dbcontroller.updateTuple(database, 'setting', "website='"+website+"'", 'id=0')
        WebsiteSaatIniVar.set(website)
        EntryWebsiteVar.set('')
    if (kabir != ''):
        data.util.dbcontroller.updateTuple(database, 'setting', "currentKabir='"+kabir+"'", 'id=0')
        KabirSaatIniVar.set(kabir)
        EntryKabirVar.set('')
    if (gaji != ''):
        data.util.dbcontroller.updateTuple(database, 'setting', "gajiPerjam='"+gaji+"'", 'id=0')
        GajiSaatIniVar.set('Rp' + gaji)
        EntryGajiVar.set('')
    if (logo != ''):
        data.util.dbcontroller.updateTuple(database, 'setting', "logo='"+logo+"'", 'id=0')
        LogoSaatIniVar.set(simplifiedLogoName(logo))
        logoPath.set('')
    TlabelStatusVar.set('Data updated.')
    closeDatabase()

def tButtonAboutCommand():
    TlabelStatusVar.set('About page opened')
    # Menutup halaman setting
    destroy_window()
    # Membuka halaman about
    data.gui.about.About.vp_start_gui()
    
def tButtonLogoLaundryCommand():
    # Membuka openfiledialog untuk mencari berkas gambar logo laundry
    tPathLogo = easygui.fileopenbox(title='Select Logo Image', filetypes = [["*.jpg", "JPG Image"], ["*.png", "PNG Image"]])
    if (tPathLogo != None):
        logoPath.set(tPathLogo)
        TlabelStatusVar.set('New logo selected')

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def simplifiedLogoName(logoPath):
    logoName = re.split(r'[/\\]', logoPath)[len(re.split(r'[/\\]', logoPath))-1]
    return logoName