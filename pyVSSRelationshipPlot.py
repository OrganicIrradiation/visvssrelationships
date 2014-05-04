import networkx as nx
import cPickle
import json
from networkx.readwrite import json_graph

# Load our preprocessed abstract data
PROCESSQUEUEPATH = 'pyVSSRelationshipData.p'
f = open(PROCESSQUEUEPATH, "r")
ourDict = cPickle.load(f)
testedNums = cPickle.load(f)
f.close()

# Loop through each abstract and add edges between the authors' names
# and the title of the abstract.
G = nx.Graph()
for abstract in ourDict:
    title = ourDict[abstract]['title']
    print 'Processing Abstract #'+str(abstract),title
    
    for author in ourDict[abstract]['authors']:
        G.add_edge(author,title)
        if not 'group' in G.node[author]:
            G.node[author]['group'] = 1
        
    firstAuthor = ourDict[abstract]['authors'][0]
    G.node[firstAuthor]['group'] = 2
    G.node[title]['group'] = 3

# Loop through all the nodes and add the name property for D3.js
for n in G:
    G.node[n]['name'] = n

# Remove parallel edges
G = nx.Graph(G)
# Remove self loops
G.remove_edges_from(G.selfloop_edges())

# Export for D3.js
d = json_graph.node_link_data(G) # node-link format to serialize
json.dump(d, open('html/force.json','w'))

# Use NetworkX to plot the data (I've had limited success)
#import matplotlib.pyplot as plt
#pos=nx.spring_layout(G) # positions for all nodes
#nx.draw_networkx_nodes(G,pos,node_size=2,alpha=0.5)
#nx.draw_networkx_edges(G,pos,alpha=0.25)
#nx.draw_networkx_labels(G,pos,font_size=7,font_family='sans-serif')
#plt.axis('off')
#plt.show() # display
