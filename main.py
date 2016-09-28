"""
Main module of application. Provide users' interface.qq
"""

import app

print("Result:\n", app.l.matrix)

values = {'A': app.A.matrix,
          'A1': app.A1.matrix,
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

keys = 'List of available values: '
for key in values:
    keys += key + ' '

while True:
    key = input("Enter the variable: ")
    if key == 'help':
        print(keys)
    else:
        print(values.get(key, "There is no such key, try again or print 'help' for calling list of values"), "\n")
