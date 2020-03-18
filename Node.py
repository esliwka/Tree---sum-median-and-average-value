from statistics import median

class Node:
    def __init__(self, value=0, parent=None):
        self.__parent__ = parent
        self.__children__ = []
        self.value = value

    def isRoot(self):
        if self.__parent__ == None: return True
        return False

    def isNode(self):
        if len(self.__children__) > 0: return True
        return False

    def getParent(self):
        return self.__parent__

    def getChildren(self):
        return self.__children__

    def getNext(self):
        if self.__parent__ == None: return None
        n = self.__parent__.getChildren()
        this = False
        for child in n:
            if this and child != self:
                return child
            if child == self:
                this = True
        return None

    def getPrev(self):
        if self.__parent__ == None: return None
        n = self.__parent__.getChildren()
        p = None
        for child in n:
            if child == self:
                return p
            p = child
        return None

    def removeChild(self, remove):
        if remove in self.__children__:
            self.__children__.remove(remove)

    def setParent(self, newParent):
        if newParent.__class__ != Node: return None
        if self.__parent__ != None:
            self.__parent__.removeChild(self)
        self.__parent__ = newParent
        newParent.addChild(self)

    def addChild(self, newChild):
        if newChild.__class__ != Node: return None
        if newChild in self.__children__: return None
        if newChild.getParent() != None:
            newChild.getParent().removeChild(newChild)
        self.__children__.append(newChild)
        newChild.__parent__ = self

    def getRoot(self):
        root = self
        while root.isRoot() == False:
            root = root.getParent()
        return root

    def printTree(self, intend=0):
        p = ""
        i = intend
        while i > 0:
            if i > 1: p += "    +"
            else: p += "    "
            i -= 1  
        if (self.isNode()):
            print(p + "+" + str(self.value))  #jeśli ma dzieci, rysuje +
        else:
            print(p + "-" + str(self.value)) #nie posiada, -
        for c in self.getChildren():
            c.printTree(intend + 1)

    def getTreeAsArray(self, treeList = []):
        treeList.append(self.value)
        if (self.isNode()):
            for c in self.getChildren():  #dla każdego dziecka
                  c.sumTreeValues()
        else:
            return self.value
        return subtreeSum

    def sumTreeValues(self):
        subtreeSum = self.value
        if (self.isNode()):
            for c in self.getChildren():  #dla każdego dziecka
                subtreeSum += c.sumTreeValues()
        else:
            return self.value
        return subtreeSum

    def treeSize(self):
        nodeCount = 1
        if (self.isNode()):
            for c in self.getChildren():  #dla każdego dziecka
                nodeCount += c.treeSize()
        else:
            return 1
        return nodeCount

    def avgValue(self):
        return self.sumTreeValues() / self.treeSize()

    def __getTreeAsArrayInternal(self, array):
        array.append(self.value)
        if self.isNode():
            for c in self.getChildren():  # dla każdego dziecka
                c.__getTreeAsArrayInternal(array)

        return array

    def getTreeAsArray(self):
        treeAsArray = []
        self.__getTreeAsArrayInternal(treeAsArray)
        return treeAsArray

    def medianValue(self):
        tree = self.getTreeAsArray()
        tree.sort()

        return median(tree)