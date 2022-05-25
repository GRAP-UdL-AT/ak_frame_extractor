"""
Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:

Use:
    from gui_frame_ext.about_window import AboutWindow

    def open_about_data(self):
        about_windows = AboutWindow(self)
        about_windows.grab_set()

"""


import os
import tkinter as tk
from gui_frame_ext.gui_frame_ext_config import GUIFrameExtractorConfig2


class AboutWindow2(tk.Toplevel):
    title_str = 'AK Frame Extractor (AK_FRAEX)'
    version_number_str = '1.0'

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(GUIFrameExtractorConfig2.geometry_about)
        self.title('About...')
        self.resizable(width=False, height=False)  # do not change the size
        self.attributes('-topmost', True)
        assets_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(assets_path, 'assets', 'icon_app.png')
        self.iconphoto(False, tk.PhotoImage(file=img_path))
        # ---------------------------

        about_label = tk.Label(self, text=self.title_str+' '+self.version_number_str)
        about_label.config(font=("Verdana", 12))
        about_label.pack(anchor=tk.CENTER)

        text_info = tk.Label(self)

        about_text_info = f' \n' \
                          f'Created by: Juan Carlos Miranda\n' \
                          f'Site: https://github.com/juancarlosmiranda\n' \
                          f'November 2021 \n' \
                          f' \n' \
                          f'PAgFRUIT project RTI2018-094222-B-I00\n' \
                          f'http://www.pagfruit.udl.cat/\n' \
                          f' \n' \
                          f'Research Group in AgroICT & Precision Agriculture\n' \
                          f'https://www.grap.udl.cat/\n'

        text_info['text'] = about_text_info
        text_info.pack(anchor=tk.CENTER)

        img_label = tk.Label(self)
        assets_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(assets_path, 'assets', 'logo_grap.png')
        img_label.image = tk.PhotoImage(file=img_path)
        img_label['image'] = img_label.image
        img_label.pack()

        buttonClose = tk.Button(self, text='Close', command=self.destroy)
        buttonClose.pack(expand=True)
