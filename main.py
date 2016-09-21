#
# n = int(input("A dimension of square matrix = "))  # додати конфігпарсер і аргпарсер!!!
print("""
1. Set a dimension (by default it is {n}
2. Calculate with random values
    """.format(n=4))
input()
import app

print("Result:", app.l.matrix)
# print("""
#     1.""")

values = {'A': app.A.matrix,
          'A2': app.A2.matrix,
          'b': app.b.matrix,
          'b1': app.b1.matrix,
          'B2': app.B2.matrix,
          'c1': app.c1.matrix,
          'C2': app.C2.matrix,
          'y1': app.y1.matrix,
          'y2': app.y2.matrix,
          'y3': app.y3.matrix,
          'y1\'': app.tran_y1.matrix,
          'y2\'': app.tran_y2.matrix,
          'z1': app.z1.matrix,
          'z2': app.z2.matrix,
          'z3': app.z3.matrix,
          'z4': app.z4.matrix,
          'z5': app.z5.matrix,
          'g1': app.g1.matrix,
          'g2': app.g2.matrix,
          'l': app.l.matrix
          }
while True:
    key = input("Enter the variable: ")
    print(values.get(key, "There is no such key, try again"), "\n")

#
# print("A:\n", A.matrix)
# print("\nA1:\n", A1.matrix)
# print("\nA2:\n", A2.matrix)
# print("\nb:\n", b.matrix)
# print("\nb1:\n", b1.matrix)
# print("\nB2:\n", B2.matrix)
# print("\nc1:\n", c1.matrix)
# print("\nC2:\n", C2.matrix)
# print("\ny1:\n", y1.matrix)
# print("\ny2:\n", y2.matrix)
# print("\ny3:\n", y3.matrix)
# print("\ny1':\n", tran_y1.matrix)
# print("\ny2':\n", tran_y2.matrix)
# print("\nz1:\n", z1.matrix)
# print("\nz2:\n", z2.matrix)
# print("\nz3:\n", z3.matrix)
# print("\nz4:\n", z4.matrix)
# print("\nz5:\n", z5.matrix)
# print("\ng1:\n", g1.matrix)
# print("\ng2:\n", g2.matrix)
# print("\nlast_part:\n", l.matrix)
