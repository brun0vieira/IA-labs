package com.company;
import undirectedgraph.Graph;
import undirectedgraph.Romenia;
import searchalgorithm.Node;
import searchalgorithm.Algorithms;
import undirectedgraph.Vertex;

public class Main {

    public static void main(String[] args) {
        Graph graph = Romenia.defineGraph();
        graph.showLinks();
        graph.showSets();
        /*Node n;
        n = graph.searchSolution("Arad", "Bucharest", Algorithms.BreadthFirstSearch, "Oltenia");
        graph.showSolution(n);
        */
        String[] regions = new String[]{"Dobrogea"};
        graph.searchSolution("Arad", "Bucharest", Algorithms.BreadthFirstSearch, regions);

    }
}
