# 基数，深圳成指*100 * 中小100*100 * 10000
A:int
# 报名次数
X:int
# 中签数量
C:int
# 抽签号
target:int


# 将基数A对应的数字倒序排列
B:int = int(str(A)[::-1])
# 起始中签号
Y:int = (B % X) + 1
# 阶数
Z:int = X // C
for i in range(C):
    if Y + i * Z == target:
        print("get it")
