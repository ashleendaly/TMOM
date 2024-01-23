from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Header, Button, Static, Digits
from datetime import datetime as dt

class Actions(Static):

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Pause", id="pause", variant="error")
        yield Button("Reset", id="reset")


class tEMOM(App):

    CSS_PATH = "global.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            yield Digits("", id="timer")
        with Center():
            yield Actions()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = dt.now().time()
        self.query_one(Digits).update(f"{clock:%T}")

if __name__ == "__main__":
    app = tEMOM()
    app.run()