"""
Body of application. Parallel calculation in several threads.
"""

import calc
from threading import Thread

K1 = 0.0000000000001
K2 = 0.00001

n = int(input("A dimension of square matrix = "))

# first stage (initialization)
A = calc.Matrix()
A_init = Thread(target=A.set_matrix, args=(n,))
A_init.start()

A1 = calc.Matrix()
A1_init = Thread(target=A1.set_matrix, args=(n,))
A1_init.start()

A2 = calc.Matrix()
A2_init = Thread(target=A2.set_matrix, args=(n,))
A2_init.start()

b = calc.Vector()
b_init = Thread(target=b.b_calculation, args=(n,))
b_init.start()

b1 = calc.Vector()
b1_init = Thread(target=b1.set_vector, args=(n,))
b1_init.start()

B2 = calc.Matrix()
B2_init = Thread(target=B2.set_matrix, args=(n,))
B2_init.start()
B2_init.join()

c1 = calc.Vector()
c1_init = Thread(target=c1.set_vector, args=(n,))
c1_init.start()

C2 = calc.Matrix()
C2_init = Thread(target=C2.C2_calculation, args=(n,))
C2_init.start()

A1_init.join()
A2_init.join()
b_init.join()
b1_init.join()
B2_init.join()
c1_init.join()
C2_init.join()

# second stage (yi calculation)
y1 = calc.YCalculation()  # y1 = A * B
y1_calc = Thread(target=y1.y1_calculation, args=(A.matrix, b.matrix, n))
y1_calc.start()

y2 = calc.YCalculation()  # y2 = A1 * (b1 + c1)
y2_calc = Thread(target=y2.y2_calculation, args=(A1.matrix, b1.matrix, c1.matrix))
y2_calc.start()

y3 = calc.YCalculation()  # y3 = A2 * (C2 + 2B2)
y3_calc = Thread(target=y3.y3_calculation, args=(A2.matrix, C2.matrix, B2.matrix))
y3_calc.start()

y1_calc.join()
y2_calc.join()
y3_calc.join()

# third stage (yi transpose)
tran_y1 = calc.YCalculation()
tran_y1_calc = Thread(target=tran_y1.yi_trasonse, args=(y1.matrix,))
tran_y1_calc.start()

tran_y2 = calc.YCalculation()
tran_y2_calc = Thread(target=tran_y2.yi_trasonse, args=(y2.matrix,))
tran_y2_calc.start()

tran_y1_calc.join()
tran_y2_calc.join()

# fourth stage (zi calculation)
z1 = calc.ZCalculation()  # z1 = y2' * (y1' * y1 * y3)
z1_calc = Thread(target=z1.z1_calculation, args=(tran_y2.matrix, tran_y1.matrix, y1.matrix, y3.matrix))
z1_calc.start()

z2 = calc.ZCalculation()  # z2 = y1' * y3^3)
z2_calc = Thread(target=z2.z2_calculation, args=(tran_y1.matrix, y3.matrix))
z2_calc.start()

z3 = calc.ZCalculation()  # z3 = y2' * y3)
z3_calc = Thread(target=z3.z3_calculation, args=(tran_y2.matrix, y3.matrix))
z3_calc.start()

z4 = calc.ZCalculation()  # z4 = y3 * y1
z4_calc = Thread(target=z4.z4_calculation, args=(y3.matrix, y1.matrix))
z4_calc.start()

z5 = calc.ZCalculation()  # z5 = y2' * y2 * y1
z5_calc = Thread(target=z5.z5_calculation, args=(tran_y1.matrix, y2.matrix, y1.matrix))
z5_calc.start()

z1_calc.join()
z2_calc.join()
z3_calc.join()
z4_calc.join()
z5_calc.join()

# fifth stage (gi calculation)
g1 = calc.GCalculation()  # g1 = z1 + z2 + z3
g1_calc = Thread(target=g1.g1_calculation, args=(z1.matrix, z2.matrix, z3.matrix))
g1_calc.start()

g2 = calc.GCalculation()  # g2 = z4 + z5
g2_calc = Thread(target=g2.g2_calculation, args=(z4.matrix, z5.matrix))
g2_calc.start()

g1_calc.join()
g2_calc.join()

# sixth stage (last calculation)
l = calc.LCalculation()  # last calc (L = K1*g1+K2*g2)
l_calc = Thread(target=l.last_calculation, args=(g1.matrix, g2.matrix, K1, K2))
l_calc.start()

l_calc.join()
