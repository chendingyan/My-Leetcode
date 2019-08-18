# 派对的最大快乐值
# 员工信息的定义如下:
# class Employee {
# public int happy; // 这名员工可以带来的快乐值
# List<Employee> subordinates; // 这名员工有哪些直接下级 }
# 公司的每个员工都符合 Employee 类的描述。整个公司的人员结构可以看作是一棵标准的、 没有环的 多叉树。树的头节点是公司唯一的老板。除老板之外的每个员工都有唯一的直接上级。 叶节点是没有 任何下属的基层员工(subordinates列表为空)，除基层员工外，每个员工都有一个或多个直接下级。
# 这个公司现在要办party，你可以决定哪些员工来，哪些员工不来。但是要遵循如下规则。 1.如果某个员工来了，那么这个员工的所有直接下级都不能来 2.派对的整体快乐值是所有到场员工快乐值的累加 3.你的目标是让派对的整体快乐值尽量大
# 给定一棵多叉树的头节点boss，请返回派对的最大快乐值。
# x来 x不来
# x来 x的happy加 下属的不来 x不来 下属的来或者不来都可以

class Employee:
    def __init__(self, happy, nexts = None):
        self.happy = happy
        self.nexts = nexts

class Info:
    def __init__(self, come, nocome):
        self.come = come
        self.nocome = nocome

def process(x):
    if x.nexts is None:
        return Info(x.happy, 0)
    come = x.happy
    nocome = 0
    for sub in x.nexts:
        come += process(sub).nocome
        nocome += max(process(sub).come , process(sub).nocome)
    return Info(come, nocome)

if __name__ == '__main__':
    boss = Employee(12)
    e1 = Employee(100)
    e2 = Employee(12)
    e3 = Employee(5)
    e4 = Employee(22)
    e5 = Employee(188)
    boss.nexts = [e1,e2]
    e1.nexts = [e3,e4]
    e4.nexts = [e5]
    info = process(boss)
    print(info.come, info.nocome)