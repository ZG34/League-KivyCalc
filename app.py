import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

from calc import Calculator

kivy.require("2.1.0")

calc = Calculator()


class MenuScreen(Screen):
    pass


class ResistValScreen(Screen):
    result = ObjectProperty(None)
    damage = ObjectProperty(None)
    resists = ObjectProperty(None)

    def calculate(self):
        outcome = calc.resists(self.damage.text, self.resists.text)
        if outcome is False:
            self.result.text = "Please enter damage and resists"
        else:
            self.result.text = (
                str(outcome)
                + f" damage taken,\nafter {self.damage.text} damage\napplied vs"
                f" {self.resists.text} resists"
            )


class EhpScreen(Screen):
    result = ObjectProperty(None)
    resists = ObjectProperty(None)
    health = ObjectProperty(None)

    def calculate(self):
        outcome = calc.ehp(self.resists.text, self.health.text)
        if outcome is False:
            self.result.text = "Please enter resists and health"
        else:
            self.result.text = (
                "You have\n"
                + str(outcome)
                + f"\neffective health vs a given damage type"
            )


class CalcInterface(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ResistValScreen(name="resists"))
        sm.add_widget(EhpScreen(name="ehp"))

        return sm


if __name__ == "__main__":
    CalcInterface().run()
