
class Time:
    def __init__(self, time_in, time_out):
        self.time_in, self.time_out = time_in, time_out

    def __str__(self):
        return f"{self.time_in}:{self.time_out}"

class Node:
    def __init__(self, val):
        self.val = val
        self.time = Time(0,0)
        self.neighbors = []
        self.is_processed = False
        self.is_discovered = False

    def __str__(self):
        return f"{self.val}, Time: {self.time}"

class Dfs:
    def __init__(self, graph):
        self.curr_time = 0
        self.parent_of = {}
        self.graph = {}
        for key in graph.keys():
            self.graph[key] = Node(key)

        for key, edges in graph.items():
            for edge in edges:
                self.graph[key].neighbors.append(self.graph[edge])


    def dfs(self, node: Node):
        self.curr_time += 1
        node.is_discovered = True
        node.time.time_in = self.curr_time

        for neighbor in node.neighbors:
            if not neighbor.is_discovered: # edge!
                neighbor.is_discovered = True
                self.parent_of[neighbor.val] = node.val
                self.process_edge(node, neighbor)
                self.dfs(neighbor)
            elif not neighbor.is_processed: # back-edge!
                self.process_edge(node, neighbor, True)

        node.is_processed = True
        self.curr_time += 1
        node.time.time_out = self.curr_time


    def process_edge(self, source, sink, is_back=False):
        if is_back:
            if self.parent_of.get(source.val, None) != sink.val:
                print(f"PURE BACK-EDGE: {source.val} --> {sink.val}")
            else:
                print(f"BACK-EDGE: {source.val} --> {sink.val}")
        else:
            print(f"{source.val} --> {sink.val}")

    def process_node_early(self):
        pass

    def process_node_late(self):
        pass

if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f", "g"],
        "e": ["h"],
        "f": ["b"],
        "g": ["e"],
        "h": []
    }

    dfs = Dfs(graph)
    dfs.dfs(dfs.graph["a"])
    for key, item in dfs.graph.items():
        print(f"{key}: {item}")
    print(dfs.parent_of)
