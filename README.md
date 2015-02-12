visvssrelationships
==========================

Plotting the relationships between VSS 2015 abstracts

##Introduction
This is some code that creates a force directed graph of the relationships between VSS 2015 abstract co-authors. It takes a Python dictionary that contains author and title information for the accepted abstracts (```visvssrelationships_data_2015.p```) and creates a dynamic plot using NetworkX and D3.js.  The force directed graph utilizes a physical simulation of charged particles and links to bring co-authored articles closer.

![Image](images/VSS2015DNA.png)

##Prerequisites
You can run these in iPython. Here are the tested library requirements:

* beautifulsoup4==4.3.2
* decorator==3.4.0
* ipy-progressbar==1.0.2
* networkx==1.9.1

D3.js is dynamically loaded for the presentation page.

##Installation & Usage
Running the iPython script will generate a "force.json" file in the html subdirectory that has all of the necessary node/link information necessary for D3.js.  Load the index.html file in the html directory to see the dynamic simulation.  Note that since the index.html requires loading a JSON file, you may need to host this on a webserver. To see a live demo, please go to:
* http://steven.cholewiak.com/code/visvssrelationships_2015/

##Related Resources
* [Force-Directed Graph Example](http://bl.ocks.org/mbostock/4062045)
* [D3.js Force Layout Documentation](https://github.com/mbostock/d3/wiki/Force-Layout)
