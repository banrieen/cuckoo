import os
import random
import numpy as np
import sqlite3
import datetime

class guess():

    LotteryNum = {"body":(), "foot":()}
    def __init__(self):
        pass

    def random_lottery(self):
        body = None
        foot = None
        body = set(sorted(random.sample(range(1,36),5)))
        foot = set(sorted(random.sample(range(1,13),2)))
        self.LotteryNum = {"body":body, "foot":foot}
        return self.LotteryNum

    def check(src, dst):
        """ Assert the guess num would not be same to history lottery 
        # Be care, the dst num set must be sorted.
        """
        if src and dst:
            if src[body] == dst[body] and src[foot] == dst[foot]:
                return False
            elif src[body] == dst[body] and src[foot] != dst[foot]:
                return False
            else:
                return Ture

    def guess_many(self, count):
        """ Creat count random lottery numbers """
        CountRL = []
        while count:
            CountRL.append(self.random_lottery())
        return CountRL
      


        
if __name__ == "__main__":
    gs = guess()
    print(gs.random_lottery())