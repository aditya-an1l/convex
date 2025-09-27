from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from ui.panels import LeftPanel, RightPanel

class LazyGitTUI(App):
    CSS_PATH = "css/lazygit.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield LeftPanel(id="left-panel")
        yield RightPanel(id="right-panel")

    def on_mount(self):
        self.query_one("#left-panel").focus()

if __name__ == "__main__":
    LazyGitTUI().run()
