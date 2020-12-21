'''
In order to generate the graph we follow the instructions from Alessio Zamboni:

1-install the library is called "rdflib" and according to your Python distribution (Note! Even if this library claims to work for both python2 and 3, in reality, it doesn't; if you install it using python3 you need a small additional step, see point 2 below);

2-just if running python3 you need to locate in your machine the site-package folder of python, enter the rdflib/tools/rdf2dot.py and modify the line in the "import cgi" with "import html as cgi";

3-select a meaningful subset of your dataset to export from Karmalinker, and export it;

4-for each file, you can run 'python -m rdflib.tools.rdf2dot rdffile.ttl>graph.dot' to convert the RDF in a GraphViz format. Substitute 'rdffile' by the name of your rdf file.

5-you can compile the GraphViz format in an image (installing Graphviz first) and running dot -Tpng graph.dot > graph.png 
'''
#In summary:
python -m rdflib.tools.rdf2dot my_rdf_file_name.ttl>graph.dot
dot -Tpng graph.dot > graph.png 
