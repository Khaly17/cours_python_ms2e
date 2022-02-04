import numpy as np

fff = open("input_file_03.dat", mode='w')

Nrow, Ncol = (5,2)

idx = 10.5
for i in range(Nrow):
    for j in range(Ncol):
        fff.write("{:8.1f}".format(idx))
        idx+= 1.0
    if i<Nrow-1:
        fff.write("\n")

fff.close()
