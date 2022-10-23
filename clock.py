import time

class Clock:
    def __init__(self) -> None:
        self.time_ = 0

    def start(self):
        self.time_ = time.time()

    def update(self):
        self.final = time.time() - self.time_

    def hide(self):
        self.hours = int(self.final//3600)
        self.final = self.final%3600
        self.minutes = int(self.final//60)
        self.final = self.final%60
        self.seconds = int(self.final)
        self.mil = int((self.final - self.seconds) *100)



