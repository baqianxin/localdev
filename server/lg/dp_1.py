
def getMinCoup(n):
    f = {1: 1}
    i = 1
    while i <= n:
        mCoup = 0
        if i == 1:
            mCoup = 0
        elif i > 11:
            mCoup = min([f[i-1], f[i-5], f[i-11]])
        elif i < 11 and i > 5:
            mCoup = min([f[i-1], f[i-5]])
        else:
            mCoup = f[i-1]
        f[i] = mCoup+1
        print(i, mCoup+1)
        i += 1

    return f[n]


#  使用 1,5,11 最少组合数 到达目标值n
getMinCoup(105)
