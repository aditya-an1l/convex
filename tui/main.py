from textual.app import App,ComposeResult
from textual.widgets import Header, Footer

class TUI(App):
    """"A TUI for convex"""

    BINDINGS = [
        ("d","toggle_dark","Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = TUI()
    app.run()
