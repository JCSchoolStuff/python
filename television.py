class Television:
    """
    A class representing a television
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to set default values for Television
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method that changes the value of the status variable
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self) -> None:
        """
        Method that changes the value of the muted variable
        :return:
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method that increases the value of the channel variable
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        """
        Method that decreases the value of the channel variable
        :return:
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method that increases the value of the volume variable
        :return:
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
    def volume_down(self) -> None:
        """
        Method that decreases the value of the volume variable
        :return:
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self):
        """
        Method that returns a string representation of the object
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'