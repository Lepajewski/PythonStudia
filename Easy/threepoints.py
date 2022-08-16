Ax, Ay = input().split()
Bx, By = input().split()
Cx, Cy = input().split()
Ax = int(Ax)
Bx = int(Bx)
Cx = int(Cx)
Ay = int(Ay)
By = int(By)
Cy = int(Cy)
if (Bx - Ax) * (Cy - Ay) == (By - Ay) * (Cx - Ax):
    print('True')
else:
    print('False')
