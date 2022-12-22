import sys
from heapq import heapify, heappush, heappop

A = "College Square"
B = "Lewis Science Center"
C = "Computer Science"
D = "Prince Center"
E = "Torreyson Library"
F = "Burdick"
G = "Speech Language Hearing"
H = "Maintenance College"
I = "Old Main"
J = "Fine Art"
K = "Police Dept."
L = "McALister Hall"
M = "Wingo"
N = "Student Center"
O = "Student Health Center"
P = "New Business Building"
Q = "Oak Tree Apt."
R = "Brewer-Hegeman"
S = "Bear village Apt."


def bellmanford(graph, src, dest, data):
    inf = sys.maxsize

    last = [dest]
    data[src]['cost'] = 0

    for i in range(17):
        for it in graph:
            for neighbor in graph[it]:
                cost = data[it]['cost'] + graph[it][neighbor]
                if cost < data[neighbor]['cost']:
                    data[neighbor]['cost'] = cost
                    if data[neighbor]['cost'] == inf:
                        data[neighbor]['pre'] = data[it]['pre'] + [it]
                    else:
                        data[neighbor]['pre'].clear()
                        data[neighbor]['pre'] = data[it]['pre'] + [it]

    print("Shortest Distance: " + str(data[dest]['cost']))
    print("Shortest Path: " + str(data[dest]['pre'] + last))


def dijsktra(graph, src, dest, data):
    inf = sys.maxsize

    data[src]['cost'] = 0
    last = [dest]
    visited = []
    temp = src
    for i in range(17):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = data[temp]['cost'] + graph[temp][j]
                    if cost < data[j]['cost']:
                        data[j]['cost'] = cost
                        data[j]['pre'] = data[temp]['pre'] + [temp]
                    heappush(min_heap, (data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(data[dest]['cost']))
    print("Shortest Path: " + str(data[dest]['pre'] + last))


if __name__ == "__main__":
    inf = sys.maxsize

    graph = {
        A: {B: 200, D: 300},
        B: {G: 250, A: 200, C: 150},
        C: {B: 150, E: 40, D: 80, F: 30},
        D: {C: 80, E: 30, A: 300, K: 100},
        E: {C: 40, D: 30, F: 80, I: 30},
        F: {C: 30, G: 100, E: 80, L: 200, H: 300},
        G: {B: 250, F: 100, H: 120},
        H: {G: 120, F: 300, L: 150, M: 100, P: 150, Q: 160},
        I: {E: 30, J: 90, K: 200, L: 100},
        J: {I: 90, K: 50, F: 1, L: 180, N: 80},
        K: {D: 100, I: 200, J: 50, O: 100},
        L: {F: 200, I: 100, J: 180, N: 100, M: 50, H: 150},
        M: {L: 50, N: 100, P: 50, H: 100},
        N: {J: 80, O: 50, L: 100, M: 100, P: 110},
        O: {K: 100, N: 50, R: 200},
        P: {M: 50, N: 110, R: 20, Q: 30, H: 150},
        Q: {H: 150, P: 30, R: 40},
        R: {O: 200, P: 20, Q: 40, S: 350},
        S: {R: 350}

    }

    info = {A: {'cost': inf, 'pre': []},  # College Square
            B: {'cost': inf, 'pre': []},  # lewis
            C: {'cost': inf, 'pre': []},  # computer
            D: {'cost': inf, 'pre': []},  # prince
            E: {'cost': inf, 'pre': []},  # torreyson
            F: {'cost': inf, 'pre': []},  # burdicks
            G: {'cost': inf, 'pre': []},  # speech
            H: {'cost': inf, 'pre': []},  # maintenance
            I: {'cost': inf, 'pre': []},  # old
            J: {'cost': inf, 'pre': []},  # fine art
            K: {'cost': inf, 'pre': []},  # police
            L: {'cost': inf, 'pre': []},  # mcalizertt
            M: {'cost': inf, 'pre': []},  # wingo
            N: {'cost': inf, 'pre': []},  # stud center
            O: {'cost': inf, 'pre': []},  # stud health
            P: {'cost': inf, 'pre': []},  # new busis
            Q: {'cost': inf, 'pre': []},  # oak
            R: {'cost': inf, 'pre': []},  # brew
            S: {'cost': inf, 'pre': []}  # bear

            }

    source = A
    destination = S

    print("Dijsktra Shortest Path Alg")
    dijsktra(graph, source, destination, info)
    print("\n")
    print("bellmanford Shortest Path Alg")
    bellmanford(graph, source, destination, info)
