import numpy as np


class Vector:
    def set_vector(self, n):  # sets random values of vector
        self.matrix = np.c_[np.random.randint(0, 100, (n, 1)), np.zeros((n, n - 1))]

    def b_calculation(self, n):  # b = 10/(i^2 + 1)
        b = []
        for i in range(n):
            bi = [10 / ((i + 1) ** 2 + 1)]
            b.append(bi)
        self.matrix = np.array(b)


class Matrix:
    def set_matrix(self, n):  # sets random values of matrix
        self.matrix = np.random.randint(0, 100, (n, n))

    def C2_calculation(self, n):  # Cij = 1/(i + 2j)
        C2 = []
        for i in range(n):
            Cij = []
            for j in range(n):
                Cij_element = 1 / ((i + 1) + 2 * (j + 1))
                Cij.append(Cij_element)
            C2.append(Cij)
        self.matrix = np.array(C2)


class YCalculation:
    def y1_calculation(self, A, b, n):
        self.matrix = np.c_[np.dot(A, b), np.zeros((n, n - 1))]

    def y2_calculation(self, A1, b1, c1):
        self.matrix = np.dot(A1, np.add(b1, c1))

    def y3_calculation(self, A2, C2, B2):
        self.matrix = np.dot(A2, np.add(C2, 2 * B2))

    def yi_trasonse(self, yi):
        self.matrix = np.transpose(yi)


class ZCalculation:
    def z1_calculation(self, trun_y2, trun_y1, y1, y3):  # z1 = y2' * (y1' * y1 * y3)
        self.matrix = np.dot(trun_y2, (np.dot(np.dot(trun_y1, y1), y3)))

    def z2_calculation(self, trun_y1, y3):  # z2 = y1' * y3^3)
        self.matrix = np.dot(trun_y1, y3 ** 3)

    def z3_calculation(self, trun_y2, y3):  # z3 = y2' * y3)
        self.matrix = np.dot(trun_y2, y3)

    def z4_calculation(self, y3, y1):  # z4 = y3 * y1
        self.matrix = np.dot(y3, y1)

    def z5_calculation(self, trun_y2, y2, y1):  # z5 = y2' * y2 * y1
        self.matrix = np.dot(np.dot(trun_y2, y2), y1)


class GCalculation:
    def g1_calculation(self, a, b, c):  # g1 = z1+z2+z3
        self.matrix = a + b + c

    def g2_calculation(self, a, b):  # g2 = z4 + z5
        self.matrix = a + b


class LCalculation:
    def last_calculation(self, a, b, k1, k2):
        self.matrix = k1 * a + k2 * b
