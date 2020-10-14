package com.company;
import undirectedgraph.Graph;
import undirectedgraph.Romenia;
import searchalgorithm.Node;
import searchalgorithm.Algorithms;
import undirectedgraph.Vertex;

public class Main {

    public static void main(String[] args) {
        Graph graph = Romenia.defineGraph();
        Node n;
        String[] regions = new String[]{"Dobrogea"}; // regioes intermedias
        //graph.showLinks();
        //graph.showSets();
        //n = graph.searchSolution("Arad", "Bucharest", Algorithms.BreadthFirstSearch);
        //graph.showSolution(n);

        n = graph.searchSolution("Arad", "Bucharest", Algorithms.AStarSearch, regions);
        graph.showSolution(n);
    }
}
