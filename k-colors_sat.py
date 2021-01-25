import sys
import itertools

vertices = []
edges = []
k = 1

def read_graph(filename):
	with open(filename) as f:
		vert_num = -1
		edg_num = -1
		for line in f.readlines():
			if line.startswith('c '): # ignore comments
				continue
			if line.startswith('e '): # add an edge, check vertex number are consistent
				parts = line.split(' ')
				u, v = int(parts[1]), int(parts[2])
				if u > vert_num or v > vert_num:
					print('Warning: invalid vertex number found in edge:', line)
				edges.append((u, v))
			
			if line.startswith('p edge'): # parse problem specification
				parts = line.split(' ')
				vert_num = int(parts[2])
				edg_num = int(parts[3])
				vertices = list(range(1, vert_num + 1))

	if edg_num != len(edges):
		print('Warning: number of edges does not match file header: %d != %d' % (len(edges), edg_num))

	return vertices, edges

def write_cnf(cnf, filename):

	variables =  max(map(abs, itertools.chain(*cnf))) # find the maximum number of a variable used
	cnf_str = '\n'.join(map(lambda c: ' '.join(map(str, c)) + ' 0', cnf)) # concatenate clauses into a string

	print('CNF created, it has %d variables and %d clauses' % (variables, len(cnf)))

	with open(filename, 'w') as f:
		f.write('p cnf %d %d\n' % (variables, len(cnf))) # write basic CNF information
		f.write(cnf_str)

def generate_cnf(vertices, edges, k):
	clauses = []
	X = [[0]*(k+1) for _ in range(len(vertices)+1)]
	counter = 1
	i = 1
	while(i < len(vertices) + 1):
		j = 1
		while(j < k + 1):
			X[i][j] = counter
			counter += 1
			j += 1
		i += 1

	i = 1
	while(i <= len(vertices)):
		c = 1
		temp_clause = []
		while(c <= k):
			temp_clause.append(X[i][c])
			c += 1
		i += 1
		clauses.append(temp_clause)


	i = 1
	while(i <= len(vertices)):
		c = 1
		while(c <= k-1):
			d = c + 1
			while(d <= k):
				clauses.append([-X[i][c],-X[i][d]])
				d += 1
			c += 1
		i += 1

	for i, j in edges:
	    c = 1
	    while(c <= k):
		    clauses.append([-X[i][c],-X[j][c]])
		    c += 1
	print() #new line for better visualisation
	
	return clauses

if __name__ == '__main__':
    vertices, edges = read_graph(sys.argv[1])
    k = int(sys.argv[2])

    print('Number of vertices:', len(vertices))
    print('Number of edges:', len(edges))
    print('Number k is:', str(k))

    cnf = generate_cnf(vertices, edges, k)

    write_cnf(cnf, sys.argv[1] + '.cnf')
