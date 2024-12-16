class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 2

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = True

    def unmute(self):
        if self.__status:
            self.__muted = False

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):

        if self.__status and not self.__muted:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):

        if self.__status and not self.__muted:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def get_status(self):
        return self.__status

    def get_channel(self):
        return self.__channel

    def get_volume(self):
        return self.__volume

    def __str__(self):
        power_status = "On" if self.__status else "Off"
        mute_status = "Muted" if self.__muted else "Unmuted"
        return f"Power [{power_status}], Channel [{self.__channel}], Volume [{self.__volume}], Mute [{mute_status}]"
