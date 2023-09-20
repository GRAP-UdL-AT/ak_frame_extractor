"""
Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:
    User interface that contains functions related to MAIN SCREEN.

Use:
    ui_frame_extractor_config = GUIFrameExtractorConfig(ui_path_config_file)
    app = GUIFrameExtractorConsole(ui_frame_extractor_config, dataset_manager_config_obj, frames_extractor_config)
    app.mainloop()

"""

import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from gui_frame_ext.about_window import AboutWindow2

from helpers.helper_validation import digit_validation
from dataset_management.dataset_config import DatasetConfig
from dataset_management.dataset_manager import DatasetManager
from video_extraction_management.frame_extraction import FramesVideoManager


class GUIFrameExtractorConsole2(tk.Tk):
    r_config = None
    dataset_config = None
    frames_extractor_config = None

    LABEL_WIDTH = 15
    ENTRY_WIDTH_PATH = 50
    BUTTON_WIDTH = 10

    TAB_TITLE_1 = 'Dataset Creation'
    TAB_TITLE_2 = 'Data Extraction'
    TAB_TITLE_3 = 'Data Migration'

    create_dataset_frame = None
    create_dataset_options_frame = None
    user_path_label = None
    user_path_entry = None
    dataset_name_label = None
    dataset_name_entry = None
    base_path_label = None
    base_path_entry = None
    load_base_path_button = None
    create_dataset_button = None
    data_extraction_frame = None
    data_options_frame = None
    current_path_label = None
    current_path_entry = None
    select_folder_button = None
    offset_label = None
    offset_spinbox = None
    number_of_frames_label = None
    number_of_frames_spinbox = None
    # ----
    rgb_check_var = None
    depth_check_var = None
    ir_check_var = None
    cloud_points_check_var = None
    rgb_check = None
    depth_check = None
    ir_check = None
    cloud_points_check = None
    # ----
    extract_folder_data_frame = None
    input_folder_label = None
    input_folder_entry = None
    load_folder_button = None
    extract_folder_button = None
    extract_file_data_frame = None
    input_file_label = None
    input_file_entry = None
    select_file_button = None
    extract_file_button = None
    message_frame = None
    messages_label = None
    messages_info = None
    results_info_label = None
    results_info = None
    quit_button = None

    tab_group = None
    tab_1 = None
    tab_2 = None

    def __init__(self, r_config, dataset_config, frames_extractor_config, master=None):
        super().__init__(master)
        # ---------------------------
        # configuration parameters
        self.r_config = r_config  # assign config
        self.dataset_config = dataset_config
        self.frames_extractor_config = frames_extractor_config
        # ---------------------------
        self.geometry(self.r_config.geometry_main)
        self.title(r_config.app_title)
        self.attributes('-topmost', True)
        # self.attributes('-fullscreen', True)
        self.state('normal')
        assets_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(assets_path, 'assets', 'ak_fraex_32.png')
        self.iconphoto(False, tk.PhotoImage(file=img_path))
        # ---------------------------
        self.create_tabs()
        self.create_widgets_tab_1()
        self.create_widgets_tab_2()
        self.create_widgets_tab_3()
        self.create_menu_bars()
        self.create_status_bar()
        self.create_message_info()
        # ---------------------------

    def create_tabs(self):
        self.tab_group = ttk.Notebook(self)
        self.tab_1 = tk.Frame(self.tab_group)
        self.tab_2 = tk.Frame(self.tab_group)
        self.tab_3 = tk.Frame(self.tab_group)
        self.tab_group.add(self.tab_1, text=self.TAB_TITLE_1)
        self.tab_group.add(self.tab_2, text=self.TAB_TITLE_2)
        self.tab_group.add(self.tab_3, text=self.TAB_TITLE_3)
        self.tab_group.pack(expand=1, fill="both")
        pass

    def create_status_bar(self):
        self.status_bar = tk.Label(self, text=";)", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_widgets_tab_1(self):
        # ############## CREATE HIERARCHY ######################
        self.create_dataset_frame = tk.LabelFrame(self.tab_1, text="Create Dataset", relief=tk.RIDGE)
        self.create_dataset_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.create_dataset_options_frame = tk.LabelFrame(self.create_dataset_frame, text="Options", relief=tk.RIDGE)
        self.create_dataset_options_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.user_path_label = tk.Label(self.create_dataset_options_frame, text='User path:', width=self.LABEL_WIDTH)
        self.user_path_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.user_path_entry = tk.Entry(self.create_dataset_options_frame, width=self.ENTRY_WIDTH_PATH)
        self.user_path_entry.grid(row=1, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.user_path_entry.insert(0, self.r_config.user_path)
        self.user_path_entry.config(state='readonly')

        self.dataset_name_label = tk.Label(self.create_dataset_options_frame, text='Dataset name:',
                                           width=self.LABEL_WIDTH)
        self.dataset_name_label.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.dataset_name_entry = tk.Entry(self.create_dataset_options_frame, width=self.ENTRY_WIDTH_PATH)
        self.dataset_name_entry.grid(row=2, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.dataset_name_entry.insert(0, self.dataset_config.dataset_name)

        self.base_path_label = tk.Label(self.create_dataset_options_frame, text='Base path:', width=self.LABEL_WIDTH)
        self.base_path_label.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.base_path_entry = tk.Entry(self.create_dataset_options_frame, width=self.ENTRY_WIDTH_PATH)
        self.base_path_entry.grid(row=3, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.base_path_entry.config(state='readonly')

        self.load_base_path_button = tk.Button(self.create_dataset_options_frame, text='Browse...',
                                               command=self.browse_base_path, width=self.BUTTON_WIDTH)
        self.load_base_path_button.grid(row=3, column=3, sticky=tk.W, ipadx=3, ipady=3)

        self.create_dataset_button = tk.Button(self.create_dataset_options_frame, text='New dataset',
                                               command=self.create_dataset_folder, width=self.BUTTON_WIDTH)
        self.create_dataset_button.grid(row=4, column=3, sticky=tk.W, ipadx=3, ipady=3)

        pass

    def create_widgets_tab_2(self):
        ########################################################
        # DATA EXTRACTION FRAME
        # ---------------------
        self.data_extraction_frame = tk.LabelFrame(self.tab_2, text="Data extraction", relief=tk.RIDGE)
        self.data_extraction_frame.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        # data options frame
        # ---------------------
        self.data_options_frame = tk.LabelFrame(self.data_extraction_frame, text="Options", relief=tk.RIDGE)
        self.data_options_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.current_path_label = tk.Label(self.data_options_frame, text='Working in:', width=self.LABEL_WIDTH)
        self.current_path_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.current_path_entry = tk.Entry(self.data_options_frame, width=self.ENTRY_WIDTH_PATH)
        self.current_path_entry.grid(row=1, column=2, columnspan=3, sticky=tk.W, ipadx=3, ipady=3)
        self.current_path_entry.config(state='readonly')

        self.select_folder_button = tk.Button(self.data_options_frame, text='Browse...',
                                              command=self.browse_working_folder_data, width=self.BUTTON_WIDTH)
        self.select_folder_button.grid(row=1, column=5, sticky=tk.W, ipadx=3, ipady=3)

        self.offset_label = tk.Label(self.data_options_frame, text='Offset in seconds:', width=self.LABEL_WIDTH)
        self.offset_label.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)
        # TODO: 07/04/2022, put automatic parameters from video HERE
        self.offset_spinbox = tk.Spinbox(self.data_options_frame, from_=0, to=30, width=5, justify=tk.RIGHT)
        self.offset_spinbox.grid(row=2, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.offset_spinbox['validate'] = 'all'
        self.offset_spinbox['validatecommand'] = (self.offset_spinbox.register(digit_validation), '%P', '%d')
        # # --------------
        self.number_of_frames_label = tk.Label(self.data_options_frame, text='Number of frames:',
                                               width=self.LABEL_WIDTH)
        self.number_of_frames_label.grid(row=2, column=3, sticky=tk.W, ipadx=3, ipady=3)
        # # -----------------------
        # TODO: 07/04/2022, put automatic parameters from video HERE
        self.number_of_frames_spinbox = tk.Spinbox(self.data_options_frame, from_=1, to=30, width=5, justify=tk.RIGHT)
        self.number_of_frames_spinbox.grid(row=2, column=4, sticky=tk.W, ipadx=3, ipady=3)
        self.number_of_frames_spinbox['validate'] = 'all'
        self.number_of_frames_spinbox['validatecommand'] = (
            self.number_of_frames_spinbox.register(digit_validation), '%P', '%d')
        # ---- check options
        self.type_of_data_label = tk.Label(self.data_options_frame, text='Extract data:',
                                           width=self.LABEL_WIDTH)
        self.type_of_data_label.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.rgb_check_var = tk.IntVar()
        self.depth_check_var = tk.IntVar()
        self.ir_check_var = tk.IntVar()
        self.cloud_points_check_var = tk.IntVar()

        self.rgb_check_var.set(1)  # todo: 18/05/2022 check with functions to see if video recorded is in BGRA
        self.depth_check_var.set(1)
        self.ir_check_var.set(1)
        self.cloud_points_check_var.set(0)
        # todo: 19/05/2022, deactivated because it will be implemented in the near future
        self.rgb_check = tk.Checkbutton(self.data_options_frame, text='RGB, Depth, IR', variable=self.rgb_check_var)
        self.rgb_check.grid(row=3, column=2, sticky=tk.W, ipadx=3, ipady=3)
        # self.depth_check = tk.Checkbutton(self.data_options_frame, text='Depth', variable=self.depth_check_var)
        # self.depth_check.grid(row=3, column=3, sticky=tk.W, ipadx=3, ipady=3)
        # self.ir_check = tk.Checkbutton(self.data_options_frame, text='IR', variable=self.ir_check_var)
        # self.ir_check.grid(row=3, column=4, sticky=tk.W, ipadx=3, ipady=3)
        self.cloud_points_check = tk.Checkbutton(self.data_options_frame, text='Cloud points',
                                                 variable=self.cloud_points_check_var)
        self.cloud_points_check.grid(row=3, column=3, sticky=tk.W, ipadx=3, ipady=3)

        ########################################################
        # EXTRACT DATA FROM FOLDER
        self.extract_folder_data_frame = tk.LabelFrame(self.data_extraction_frame,
                                                       text="Extract data from video folder", relief=tk.RIDGE)
        self.extract_folder_data_frame.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        self.input_folder_label = tk.Label(self.extract_folder_data_frame, text='Input folder:', width=self.LABEL_WIDTH)
        self.input_folder_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.input_folder_entry = tk.Entry(self.extract_folder_data_frame, width=self.ENTRY_WIDTH_PATH)
        self.input_folder_entry.grid(row=1, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.input_folder_entry.config(state='readonly')  # by default readonly

        self.load_folder_button = tk.Button(self.extract_folder_data_frame, text='Input folder',
                                            command=self.select_input_folder_data, width=self.BUTTON_WIDTH)
        self.load_folder_button.grid(row=1, column=3, sticky=tk.W, ipadx=3, ipady=3)

        self.extract_folder_button = tk.Button(self.extract_folder_data_frame, text='Extract frames',
                                               command=self.extract_folder_data, width=self.BUTTON_WIDTH)
        self.extract_folder_button.grid(row=2, column=3, sticky=tk.W, ipadx=3, ipady=3)

        ########################################################
        # EXTRACT DATA FROM FILE
        self.extract_file_data_frame = tk.LabelFrame(self.data_extraction_frame, text="Extract data from video file",
                                                     relief=tk.RIDGE)
        self.extract_file_data_frame.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        self.input_file_label = tk.Label(self.extract_file_data_frame, text='Selected file:', width=self.LABEL_WIDTH)
        self.input_file_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.input_file_entry = tk.Entry(self.extract_file_data_frame, width=self.ENTRY_WIDTH_PATH)
        self.input_file_entry.grid(row=1, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.input_file_entry.config(state='readonly')

        self.select_file_button = tk.Button(self.extract_file_data_frame, text='Select file',
                                            command=self.select_file_data, width=self.BUTTON_WIDTH)
        self.select_file_button.grid(row=1, column=3, sticky=tk.W, ipadx=3, ipady=3)

        self.extract_file_button = tk.Button(self.extract_file_data_frame, text='Extract frames',
                                             command=self.extract_file_data, width=self.BUTTON_WIDTH)
        self.extract_file_button.grid(row=2, column=3, sticky=tk.W, ipadx=3, ipady=3)

        pass

    def create_message_info(self):
        ########################################################
        # MESSAGE FRAME
        self.message_frame = tk.LabelFrame(self, text="Info", relief=tk.RIDGE)
        # self.message_frame.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        self.message_frame.pack(expand=1, fill=tk.X)

        self.messages_label = tk.Label(self.message_frame, text='Messages:', width=self.LABEL_WIDTH)
        self.messages_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.messages_info = tk.Text(self.message_frame, width=65, height=5)
        self.messages_info.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.results_info_label = tk.Label(self.message_frame, text='Results:', width=self.LABEL_WIDTH)
        self.results_info_label.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.results_info = tk.Text(self.message_frame, width=65, height=5)
        self.results_info.grid(row=4, column=1, sticky=tk.W, ipadx=3, ipady=3)

        ########################################################
        self.quit_button = tk.Button(self.message_frame, text='Quit', command=self.quit_app)
        self.quit_button.grid(row=5, column=1, sticky=tk.EW)
        ########################################################

    def create_widgets_tab_3(self):
        print(self.current_path_entry.get())
        ########################################################
        # EXTRACT DATA FROM FOLDER
        self.csv_folder_data_frame = tk.LabelFrame(self.tab_3, text=".CSV files to PASCAL_VOC conversion",
                                                   relief=tk.RIDGE)
        self.csv_folder_data_frame.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        self.input_csv_folder_label = tk.Label(self.csv_folder_data_frame, text='Input folder:', width=self.LABEL_WIDTH)
        self.input_csv_folder_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.input_csv_folder_entry = tk.Entry(self.csv_folder_data_frame, width=self.ENTRY_WIDTH_PATH)
        self.input_csv_folder_entry.grid(row=1, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.input_csv_folder_entry.config(state='readonly')  # by default readonly

        self.load_csv_folder_button = tk.Button(self.csv_folder_data_frame, text='CSV folder',
                                                command=self.select_migrate_folder_data, width=self.BUTTON_WIDTH)
        self.load_csv_folder_button.grid(row=1, column=3, sticky=tk.W, ipadx=3, ipady=3)

        self.migrate_csv_folder_button = tk.Button(self.csv_folder_data_frame, text='Convert files',
                                                   command=self.migrate_folder_data, width=self.BUTTON_WIDTH)
        self.migrate_csv_folder_button.grid(row=2, column=3, sticky=tk.W, ipadx=3, ipady=3)
        pass

    def create_menu_bars(self):
        """
        Add menu to the UI
        :return:
        :return:
        """
        self.menubar = tk.Menu(self)

        # todo: delete menu option

        self.menu_file = tk.Menu(self.menubar, tearoff=False)
        # self.menu_file.add_command(label="A_command", command=self.not_implemented_yet)
        self.menu_file.add_command(label="Quit", command=self.quit_app)

        self.menu_help = tk.Menu(self.menubar, tearoff=False)
        self.menu_help.add_command(label="Help...", command=self.open_about_data)
        self.menu_help.add_command(label="About...", command=self.open_about_data)

        self.menubar.add_cascade(menu=self.menu_file, label='File', underline=0)
        self.menubar.add_cascade(menu=self.menu_help, label='About', underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def open_about_data(self):
        about_windows = AboutWindow2(self)
        about_windows.grab_set()

    def not_implemented_yet(self):
        print("Not implemented yet!!!")

    def clean_text_widgets(self):
        self.messages_info.delete("1.0", "end")
        self.results_info.delete("1.0", "end")

    def browse_base_path(self):
        analyze_status_str = ""
        self.base_path_entry.config(state='normal')  # by default disabled

        directory_selected = filedialog.askdirectory(initialdir=self.r_config.input_dataset_folder)
        if directory_selected == "":
            analyze_status_str = "A directory has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str + "\n")
        else:
            self.messages_info.insert("end", "Base path selected " + directory_selected + "\n")
            # ------------------------------
            self.base_path_entry.delete(0, "end")
            self.base_path_entry.insert(0, directory_selected)
            # ------------------------------
        # ----------------------------------------
        self.base_path_entry.config(state='readonly')  # by default disabled

    def create_dataset_folder(self):
        base_path = os.path.join(self.base_path_entry.get())
        dataset_name = self.dataset_name_entry.get()
        directory_selected = os.path.join(base_path, dataset_name)

        if base_path == "" or dataset_name == "":
            self.messages_info.insert("end", "Browse a folder to configure base path " + "\n")
        else:
            if os.path.isdir(directory_selected):
                msg_box = tk.messagebox.askquestion('Exit Application',
                                                    'Are you sure you want to overwrite the application?',
                                                    icon='warning')
                if msg_box == 'yes':
                    self.dataset_config = DatasetConfig(base_path, dataset_name)
                    dataset_manager_obj = DatasetManager(self.dataset_config)
                    dataset_manager_obj.create_hierarchy()
                    # -----------------------
                    self.current_path_entry.config(state='normal')
                    self.current_path_entry.delete(0, "end")
                    self.current_path_entry.insert(0, directory_selected)
                    self.current_path_entry.config(state='readonly')
                    # ------------------------------
                    self.messages_info.insert("end", f"Created dataset metadata at {directory_selected}" + "\n")
                    # -----------------------
                else:
                    tk.messagebox.showinfo('Return', 'You must select a new base path')
            else:
                self.dataset_config = DatasetConfig(base_path, dataset_name)
                dataset_manager_obj = DatasetManager(self.dataset_config)
                dataset_manager_obj.create_hierarchy()
                # ------------------------------
                self.current_path_entry.config(state='normal')
                self.current_path_entry.delete(0, "end")
                self.current_path_entry.insert(0, directory_selected)
                self.current_path_entry.config(state='readonly')
                # ------------------------------
                # ---------------
                self.messages_info.insert("end", f"Created dataset metadata at {directory_selected}" + "\n")
                # ---------------

    def browse_working_folder_data(self):
        analyze_status_str = ""
        # todo: check this initial folder
        # todo:; put in variables extension settings
        self.current_path_entry.config(state='normal')
        directory_selected = filedialog.askdirectory(initialdir=os.path.join(self.current_path_entry.get()))

        if directory_selected == "":
            analyze_status_str = "A directory has not been selected " + "\n"
            print(analyze_status_str)
        else:
            self.current_path_entry.delete(0, "end")
            self.current_path_entry.insert(0, os.path.join(directory_selected))
            # ----------------------------------------
        analyze_status_str = directory_selected + "\n"
        self.current_path_entry.config(state='readonly')
        self.input_folder_entry.config(state='readonly')
        self.messages_info.insert("end", "Selected " + analyze_status_str)
        # ----------------------------------------

    def select_input_folder_data(self):
        analyze_status_str = ""
        directory_selected = filedialog.askdirectory(initialdir=self.r_config.input_dataset_folder)

        if directory_selected == "":
            analyze_status_str = "A directory has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str)
        else:
            # ----------------------------------------
            self.current_path_entry.config(state='readonly')
            self.input_folder_entry.config(state='normal')
            self.input_folder_entry.delete(0, "end")
            self.input_folder_entry.insert(0, os.path.join(directory_selected))
            self.input_folder_entry.config(state='readonly')
            # ----------------------------------------
        analyze_status_str = directory_selected + "\n"
        self.messages_info.insert("end", "Selected " + analyze_status_str)
        # ----------------------------------------

    def extract_folder_data(self):
        analyze_status_str = ""
        results_info_str = ""
        directory_selected = os.path.join(self.input_folder_entry.get())

        if directory_selected == "":
            analyze_status_str = "A directory has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str)
        else:
            self.input_folder_entry.delete(0, "end")
            self.input_folder_entry.insert(0, directory_selected)

            an_offset = int(self.offset_spinbox.get())
            a_number_of_frames = int(self.number_of_frames_spinbox.get())

            # TODO: 03/03/2022 CHECK DIRECTORY_SELECTED
            self.frames_extractor_config.path_images_output = self.dataset_config.dataset_images_path
            # TODO: 15/02/2022 temporal
            self.frames_extractor_config.path_annotations_output = self.dataset_config.dataset_annotations_path
            track_file = os.path.join(self.dataset_config.dataset_sets_path, 'all.txt')
            # ----------------------------------------
            for a_filename in os.listdir(directory_selected):
                if a_filename.endswith(self.r_config.file_extension_to_search):
                    a_path_filename = os.path.join(directory_selected, a_filename)
                    print(a_filename)
                    print(a_path_filename)
                    frames_extractor_obj = FramesVideoManager(self.frames_extractor_config, a_path_filename)
                    [frames_written, errors, output_folder] = frames_extractor_obj.export_frames_to_files(track_file,
                                                                                                          an_offset,
                                                                                                          a_number_of_frames)
                    results_info_str = f"frames written {frames_written} errors {errors} output folder {output_folder}"
        # ----------------------------------------
        analyze_status_str = directory_selected
        self.messages_info.insert("end", analyze_status_str)
        self.results_info.insert("end", "Extracting from " + results_info_str)

    def select_migrate_folder_data(self):
        analyze_status_str = ""
        directory_selected = filedialog.askdirectory(initialdir=self.r_config.input_dataset_folder)

        if directory_selected == "":
            analyze_status_str = "A directory has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str)
        else:
            # ----------------------------------------
            self.current_path_entry.config(state='readonly')
            self.input_csv_folder_entry.config(state='normal')
            self.input_csv_folder_entry.delete(0, "end")
            self.input_csv_folder_entry.insert(0, os.path.join(directory_selected))
            self.input_csv_folder_entry.config(state='readonly')
            # ----------------------------------------
        analyze_status_str = directory_selected + "\n"
        self.messages_info.insert("end", "Selected " + analyze_status_str)

    def migrate_folder_data(self):
        """
        Used to create .XML objects
        :return:
        """
        analyze_status_str = ""
        results_info_str = ""
        directory_selected = os.path.join(self.input_csv_folder_entry.get())

        if directory_selected == "":
            analyze_status_str = "A directory has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str)
        else:
            self.input_csv_folder_entry.delete(0, "end")
            self.input_csv_folder_entry.insert(0, directory_selected)

            print('HERE WE MIGRATE TO .XML')
            print('self.dataset_config.dataset_name', self.dataset_config.dataset_name)
            print('self.dataset_config.base_path', self.dataset_config.base_path)
            print('directory_selected', directory_selected)
            print('annotations', self.dataset_config.dataset_annotations_path)
            print('square', self.dataset_config.dataset_squares_path)
            directory_annotations = self.dataset_config.dataset_annotations_path
            print(f"directory_annotations={directory_annotations}")
            # ----------------------------------------
            for a_filename in os.listdir(directory_annotations):  # todo 24/08/223 check error path
                # self.r_config.file_extension_to_search
                # if a_filename.endswith('.csv'):
                a_path_filename = os.path.join(directory_annotations, a_filename)
                print(a_filename)
                print(a_path_filename)
                print('HERE WE MIGRATE TO .XML')  # todo: check this and improve it
                print('self.dataset_config.dataset_name', self.dataset_config.dataset_name)
                print('self.dataset_config.base_path', self.dataset_config.base_path)
                base_path = os.path.join(self.dataset_config.base_path)
                dataset_name = self.dataset_config.dataset_name
                directory_selected = os.path.join(base_path, dataset_name)
                self.dataset_config = DatasetConfig(base_path, dataset_name)
                dataset_manager_obj = DatasetManager(self.dataset_config)
                label_filename = 'labelmap_apples_id.json'  # TODO: create a basic .json
                label_json_path = os.path.join(base_path, dataset_name, 'preprocessed_data', label_filename)
                # dataset_manager_obj.create_XML_files(label_json_path)
                dataset_manager_obj.create_labeled_XML_files()
                results_info_str = f" .xml files migrated"
        # ----------------------------------------
        analyze_status_str = directory_selected
        self.messages_info.insert("end", analyze_status_str)
        self.results_info.insert("end", ".xml files migrated " + results_info_str)

    def select_file_data(self):
        analyze_status_str = ""

        path_filename_selected = filedialog.askopenfilename(initialdir=self.input_folder_entry, title="Select a File",
                                                            filetypes=(
                                                                ("Text files", self.r_config.file_extension_to_search),
                                                                ("all files", "*.mkv")))

        if path_filename_selected == "":
            analyze_status_str = "A file has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str)
        else:
            # todo: update automatic of limit offset, update number of frames
            # ---------------------------
            self.input_file_entry.config(state='normal')
            self.input_file_entry.delete(0, "end")
            self.input_file_entry.insert(0, path_filename_selected)
            self.input_file_entry.config(state='readonly')
            # ----------------------------
        # ----------------------------------------
        analyze_status_str = path_filename_selected + "\n"
        self.messages_info.insert("1.0", "Selected " + analyze_status_str)

    def extract_file_data(self):
        analyze_status_str = ""
        results_info_str = ""
        results_info_str_3d = ""
        path_filename_selected = os.path.join(self.input_file_entry.get())

        if path_filename_selected == "":
            analyze_status_str = "A file has not been selected " + "\n"
            self.messages_info.insert("end", analyze_status_str)
        else:
            an_input_file = os.path.join(path_filename_selected)
            an_offset = int(self.offset_spinbox.get())
            a_number_of_frames = int(self.number_of_frames_spinbox.get())

            self.frames_extractor_config.path_images_output = self.dataset_config.dataset_images_path
            # TODO: 15/02/2022 temporal
            self.frames_extractor_config.path_annotations_output = self.dataset_config.dataset_annotations_path
            print(self.current_path_entry.get())
            track_file = os.path.join(self.dataset_config.dataset_sets_path,
                                      'all.txt')  # todo: check error with this 19/05/2022
            # -------------------------
            if self.rgb_check_var.get() == 1:
                pass
                # ------------------------
                frames_extractor_obj = FramesVideoManager(self.frames_extractor_config, an_input_file)
                [frames_written, errors, output_folder] = frames_extractor_obj.export_frames_to_files(track_file, an_offset,
                                                                                                  a_number_of_frames)
                results_info_str = f"frames written {frames_written} errors {errors} output folder {output_folder}"
            # -------------------------
            if self.cloud_points_check_var.get() == 1:
                # 19/05/2022 todo add option checkers
                self.frames_extractor_config.path_mesh_output = self.dataset_config.dataset_cloud_points_path
                [frames_written, errors, output_folder] = frames_extractor_obj.export_frames_to_colorized_mesh(
                    an_offset, a_number_of_frames)
                results_info_str_3d = f"frames written {frames_written} errors {errors} output folder {output_folder}"

        # ----------------------------------------
        analyze_status_str = path_filename_selected + "\n"
        self.messages_info.insert("1.0", "Extracting from " + analyze_status_str)
        self.results_info.insert("1.0", results_info_str)
        self.results_info.insert("1.0", results_info_str_3d)
        # ----------------------------------------

    def quit_app(self):
        # ---------------------------------------------
        self.quit
        self.destroy()

# TODO: 08/04/2022 add internationalization
