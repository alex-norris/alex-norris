import random

committeeMenCounts = []
committeeSize = 4

for j in range(10000):  # how many iterations?
    profs = [0,0,0,0,1,1,1,1,1,1]  # 4 women + 6 men, reset after each run
    menCount = 0  # reset after each committee
    for i in range(committeeSize):
        # remove random prof and add to running total if man:
        menCount += profs.pop(random.randint(0,len(profs)-1))
    # add the number of men in this committee to running tally:
    committeeMenCounts.append(menCount)

# average number of men per committee, as a ratio
print(sum(committeeMenCounts)/len(committeeMenCounts)/float(committeeSize))
