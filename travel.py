

import heapq

def dijkstra(graph, start, end):
    """
    Finds the shortest path between start and end nodes in a weighted graph using Dijkstra's algorithm.
    :param graph: Dictionary representing the graph {node: [(neighbor, weight), ...]}
    :param start: Starting node
    :param end: Destination node
    :return: (path, cost) where path is the list of nodes and cost is the total weight
    """
    priority_queue = [(0, start, [])]  # (cost, current_node, path)
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        path = path + [current_node]

        if current_node == end:
            return path, cost

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return None, float('inf')

def add_route(graph, source, destination, weight):
    """ Adds a route to the graph. """
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append((destination, weight))
    graph[destination].append((source, weight))  # Remove this line for directed graphs

def display_routes(graph):
    """ Display all routes in the graph. """
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

if __name__ == "__main__":
    # Graph representation
    graph = {}

    print("Travel Planner")
    while True:
        print("\nOptions:")
        print("1. Add a route")
        print("2. Find shortest path")
        print("3. Display routes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source = input("Enter source location: ")
            destination = input("Enter destination location: ")
            weight = float(input("Enter distance/time/cost (as weight): "))
            add_route(graph, source, destination, weight)

        elif choice == "2":
            start = input("Enter starting location: ")
            end = input("Enter destination location: ")
            path, cost = dijkstra(graph, start, end)
            if path:
                print(f"Shortest path: {' -> '.join(path)} with total cost: {cost}")
            else:
                print("No path found.")

        elif choice == "3":
            display_routes(graph)

        elif choice == "4":
            print("Exiting the Travel Planner. Safe travels!")
            break

        else:
            print("Invalid choice. Please try again.")
