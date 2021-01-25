import pycosat
import sys

def read_CNF(filename):
    with open(filename) as f:
        cnf = []
        for line in f.readlines():
            if line.startswith('p cnf'):
                continue
            else:
                cnf.append([int(x) for x in line.split(' ')[:-1]])
                #print(line)
    return cnf

#for manual use within e.g. IDLE
#print(bool(pycosat.solve(read_CNF("1.graph.cnf"))))

if __name__ == '__main__':
    result = pycosat.solve(read_CNF(sys.argv[1]))
    if result == ("UNSAT" or "UNKNOWN"):
        print(result)
    else:
        print("SAT")
