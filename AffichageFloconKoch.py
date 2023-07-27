import turtle as tu

def segment_koch(l,n):
    flocon(l/3,n-1)
    tu.lt(60)
    flocon(l/3,n-1)
    tu.right(120)
    flocon(l/3,n-1)
    tu.lt(60)
    flocon(l/3,n-1)

def flocon(l,n) :
    if n==0 : tu.fd(l)
    else :
        segment_koch(l,n)


def flocon_partie (l,n):
    flocon(l,n)
    tu.lt(240)
    flocon(l,n)
    tu.lt(240)
    flocon(l,n)



if __name__ == '__main__' :
    tu.color('green')
    tu.hideturtle()
    tu.tracer(5,0)
    flocon_partie (300,5)
    tu.exitonclick()


