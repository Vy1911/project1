import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller import TelevisionController


class TelevisionGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("TV Remote")

        # Initialize mute status and previous volume
        self.is_muted = False  # To track mute/unmute status
        self.previous_volume = self.controller.tv.get_volume()  # To store the volume before mute

        # Loading images dynamically
        try:
            self.bbc_logo = Image.open("bbc.jpg")
            self.nbc_logo = Image.open("nbc.jpg")
            self.netflix_logo = Image.open("netflix.jpg")
        except FileNotFoundError:
            messagebox.showerror("Error", "Image files not found!")
            self.bbc_logo = Image.new("RGB", (150, 150))
            self.nbc_logo = Image.new("RGB", (150, 150))
            self.netflix_logo = Image.new("RGB", (150, 150))

        # Resize images to fit in the GUI
        self.bbc_logo = self.resize_image(self.bbc_logo, 150, 150)
        self.nbc_logo = self.resize_image(self.nbc_logo, 150, 150)
        self.netflix_logo = self.resize_image(self.netflix_logo, 150, 150)

        self.bbc_logo_tk = ImageTk.PhotoImage(self.bbc_logo)
        self.nbc_logo_tk = ImageTk.PhotoImage(self.nbc_logo)
        self.netflix_logo_tk = ImageTk.PhotoImage(self.netflix_logo)

        self.channel_display_frame = tk.Frame(root)
        self.channel_display_frame.pack(pady=10)

        self.channel_image_label = tk.Label(self.channel_display_frame, image=self.bbc_logo_tk)
        self.channel_image_label.grid(row=0, column=0, padx=10)

        self.channel_label = tk.Label(self.channel_display_frame, text="BBC", font=("Helvetica", 20))
        self.channel_label.grid(row=0, column=1)

        self.volume_label = tk.Label(self.channel_display_frame, text="Volume: 0", font=("Helvetica", 15))
        self.volume_label.grid(row=1, column=1)

        # Power status label
        self.power_status_label = tk.Label(self.channel_display_frame, text="Power: Off", font=("Helvetica", 15))
        self.power_status_label.grid(row=2, column=1)

        self.control_panel = tk.Frame(root)
        self.control_panel.pack(pady=20)

        self.power_button = tk.Button(self.control_panel, text="Power", width=12, command=self.toggle_power)
        self.power_button.grid(row=0, column=0, padx=10, pady=5)

        self.mute_button = tk.Button(self.control_panel, text="Mute", width=12, command=self.toggle_mute)
        self.mute_button.grid(row=0, column=1, padx=10, pady=5)

        self.channel_up_button = tk.Button(self.control_panel, text="Channel Up", width=12, command=self.channel_up)
        self.channel_up_button.grid(row=1, column=0, padx=10, pady=5)

        self.channel_down_button = tk.Button(self.control_panel, text="Channel Down", width=12,
                                             command=self.channel_down)
        self.channel_down_button.grid(row=1, column=1, padx=10, pady=5)

        self.volume_up_button = tk.Button(self.control_panel, text="Volume Up", width=12, command=self.volume_up)
        self.volume_up_button.grid(row=2, column=0, padx=10, pady=5)

        self.volume_down_button = tk.Button(self.control_panel, text="Volume Down", width=12, command=self.volume_down)
        self.volume_down_button.grid(row=2, column=1, padx=10, pady=5)

        self.update_labels()

    def resize_image(self, image, width, height):
        """Resize the image to a specified width and height."""
        return image.resize((width, height), Image.Resampling.LANCZOS)

    def update_labels(self):
        # Fetch current TV status, channel, and volume
        status = self.controller.get_tv_status()
        channel = self.controller.tv.get_channel()  # Fetch current channel directly
        volume = self.controller.tv.get_volume()  # Fetch current volume directly
        mute_status = "Muted" if self.is_muted else "Unmuted"

        # Update the channel image and label based on the current channel
        if channel == 0:
            self.channel_image_label.config(image=self.bbc_logo_tk)
            self.channel_label.config(text="BBC")
        elif channel == 1:
            self.channel_image_label.config(image=self.nbc_logo_tk)
            self.channel_label.config(text="NBC")
        elif channel == 2:
            self.channel_image_label.config(image=self.netflix_logo_tk)
            self.channel_label.config(text="Netflix")

        # Update volume and mute status
        self.volume_label.config(text=f"Volume: {volume}")

        # Update power status
        power_status = "On" if self.controller.tv.get_status() else "Off"
        self.power_status_label.config(text=f"Power: {power_status}")

        self.update_power_status()

    def update_power_status(self):
        # Update the window title based on the power status
        power_status = "On" if self.controller.tv.get_status() else "Off"
        self.root.title(f"TV Remote - Power: {power_status}")

    def toggle_power(self):
        # Toggle power without sound
        self.controller.toggle_power()
        self.update_labels()

    def toggle_mute(self):
        # Handle mute/unmute behavior
        if self.is_muted:
            # Unmute the TV and restore the previous volume
            self.controller.tv.__volume = self.previous_volume
            self.is_muted = False
        else:
            # Mute the TV and set volume to 0
            self.previous_volume = self.controller.tv.get_volume()  # Store the current volume
            self.controller.tv.__volume = 0
            self.is_muted = True
        self.update_labels()

    def channel_up(self):
        self.controller.channel_up()
        self.update_labels()

    def channel_down(self):
        self.controller.channel_down()
        self.update_labels()

    def volume_up(self):
        self.controller.volume_up()
        self.update_labels()

    def volume_down(self):
        self.controller.volume_down()
        self.update_labels()


if __name__ == "__main__":
    root = tk.Tk()
    controller = TelevisionController()
    gui = TelevisionGUI(root, controller)
    root.mainloop()
