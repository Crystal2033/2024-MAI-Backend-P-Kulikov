from LRU.BiLinkedList import BiLinkedList
from LRU.LRUCache import LRUCache


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # myList = BiLinkedList()
    # node1 = myList.add(1, 100)
    # node2 = myList.add(2, 200)
    # node3 = myList.add(3, 300)
    # node4 = myList.add(4, 400)
    #
    # print(myList.remove(node4))
    # print(myList.remove(node1))
    # print(myList.remove(node2))
    # print(myList.remove(node3))
    # print("Okay")
    lruCache = LRUCache(4)
    lruCache.set("key1", "value1")
    lruCache.set("key2", "value2")
    lruCache.set("key3", "value3")
    lruCache.set("key4", "value4")
    lruCache.set("key5", "value5")

    lruCache.rem("key3")

    print(lruCache.get("key3"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
