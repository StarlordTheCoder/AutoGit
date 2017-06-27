import sched, time

class Automation:

    def __init__(self):
        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(1, 1, self.do_something)
        self.s.run()

    def do_something(self):
        print("Doing stuff...")
        # do your stuff
        self.s.enter(1, 1, self.do_something)

auto = Automation()