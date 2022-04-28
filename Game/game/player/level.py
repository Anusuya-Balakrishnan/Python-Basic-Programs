class Level:
    a="public"
    _b="protected"
    __c="private"

    def get(self):
        print("Player1 is now playing now ")

class Level2:
    def getValue(self):
        print("level2 is running")
        print(Level.a)
        print(Level._b)
le=Level2()
le.getValue()
#print(le.a)
#print(le._b)
# print(le.__c)