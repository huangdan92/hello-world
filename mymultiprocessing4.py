# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import multiprocessing as mp
import time

def job(x):
    time.sleep(1)
    return x*x

def multicore():
    pool = mp.Pool(processes=2)
    # res = pool.map(job, range(1000000000))
    # print(res)
    # res = pool.apply_async(job, (1,2,3))
    # print(res.get())
    multi_res =[pool.apply_async(job, (i,)) for i in range(1000000000)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()

