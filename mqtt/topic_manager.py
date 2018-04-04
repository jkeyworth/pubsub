class TopicManager:
    def __init__(self, domain, room):
        self.__domain = domain
        self.__room = room

    def get_topic(self, device):
        return self.__domain + '/' + self.__room + '/' + device


if __name__ == "__main__":
    tm = TopicManager("a", "b")
    assert (tm.get_topic("c") == "a/b/c")
