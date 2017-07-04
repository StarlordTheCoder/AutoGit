import sched, time


class Automation:
    """
    Klasse welches das regelmässige ausführen von einer Aktion erlaubt
    """

    def __init__(self, action, timeout_in_seconds):
        self.action = action
        self.timeout_in_seconds = timeout_in_seconds
        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(self.timeout_in_seconds, 1, self.execute_action)
        self.s.run()

    def execute_action(self):
        print("Executing action...")

        self.action()

        self.s.enter(self.timeout_in_seconds, 1, self.execute_action)