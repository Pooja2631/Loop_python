import random 
names=['neha','anshika','preeti','deepti','rani','amrita','moni','dugra','savita','chandni']
room_bed=['room no:- 301 bed_1','room no:-102 bed_3','room no:-304 bed_5','room no:-402 bed_3',' room no:-404 bed_8','room no:-403 bed_6','room no:-303 bed_9','room no:-302 bed_1','room no:-103 bed_4','room no:-203 bed_2','room no:-401 bed_9'] 
random.shuffle(names)
random.shuffle(room_bed)
i=0
while i<len(names):
    a=(names[i],room_bed[i])
    i=i+1
    print()

