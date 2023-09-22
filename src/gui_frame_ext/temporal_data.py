

self.t3_current_path_entry

self.dataset_config = DatasetConfig(base_path, dataset_name)
dataset_manager_obj = DatasetManager(self.dataset_config)



self.t3_current_path_entry

self.t3_input_csv_folder_entry
self.input_csv_folder_entry

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


def t1_create_dataset_folder(self):
    base_path = os.path.join(self.t1_base_path_entry.get())
    dataset_name = self.t1_dataset_name_entry.get()
    directory_selected = os.path.join(base_path, dataset_name)
    directory_selected = os.path.normpath(directory_selected)  # normalize

    # todo: 22/09/2023 could be a datase string to identify the dataset name by default
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
                # todo: 21/09/2023 check
                # self.current_path_entry.config(state='normal')
                # self.current_path_entry.delete(0, "end")
                # self.current_path_entry.insert(0, directory_selected)
                # self.current_path_entry.config(state='readonly')
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
            # todo: check this 21/09/2023
            # self.current_path_entry.config(state='normal')
            # self.current_path_entry.delete(0, "end")
            # self.current_path_entry.insert(0, directory_selected)
            # self.current_path_entry.config(state='readonly')
            # ------------------------------
            # ---------------
            directory_selected = os.path.normpath(directory_selected)
            self.messages_info.insert("end", f"Created dataset metadata at {directory_selected}" + "\n")

        self.current_working_directory = directory_selected
        print(f"self.current_working_directory= {self.current_working_directory}")



        msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to overwrite the application?', icon='warning')
        if msg_box == 'yes':
            self.dataset_config = DatasetConfig(base_path, dataset_name)
            dataset_manager_obj = DatasetManager(self.dataset_config)
            dataset_manager_obj.create_hierarchy()
            # ------------------------------
            # Creating
            # ------------------------------
            print("Creating")
            self.messages_info.insert("end", f"Created dataset metadata at {directory_selected}" + "\n")
            # -----------------------
        else:
            tk.messagebox.showinfo('Return', 'You must select a new base path')