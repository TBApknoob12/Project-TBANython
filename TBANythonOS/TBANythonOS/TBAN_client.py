import os
import tkinter as tk
from tkinter import ttk
from minecraft_launcher_lib import launch
from minecraft_launcher_lib.utils.minecraft_directory import get_minecraft_directory
from minecraft_launcher_lib.profile import Profile, ProfileManager

# Set up the main window
root = tk.Tk()
root.title("Minecraft Launcher")
root.geometry("700x500")

# Set up the login frame
login_frame = ttk.LabelFrame(root, text="Login Details")
login_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add username and password labels
ttk.Label(login_frame, text="Username:").grid(column=0, row=0, padx=5, pady=5)
ttk.Label(login_frame, text="Password:").grid(column=0, row=1, padx=5, pady=5)

# Add username and password entry fields
username_entry = ttk.Entry(login_frame, width=30)
password_entry = ttk.Entry(login_frame, width=30, show="*")
username_entry.grid(column=1, row=0, padx=5, pady=5)
password_entry.grid(column=1, row=1, padx=5, pady=5)

# Add checkbox for offline mode
offline_mode_var = tk.BooleanVar(value=False)
ttk.Checkbutton(login_frame, text="Offline Mode", variable=offline_mode_var).grid(column=1, row=2, padx=5, pady=5)

# Set up the game version frame
version_frame = ttk.LabelFrame(root, text="Game Version")
version_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add game version dropdown menu
version_options = ["1.19.4","1.19.3","1.19.2","1.19.1","1.19","1.18.2","1.18.1","1.18","1.17.1","1.17", "1.16.5", "1.16.4","1.16.3","1.16.2","1.16.1","1.16","1.15.2","1.15.1","1.15",]
version_var = tk.StringVar(value=version_options[0])
ttk.Label(version_frame, text="Select Version:").grid(column=0, row=0, padx=5, pady=5)
ttk.OptionMenu(version_frame, version_var, *version_options).grid(column=1, row=0, padx=5, pady=5)

# Set up the profile frame
profile_manager = ProfileManager(get_minecraft_directory())
profile_frame = ttk.LabelFrame(root, text="Profiles")
profile_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add profile dropdown menu
profile_var = tk.StringVar()

def update_profiles():
    profiles = profile_manager.get_profiles()
    profile_menu['menu'].delete(0, 'end')
    for profile_name in profiles:
        profile_menu['menu'].add_command(label=profile_name, command=tk._setit(profile_var, profile_name))

update_profiles()

ttk.Label(profile_frame, text="Select Profile:").grid(column=0, row=0, padx=5, pady=5)
profile_menu = ttk.OptionMenu(profile_frame, profile_var, "")
profile_menu.grid(column=1, row=0, padx=5, pady=5)

# Add button to create new profile
new_profile_entry = ttk.Entry(profile_frame, width=30)
new_profile_entry.grid(column=2, row=0, padx=5, pady=5)

def create_new_profile():
    profile_name = new_profile_entry.get()
    if profile_name:
        profile = Profile(profile_name)
        profile_manager.save_profile(profile)
        update_profiles()

ttk.Button(profile_frame, text="Create New Profile", command=create_new_profile).grid(column=3, row=0, padx=5, pady=5)

# Add button to edit profile
def edit_profile():
    profile_name = profile_var.get()
    if profile_name:
        profile = profile_manager.get_profile(profile_name)
        if profile:
            # Open a new window for editing the profile
            edit_window = tk.Toplevel(root)
            edit_window.title("Edit Profile")

            # Add fields for editing the profile
            ttk.Label(edit_window, text="Game Directory:").grid(column=0, row=0, padx=5, pady=5)
            game_dir_entry = ttk.Entry(edit_window, width=50)
            game_dir_entry.insert(0, profile.game_directory)
            game_dir_entry.grid(column=1, row=0, padx=5, pady=5)

            ttk.Label(edit_window, text="Java Executable:").grid(column=0, row=1, padx=5, pady=5)
            java_exec_entry = ttk.Entry(edit_window, width=50)
            java_exec_entry.insert(0, profile.java_executable)
            java_exec_entry.grid(column=1, row=1, padx=5, pady=5)
                       ttk.Label(edit_window, text="Java Arguments:").grid(column=0, row=2, padx=5, pady=5)
            java_args_entry = ttk.Entry(edit_window, width=50)
            java_args_entry.insert(0, profile.java_arguments)
            java_args_entry.grid(column=1, row=2, padx=5, pady=5)

            ttk.Label(edit_window, text="Game Arguments:").grid(column=0, row=3, padx=5, pady=5)
            game_args_entry = ttk.Entry(edit_window, width=50)
            game_args_entry.insert(0, profile.game_arguments)
            game_args_entry.grid(column=1, row=3, padx=5, pady=5)

            def save_profile():
                # Update the profile with the new values
                profile.game_directory = game_dir_entry.get()
                profile.java_executable = java_exec_entry.get()
                profile.java_arguments = java_args_entry.get()
                profile.game_arguments = game_args_entry.get()

                # Save the profile and close the window
                profile_manager.save_profile(profile)
                edit_window.destroy()

            ttk.Button(edit_window, text="Save", command=save_profile).grid(column=1, row=4, padx=5, pady=5)

