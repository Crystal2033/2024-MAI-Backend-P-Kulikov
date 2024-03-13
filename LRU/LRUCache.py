from LRU.BiLinkedList import BiLinkedList


class LRUCache:

    biLinkedList = None
    mapWithLinksToNodes = {}
    capacity = 0

    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.biLinkedList = BiLinkedList()

    def get(self, key: str) -> str:
        if key not in self.mapWithLinksToNodes:
            return "None"
        else:
            return self.mapWithLinksToNodes[key].getValue()

    def set(self, key: str, value: str) -> None:
        if key not in self.mapWithLinksToNodes:
            self.mapWithLinksToNodes[key] = self.biLinkedList.add(key, value)
            if len(self.mapWithLinksToNodes) > self.capacity:
                deletedKey = self.biLinkedList.removeOlderElement()
                self.mapWithLinksToNodes.pop(deletedKey)
        else:
            self.biLinkedList.remove(self.mapWithLinksToNodes[key])
            self.biLinkedList.add(key, value)

    def rem(self, key: str) -> None:
        self.biLinkedList.remove(self.mapWithLinksToNodes[key])
        self.mapWithLinksToNodes.pop(key)
