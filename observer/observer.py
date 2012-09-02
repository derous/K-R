class Event:
    def __init__(self, msg):
        self.message = msg

class BroadcastEvent(Event):
    pass

class FirstEvent(Event):
    pass

class GroupEvent:
    def __init__(self, msg, target_group):
        self.message = msg
        self.group = target_group
    pass

class observer:
    def __init__(self):
        self.items = []
    def rise(self, sender, event):
        if isinstance(event, BroadcastEvent):
            for item in self.items:
                item.message(sender, event)
        if isinstance(event, FirstEvent):
            self.items[0].message(sender, event)

        if isinstance(event, GroupEvent):
            for item in self.items:
                if isinstance(item, event.group):
                    item.message(sender, event)

class abstract_item:
    def __init__(self, holder):
        self.holder = holder

    def message(self, sender, msg):
        print "object", self, "received the message", msg.message, "from", sender

    def rise_event(self, event):
        self.holder.rise(self, event)

class lamb(abstract_item):
    pass

class dog(abstract_item):
    pass

manager = observer()

for i in range(100):
    manager.items.append(lamb(manager))
    manager.items.append(dog(manager))

#manager.items[6].rise_event(BroadcastEvent("broadcasting"))
#manager.items[6].rise_event(FirstEvent("First object message"))

manager.items[6].rise_event(GroupEvent("to group", abstract_item))
