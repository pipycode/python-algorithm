class Node(object):
    def __init__(self, value, flag=None):
        self.value = value
        self.flag = flag
        
        self.parent = None
        self.child = {}
        
class trie:
    def __init__(self):
        self.head = Node('$') # start token
        
    def insert(self, word):
        pointer = self.head
        check, result = True, 0
        for i, alphabet in enumerate(word):
            if alphabet not in pointer.child:
                pointer.child[alphabet] = Node(alphabet)
                pointer.child[alphabet].parent = pointer
                if check:
                    check=False
                    result=i
            pointer = pointer.child[alphabet]
        pointer.flag = word
        return result

def solution(words):
    words.sort()
    words.append(';') # End token
    word_tree = trie()
    word_tree.insert(words[0])
    
    answer = 0
    before = 0
    for i, word in enumerate(words[1:]):
        temp = word_tree.insert(word)
        if temp == len(words[i]):
            answer += temp
        elif temp <= before:
            answer += (before+1)
        else:
            answer += (temp+1)
        before = temp
    
    
    return answer