# Generates a dot file of the happy and ``melancoil'' numbers, as shown in the
# Numberphile video ``145 and then Melancoil''
# See https://youtu.be/_DpzAvb3Vk4

import sys

def happificate(n):
    sum = 0
    while n > 0:
        digit = n % 10
        n //= 10
        sum += digit ** 2

    return sum

def happificateRange(begin, end):
    graph = {}

    for n in range(begin, end + 1):
        if n not in graph:
            result = happificate(n)
            graph[n] = result

            while result > end and result not in graph:
                n = result
                result = happificate(n)
                graph[n] = result

    return graph

def seperate(graph):
    happy = []
    unhappy = []

    for k in graph:
        next = graph[k]
        path = [k]

        while next != 1 and next not in path:
            path.append(next)
            next = graph[next]

        if next == 1:
            happy.append(k)
        else:
            unhappy.append(k)

    return (happy, unhappy)



def graphToDot(graph):

    happy, unhappy = seperate(graph)

    print("digraph {")

    print("\tsubgraph cluster_happy {")
    print("\t\tgraph [label=\"Happy Numbers\", style=dotted];")


    for k in happy:
        print("\t\tn{0} [label=\"{0}\"];".format(k))
        print("\t\tn{0} -> n{1};".format(k, graph[k]))

    print("\t}")

    print("\tsubgraph cluster_melancoil {")
    print("\t\tgraph [label=\"Melancoil\", style=dotted];")

    for k in unhappy:
        print("\t\tn{0} [label=\"{0}\"];".format(k))
        print("\t\tn{0} -> n{1};".format(k, graph[k]))
    print("\t}")

    print("}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {0} MAXIMUM".format(sys.argv[0]))
        print("Create a graph of the happy numbers from 1 to MAXIMUM")
    
    graphToDot(happificateRange(1, int(sys.argv[1])))
