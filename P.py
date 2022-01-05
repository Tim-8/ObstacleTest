#matplotlib nbagg #jupyter notebook上でアニメーション表示させるために必要
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
from matplotlib.animation import PillowWriter,FuncAnimation #動画作成用に追加

fig = plt.figure()
ax1 = fig.add_subplot(111)

A=np.array([-3,2])
B=np.array([-3,-2])
C=np.array([3,-2])
D=np.array([3,2])

scale=1.1
scaleP=1.2

p = pat.Polygon(xy = [A,B,C,D],
                edgecolor='black',
                facecolor='white',
                linewidth=1.6)

def initialize():
    ax1.set_xlim(-4,4)
    ax1.set_ylim(-3,3)
    ax1.add_patch(p)


    ax1.text(A[0]*scale,A[1]*scale,"A",fontsize=15,horizontalalignment='center',verticalalignment='center')
    ax1.text(B[0]*scale,B[1]*scale,"B",fontsize=15,horizontalalignment='center',verticalalignment='center')
    ax1.text(C[0]*scale,C[1]*scale,"C",fontsize=15,horizontalalignment='center',verticalalignment='center')
    ax1.text(D[0]*scale,D[1]*scale,"D",fontsize=15,horizontalalignment='center',verticalalignment='center')

    ax1.text(-3.5,0.0,"4cm",horizontalalignment='center',verticalalignment='center')
    ax1.text(0.0,-2.5,"6cm",horizontalalignment='center',verticalalignment='center')


def moveP(x):
    if 0<= x <4:
        return A+np.array([0,-1])*x*velocity
    elif 4<=x <10:
        return B+np.array([1,0])*(x-4)*velocity
    elif 10<= x <14:
        return C+np.array([0,1])*(x-10)*velocity
    else:
        return D

velocity=1.0
timestep=0.1

def animate(t):
    plt.cla()
    initialize()

    x=timestep*t
    P=moveP(x)

    ax1.plot(P[0],P[1],marker='o',color='black')
    ax1.text(P[0]*scaleP,P[1]*scaleP,"P",fontsize=15,horizontalalignment='center',verticalalignment='center')

    S = pat.Polygon(xy = [A,P,D],
                    edgecolor='black',
                    facecolor='lightgray',
                    linewidth=1.6)

    ax1.add_patch(S)

    plt.axis('off')
    plt.title('x=' + '{:.1f}'.format(x)+'sec')

anim = FuncAnimation(fig,animate,frames=140,repeat=True,interval=timestep*1000)
#anim.save("ugokutenP.gif", writer='pillow',fps=10)
plt.show()
