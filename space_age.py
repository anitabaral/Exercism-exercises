class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def spaceAge(self, factor):
        return round(self.seconds/(60 * 60 * 24 * 365.25 * factor), 2)

    def on_earth(self):
        return self.spaceAge(1)

    def on_mercury(self):
        return self.spaceAge(0.2408467)

    def on_venus(self):
        return self.spaceAge(0.61519726)

    def on_mars(self):
        return self.spaceAge(1.8808158)

    def on_jupiter(self):
        return self.spaceAge(11.862615)

    def on_saturn(self):
        return self.spaceAge(29.447498)

    def on_uranus(self):
        return self.spaceAge(84.016846)

    def on_neptune(self):
        return self.spaceAge(164.79132)
