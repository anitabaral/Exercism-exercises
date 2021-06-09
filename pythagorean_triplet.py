def triplets_with_sum(number):
    list_here = []
    for i in range(number):
        for j in range(number):
            for k in range(number):
                if ((i + j + k + 3) == number):
                    if ( ((i+1)**2 + (j+1)**2 == (k+1)**2)):
                            list_here.append([(i+1), (j+1), (k+1)])
    return list(map(lambda x: list(x), list(set(tuple(sorted(sub)) for sub in list_here))))

# print(triplets_with_sum(1001))

'''Kankua's solution: Math way to solve the problem, the above way uses brute force method which consumes a lot of time'''
# a**2 + b**2 = c**2
# a + b + c = N <->
# a**2 + b**2 = c**2
# a + b = N - c
# Solving system of equations for a and b
# D = sqrt(c**2 - N**2 + 2*N*c)
# a = (N - c - D)/2
# b = (N - c + D)/2
# D is real for c > N * (sqrt(2) - 1)
# And c < N/2 from the problem statement

# import math
# def triplets_with_sum(number):
# 	N=float(number)
# 	triplets = []
# 	for c in range(int(N/2)-1,int((math.sqrt(2)-1)*N),-1):
# 		D = math.sqrt(c**2 - N**2 + 2*N*c)
# 		if D==int(D):
# 			triplets.append([int((N-c-D)/2),int((N-c+D)/2),c])
# 	return triplets
