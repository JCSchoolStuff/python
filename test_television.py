import pytest
from television import *

class Test():

    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert self.t1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.t1.power()
    def test_mute(self):
        self.t1.mute()

    def test_channel_up(self):
        self.t1.channel_up()
    def test_channel_down(self):
        self.t1.channel_down()

    def test_volume_up(self):
        self.t1.volume_up()
    def test_volume_down(self):
        self.t1.volume_down()

if __name__ == '__main__':
    pytest.main()
