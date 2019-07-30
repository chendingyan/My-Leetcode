# 有n个打包机器从左到右一字排开，上方有一个自动装置会抓取一批放物品到每个打包机上，
# 放到每个机器上的这些物品数量有多有少，由于物品数量不相同，需要工人将每个机器上的物品进行移动从而到达物品数量相等才能打包。
# 每个物品重量太大, 每次只能搬一个物品进行移动，为了省力，只在相邻的机器上移动。
# 请计算在搬动最小轮数的前提下，使每个机器上的物品数量相等。如果不能使每个机器上的物品相同， 返回-1。
# 例如[1,0,5]表示有3个机器，每个机器上分别有1、0、5个物品，经过这些轮后: 第一轮:1 0<-5 => 1 1 4  第二轮:1<-1<-4 => 2 1 3  第三轮:
# 2 1 <- 3 => 2 2 2 移动了3轮，每个机器上的物品相等，所以返回3
# 例如[2,2,3]表示有3个机器，每个机器上分别有2、2、3个物品， 这些物品不管怎么移动，都不能使三个机器上物品数量相等，返回-1

# 思路 先用单点的想法考虑 将模型简化成三个变量  restLeft x restRight
# 分类讨论
# 每个位置的单点 都会有一个瓶颈 其中最痛的瓶颈 就是我们要的答案
def packingmachine(machines):
    sum = 0
    for i in range (0, len(machines)):
        sum+=machines[i]
    if sum%len(machines)!= 0:
        return -1
    else:
        avg = int (sum / len(machines))
    maxOps = 0
    leftSum = 0
    for i in range(0, len(machines)):
        rightSum = sum - leftSum - machines[i]
        leftRes = leftSum -i * avg # 正数代表 多余了 要给出去 负数代表不够 要被支援
        rightRes = rightSum - (len(machines) - i - 1) * avg
        print(leftRes, rightRes)
        if leftSum <= 0 and rightSum <= 0:
            maxOps = max(maxOps, leftRes+rightRes)
        else:
            maxOps = max(maxOps, max(abs(leftRes), abs(rightRes)))
        leftSum+=machines[i]

    return maxOps

if __name__ == '__main__':
    machines = [1,0,5]
    print(packingmachine(machines))

