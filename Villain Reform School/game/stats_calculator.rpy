init python:
    class Character_Stats:
        def __init__(self):
            self._ATK = 0
            self._HP = 0
            self._SECONDARY = 0

        @property
        def ATK(self):
            return self._ATK

        @property
        def HP(self):
            return self._HP

        @property
        def Secondary(self):
            return self._SECONDARY

        def AutoConfigure(self):

            self._ATK = 0
            self._HP = 0
            self._SECONDARY = 0

            if Intel >= Vigor:
                self._HP += 1
            else:
                self._ATK += 1

            if Intel >= Charm:
                self._HP += 1
            else:
                self._SECONDARY += 1

            if Vigor >= Charm:
                self._ATK += 1
            else:
                self._SECONDARY += 1

            if self._HP == 2:
                self._HP = 24
            elif self._HP == 1:
                self._HP = 16
            else:
                self._HP = 12
            
            if self._ATK == 2:
                self._ATK = 8
            elif self._ATK == 1:
                self._ATK = 6
            else:
                self._ATK = 4

            if self._SECONDARY == 2:
                self._SECONDARY = 12
            elif self._SECONDARY == 1:
                self._SECONDARY = 8
            else:
                self._SECONDARY = 6