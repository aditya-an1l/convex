from textual.widgets import ListView, ListItem, Static
from textual.app import ComposeResult
from textual.widget import Widget
from git_commands import get_branches, get_status

class LeftPanel(ListView):
    def compose(self) -> ComposeResult:
        branches = get_branches()
        for branch in branches:
            yield ListItem(Static(branch))

class RightPanel(Static):
    def on_mount(self):
        self.update(get_status())
