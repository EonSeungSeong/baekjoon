h= [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
s = ["A+","A0","B+",'B0',"C+",'C0',"D+",'D0',"F"]

hour_total = 0
score_total = 0

for i in range(20):
    major, hour, score = input().split()
    hour = float(hour)
    if score != "P":
        hour_total +=hour
        score_total += hour* h[s.index(score)]

print("%.6f" % (score_total/ hour_total))       