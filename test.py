import random
import time
random.seed( time.time() )

num_map = [ 0 for i in range(10)]
for i in range(1000000):
    rand_int = random.choice( num_map )
    num_map[rand_int]+=1


count = 0
all_count = 0
for num in num_map:
    all_count+=num
for idx,num in enumerate(num_map):
    print("%d: %d(%d%%)" % (idx+1,num,(num+count)/all_count*100))
    count+=num


