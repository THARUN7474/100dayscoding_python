n = int(input())
sequences = []
for _ in range(n):
    line = input().split()
    m = int(line[0])
    values = line[1:]
    sequences.append(values)

p = int(input())
changes = []
for _ in range(p):
    old_password, new_password = input().split()
    changes.append((old_password, new_password))

def is_reject(old_password, new_password):
    for sequence in sequences:
        if old_password in sequence and new_password in sequence:
            return "REJECT"
    return "OK"

for old_password, new_password in changes:
    result = is_reject(old_password, new_password)
    print(result)

from collections import defaultdict
from queue import Queue

# Read the input
n = int(input())
graph = defaultdict(list)
in_degree = defaultdict(int)

# Process the input and build the graph
for _ in range(n):
    line = input().split()
    p1, relation, p2 = line
    if relation == "->":
        graph[p1].append(p2)
        in_degree[p2] += 1

# Perform topological sort to find possible sources
sources = []
queue = Queue()

# Initialize the queue with nodes that have in-degree 0
for node in graph.keys():
    if in_degree[node] == 0:
        queue.put(node)

while not queue.empty():
    node = queue.get()
    sources.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.put(neighbor)

# Sort the sources alphabetically
sources.sort()

# Output the possible sources
for source in sources:
    print(source)
