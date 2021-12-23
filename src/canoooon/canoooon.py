class Canon:
    def __init__(self):
        self._name = "Canon"

    def greet(self):
        print("こんにちは〜{}です！".format(self._name))

    @property
    def name(self):
        return self._name

    @property
    def favorite_artists(self):
        return [
            "BABYMETAL (all)",
            "MAMAMOO (MoonByul, Solar)",
            "IZ*ONE (YURI)",
            "B'z",
            "SPEED (hiro)",
            "玉置浩二",
            "小田和正",
            "Surface",
        ]