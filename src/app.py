from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Static, Button

# class TimeDisplay(Static):

class Timer(Static):

    def compose(self) -> ComposeResult:
        # yield TimeDisplay("10:00")
        yield Button("Start", id="start", variant="success")
        yield Button("Pause", id="pause", variant="error")
        yield Button("Reset", id="reset")


class tEMOM(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(Timer())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = tEMOM()
    app.run()