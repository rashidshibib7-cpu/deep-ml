import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	n_m = np.array(matrix)
	return (n_m * scalar ).tolist()
	return [[element * scalar for element in row] for row in matrix]