ttk.Button(profile_frame, text="Edit Profile", command=edit_profile).grid(column=4, row=0, padx=5, pady=5)

# Set up the modpack installation frame
modpack_frame = ttk.LabelFrame(root, text="Modpack Installation")
modpack_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add modpack URL label and entry field
ttk.Label(modpack_frame, text="Modpack URL:").grid(column=0, row=0, padx=5, pady=5)
modpack_url_entry = ttk.Entry(modpack_frame, width=50)
modpack_url_entry.grid(column=1, row=0, padx=5, pady=5)

# Set up the game options frame
options_frame = ttk.LabelFrame(root, text="Game Options")
options_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add checkbox for Forge support
forge_var = tk.BooleanVar(value=False)
ttk.Checkbutton(options_frame, text="Forge", variable=forge_var).grid(column=0, row=0, padx=5, pady=5)

# Add checkbox for Fabric support
fabric_var = tk.BooleanVar(value=False)
ttk.Checkbutton(options_frame, text="Fabric", variable=fabric_var).grid(column=0, row=1, padx=5, pady=5)

# Add checkbox for Vanilla support
vanilla_var = tk.BooleanVar(value=True)
ttk.Checkbutton(options_frame, text="Vanilla", variable=vanilla_var).grid(column=0, row=2, padx=5, pady=5)

# Set up the launch button
def launch_game():
    # Get the Minecraft directory
    minecraft_dir = get_minecraft_directory()

    # Set the game options based on user input
    game_options = {
        "username": username_entry.get(),
        "password": password_entry.get() if password_entry.get() else None,
        "offline": offline_mode_var.get(),
        "custom_resolution": None,
        "server": False,
        "port": None,
        "fullscreen": False,
        "window_size": None,
        "java_path": None,
        "java_arguments": None,
        "extra_jvm_arguments": None,
        "hide_launch_output": False,
        "custom_icon_path": None,
        "show_game_log": False,
        "auto_connect": True,
    }

    # Set the game version based on user input
    game_version = version_var.get()

    # Set the game options based on user input
    if forge_var.get():
        game_options["forge_version"] = "latest"
    elif fabric_var.get():
        game_options["fabric_version"] = "latest"

    # Download and extract modpack files
    modpack_url = modpack_url_entry.get()
    if modpack_url:
        import zipfile
        import io
        import requests

        response = requests.get(modpack_url)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(minecraft_dir)

    # Get the selected profile and set its settings
    profile_name = profile_var.get()
    if profile_name:
        profile = profile_manager.get_profile(profile_name)
        if profile:
            game_options["java_path"] = profile.java_executable
            game_options["java_arguments"] = profile.java_arguments
            game_options["game_directory"] = profile.game_directory
            game_options["game_arguments"] = profile.game_arguments
                else:
        # Create a new profile with the selected options
        profile = Profile(new_profile_entry.get())
        profile.game_directory = minecraft_dir
        profile.java_executable = None
        profile.java_arguments = None
        profile.game_arguments = f"--version {game_version}"
        profile_manager.save_profile(profile)

        game_options["game_directory"] = minecraft_dir
        game_options["java_path"] = None
        game_options["java_arguments"] = None
        game_options["game_arguments"] = f"--version {game_version} --profile {new_profile_entry.get()}"

    # Launch Minecraft with the selected options
    launch.launch_minecraft(
        version=game_version,
        minecraft_directory=minecraft_dir,
        auth_player_name=game_options["username"],
        auth_uuid=None,
        auth_access_token=game_options["password"],
        user_properties={},
        assets_root=None,
        assets_index_name=None,
        game_directory=game_options["game_directory"],
        java_path=game_options["java_path"],
        jvm_arguments=game_options["java_arguments"],
        game_arguments=game_options["game_arguments"],
        extra_jvm_arguments=None,
        hide_output=False,
        window_size=None,
        fullscreen=False,
        server=False,
        port=None,
        proxy=None,
        launcher_log_handler=None,
    )

launch_button = ttk.Button(root, text="Launch", command=launch_game)
launch_button.pack(padx=10, pady=10, fill="both", expand=True)

# Start the main event loop
root.mainloop()
