import tkinter as tk
from interactive_story_plugin import InteractiveStoryPlugin

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.story_plugin = InteractiveStoryPlugin()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Enter your story input:")
        self.input_label.grid(row=0, column=0)

        self.input_entry = tk.Entry(self)
        self.input_entry.grid(row=0, column=1)

        self.submit_button = tk.Button(self, text="Submit", command=self.update_story)
        self.submit_button.grid(row=1, column=0, columnspan=2)

        self.story_output = tk.Text(self, width=50, height=10)
        self.story_output.grid(row=2, column=0, columnspan=2)
        self.story_output.insert(tk.END, "Start your story...")

    def update_story(self):
        user_input = self.input_entry.get()
        self.story_plugin.user_input(user_input)
        scene_description = self.story_plugin.describe_scene()
        self.story_output.insert(tk.END, "\n" + scene_description)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
