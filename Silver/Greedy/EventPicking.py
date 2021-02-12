class Event:
    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

    def __lt__ (self, other):
        return self.end < other.end

    def __gt__ (self, other):
        return other.__lt__(self)

event1 = Event(0,2, "1st")
event2 = Event(1,3, "2nd")
event3 = Event(3,5, "3rd")
event4 = Event(4,5, "1st")
a = [event1, event2, event3, event4]
a.sort()
count = 1

last_event = 0

for i in range(1, len(a)):
    if a[i].start > a[last_event].end:
        count = count + 1
        last_event = i

print(count)


