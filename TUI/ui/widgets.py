from textual.widgets import Button

# Example of a custom widget
class ActionButton(Button):
    def __init__(self, label, command=None):
        super().__init__(label)
        self.command = command
