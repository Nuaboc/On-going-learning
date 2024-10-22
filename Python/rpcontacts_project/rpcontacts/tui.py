from textual.app import App
from textual.widgets import Footer, Header

class ContactsApp(App):
    BINDINGS = [
        ("m","toogle_dark", "Toogle dark mode"),
    ]
    
    def compose(self):
        """Textual automatically calls this method when you run the app.
        With this method, you can build the app’s main screen. For now,
        your app will only have a header and a footer, which you’ll create
        with the Header and Footer classes that are built into Textual."""
        yield Header()
        yield Footer()

    def on_mount(self):
        """This also called automatically. In this method, you set up some properties
        of your main screen, like the title and subtitle. With this, you have
        the skeleton TUI for your app."""
        self.title = "Contacts"
        self.sub_title = "A Contacts Book App With Textual & Python"

    def action_toggle_dark(self):
        self.dark = not self.dark