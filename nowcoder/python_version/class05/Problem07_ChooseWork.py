# 为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。
# class Job {
# public int money;// 该工作的报酬 public int hard; // 该工作的难度
#     public Job(int money, int hard) {
#         this.money = money;
#         this.hard = hard;
# } }
# 给定一个Job类型的数组jobarr，表示所有的工作。给定一个int类型的数组arr，表示所有小伙伴的能力。 返回int类型的数组，表示每一个小伙伴按照牛牛的标准选工作后所能获得的报酬。

# 先将工作按难度排序 去掉 工作难度相同 薪水不是最高的工作 然后 去掉工作难度更大 但薪水还没前一个难度高的工作 最后按这个有序表 排序 查找
import random
class Job:
    def __init__(self, money, hard):
        self.money = money
        self.hard = hard

    def __str__(self):
        return 'hard: ' + str(self.hard)+ ' money: ' + str(self.money)

    def __lt__(self, other):
        return self.hard < other.hard

def getJobs(arr, ability):
    jobs = dict()
    for job in arr:
        if job.hard not in jobs.keys():
            jobs[job.hard] = job.money
        else:
            if jobs[job.hard] < job.money:
                jobs[job.hard] = job.money
    jobs = sorted(jobs.items())
    final = []
    final.append(jobs[0])
    for i in range(1, len(jobs)):
        if jobs[i][1] > final[-1][1]:
            final.append(jobs[i])
    print(final)
    jobs = []
    moneys = []
    for i in final:
        jobs.append(i[0])
        moneys.append(i[1])
    print(jobs, moneys)



if __name__ == '__main__':
    arr = []
    for i in range(10):
        job = Job(random.randrange(1,100), random.randrange(1,5))
        print(job)
        arr.append(job)

    ability = []
    for i in range(20):
        ability.append(random.randrange(1, 5))
    print(ability)
    getJobs(arr, ability)

