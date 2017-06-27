import sched, time


class Automation:

    def __init__(self, action, timeout_in_seconds):
        self.action = action
        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(timeout_in_seconds, 1, self.execute_action)
        self.s.run()

    def execute_action(self):
        print("Executing action...")

        self.action()

        self.s.enter(1, 1, self.execute_action)