"""
Given a row total R, column total C, and grid layout G - compute the probability of striking a target 1.

Example:
R = 2, C = 3, G = [0,1,0,1,1,0]
result:
probability = 50%  *classical probability
"""

"""Based on these details, it may not be necessary to deal with breaking the rows/columns out, unless specified."""


def prob(R,C,G):
	denom = R*C  
	count = sum(G)
	probval = round(count/denom * 100, 2)
	print(str(probval)+' %')
	return probval