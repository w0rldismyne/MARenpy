init python:
    class Character_Stats:
        def __init__(self):
            self._Vigor = 0
            self._Charm = 0
            self._Intelligence = 0
            self._Vision = 0

        @property
        def Vigor(self):
            return self._Vigor

        @property
        def Charm(self):
            return self._Charm

        @property
        def Intelligence(self):
            return self._Intelligence

        @property
        def Vision(self):
            return self._Vision

        def Recalibrate(self):
            pass