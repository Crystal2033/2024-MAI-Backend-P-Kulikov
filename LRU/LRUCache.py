from LRU.BiLinkedList import BiLinkedList


class LRUCache:

    biLinkedList = None

    capacity = 0

    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.biLinkedList = BiLinkedList()
        self.mapWithLinksToNodes = {}

    def get(self, key: str) -> str:
        if key not in self.mapWithLinksToNodes:
            return ""
        else:
            foundedKeyValue = self.biLinkedList.remove(self.mapWithLinksToNodes[key])
            self.mapWithLinksToNodes[key] = self.biLinkedList.add(foundedKeyValue[0], foundedKeyValue[1])
            return foundedKeyValue[1]

    def set(self, key: str, value: str) -> None:
        if key not in self.mapWithLinksToNodes:
            self.mapWithLinksToNodes[key] = self.biLinkedList.add(key, value)
            if len(self.mapWithLinksToNodes.keys()) > self.capacity:
                deletedKeyValue = self.biLinkedList.remove_elder_element()
                self.mapWithLinksToNodes.pop(deletedKeyValue[0])
        else:
            self.biLinkedList.remove(self.mapWithLinksToNodes[key])
            self.mapWithLinksToNodes[key] = self.biLinkedList.add(key, value)

    def rem(self, key: str) -> None:
        self.biLinkedList.remove(self.mapWithLinksToNodes[key])
        self.mapWithLinksToNodes.pop(key)
