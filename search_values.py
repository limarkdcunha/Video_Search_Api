import pandas as pd

class Node():
    def __init__(self):
        self.data= {}
        self.end = False

class Trie():
    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return Node()

    def insert(self,word):
        root=self.root
        for i in list(word):
            if not root.data.get(i):
                root.data[i] = self.getNode()
            root = root.data[i]

        root.end = True
#-----------------------------------------------------------------------------------------------

    def traverse(self, node, temp, final):
        if node.end == True:
            final.append(temp)

        for i,j in node.data.items():
            self.traverse(j,temp + i, final)
#-----------------------------------------------------------------------------------------------

    def search_function(self,key):
        root=self.root
        final=[]
        temp = ''
        flag=False

        for i in list(key):
            if not root.data.get(i):
                flag=True
                break
            temp +=i
            root=root.data[i]

        if flag:
            return 0
        elif root.end and not root.data:
            return -1

        self.traverse(root,temp,final)

        return final

#------------------------------------------------------------------------
#Getting the data from csv file
def get_list():
    video_data = pd.read_csv('whc-sites-2019.csv')
    video_data['name_en'] = video_data['name_en'].str.lower()

    video_list = video_data['name_en'].tolist()

    return video_list

#Function to be called from API
def results(name):
    names_list =  get_list()
    n_len = len(names_list)

    #Object of the class Trie
    t = Trie()


    #Insertion of words from into trie from names_list
    for i in range(n_len):
        t.insert(names_list[i])

    final_list = t.search_function(name)

    if(final_list == 0):
        return 'No Results Found'
    else:
        final_values = { i : final_list[i]  for i in range(len(final_list)) }
        return final_values
