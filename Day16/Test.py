class Robot:
    def introduce_self(self):
        print("My weight is " + self.name )

r1 = Robot()
r1.namee = "Tom"
r1.color = "red"
r1.weight = 30

r1.introduce_self()