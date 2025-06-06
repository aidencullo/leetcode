class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        return sum((1 for ping in self.pings if ping >= t - 3000))
