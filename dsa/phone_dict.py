class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.isWordEnd = False

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()

  def print(self):
    for child in self.root.children:
      print(child)

  def insert(self, word: str):
    node = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.isWordEnd = True

  def searchUtil(self, node: TrieNode, prefix: str):
    print("searching for :", prefix)
    curNode = node
    for c in prefix:
      if c not in node.children:
        return False
      curNode = node.children[c]
    return curNode.isWordEnd

  def search(self, word: str):
    prefix = ''
    curNode = self.root
    for c in word:
      prefix += c
      if(self.searchUtil(curNode, prefix)):
        print(prefix)

class PhoneDict:
  def __init__(self, contacts) -> None:
    self.trie = Trie()
    for contact in contacts:
      self.trie.insert(contact)

  def search(self, query):
    self.trie.search(query)

phoneDict = PhoneDict(["gforgeeks","geeksquiz"])
print(phoneDict.search('gekk'))