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
    # lruCache = LRUCache(2)
    # lruCache.set("2", "1")
    # lruCache.set("1", "1")
    # print(lruCache.get("2"))
    #
    # lruCache.set("4", "1")
    # print(lruCache.get("1"))
    # print(lruCache.get("2"))
    #lruCache.set("2", "2")

    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    print(cache.get('Jesse'))  # вернёт 'James'
    cache.rem('Walter')
    print(cache.get('Walter'))  # вернёт ''



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
