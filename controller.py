from television import Television

class TelevisionController:
    def __init__(self):
        self.tv = Television()

    def toggle_power(self):
        self.tv.power()

    def toggle_mute(self):
        if self.tv.get_status():
            if self.tv.get_volume() > 0:
                self.tv.mute()
            else:
                self.tv.unmute()

    def channel_up(self):
        if self.tv.get_status():
            self.tv.channel_up()

    def channel_down(self):
        if self.tv.get_status():
            self.tv.channel_down()

    def volume_up(self):
        if self.tv.get_status():
            self.tv.volume_up()

    def volume_down(self):
        if self.tv.get_status():
            self.tv.volume_down()

    def get_tv_status(self):
        return str(self.tv)
