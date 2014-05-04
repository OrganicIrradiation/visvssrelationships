pyVSSRelationshipPlot
==========================

Plotting the relationships between VSS 2014 abstracts

##Introduction
This is a script that creates a force directed graph of the relationships between VSS 2014 abstract co-authors. It takes a Python dictionary that contains author and title information for the accepted abstracts ("pyVSSRelationshipData.p") and creates a dynamic plot using NetworkX and D3.js.  The force directed graph utilizes a physical simulation of charged particles and links to bring co-authored articles closer.

![Image](images/VSS2014DNAv1.png)

##Prerequisites
You will need Python 2.7.6 and the following libraries (tested versions in parentheses):
* networkx (1.8.1)

D3.js is dynamically loaded for the presentation page.

##Installation & Usage
After you have the prerequisites installed, you should download the folder to your location of choice.  Running the script will generate a "force.json" file in the html subdirectory that has all of the necessary node/link information necessary for D3.js.  Load the index.html file in the html directory to see the dynamic simulation.  Note that since the index.html requires loading a JSON file, you may need to host this on a webserver. To see a live demo, please go to:
* http://steven.cholewiak.com/codeprojects/pyVSSRelationshipPlot/

##Related Resources
* [Force-Directed Graph Example](http://bl.ocks.org/mbostock/4062045)
* [D3.js Force Layout Documentation](https://github.com/mbostock/d3/wiki/Force-Layout)
