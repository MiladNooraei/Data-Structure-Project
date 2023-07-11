#Opening text file
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

#Getting Resturansts and Distances and Queries from user
resturants, k, s = [], [], []
for i in range(1, 801):
    rd = lines[i].split()
    resturants += [[rd[0], int(rd[1])]]

for j in range(802, 1002):
    ks = lines[j].split()
    k += [int(ks[0])]
    s += [ks[1]]

#Building Trie Data Structure
class TrieTree:
    
    def __init__(self):
        
        self.root = {}
    
    def insert(self, word):
        
        current_node = self.root
        #cheking if it already exist
        #if not insert
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["*"] = True
    
    #searching for word
    def search(self, word, ran):
        
        current_node = self.root
        
        #if not exist return no resturant
        
        for char in word:
            if char not in current_node:
                return "NO restaurant found!"
            #otherwise find node
            
            current_node = current_node[char]
            
        node = Queries[0:ran]
        
        #if it exist go through node
        #make a list of resturants with same s
        #use ascii value to find the min of next letter
        if "*" in str(current_node):
            
            #initalize with 122(z)
            ascii_code = 122
            
            for i in node:
                
                
                #find letter with min ascii value
                
                if i.startswith(word) and ord(i[len(word)]) < ascii_code:
                    ascii_code = ord(i[len(word)])
                    x = i
                    
                    return x
        
        else:
            return "NO restaurant found!"
    


#Heapify function
def heapify(array, N, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if (left < N) and (array[left][1] < array[smallest][1]):
        smallest = left
        
    if (right < N) and (array[right][1] < array[smallest][1]):
        smallest = right
        
    if smallest != i:
        (array[i], array[smallest]) = (array[smallest], array[i])
        
        heapify(array, N, smallest)

#Sorting min heap
def heapSort(array, N, hcounter):
    
    for i in range(N-1, hcounter, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

#Buildng Heap
flag = True
Queries = []
mini = 0
N = len(resturants)

for i in range(int(N / 2)-1, -1, -1):
    heapify(resturants, N, i)

#sorting based on k
def new_sort(flag, number, hcounter):
    
    global Queries
    
    if flag:
        full = max(k)
        
        hcounter = N - (full + 2)
        
        heapSort(resturants, N, hcounter)
        
        for i in range(1, full+1):
            Queries += [resturants[-i][0]]

#Building Trie and doing the action
tr = TrieTree()

def build_Trie(number, last_number, Queries, s):
    
    if number > last_number:
        global flag
        global mini
        
        hcounter = mini
        new_sort(flag, number, hcounter)
        flag = False
        
        for i in range(last_number, number):
            tr.insert(Queries[i])
        mini = number
        
    elif number == last_number:
        pass
    
    result = tr.search(s, number)
    if result == None:
        print("NO restaurant found!")
    else:
        print(result)
    
#Moving on k list which contains k close resturants
last_k = 0
counter = 0
for i in k:
    build_Trie(i, last_k, Queries, s[counter])
    counter += 1
    last_k = i