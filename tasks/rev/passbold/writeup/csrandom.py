# Partial C# PRNG generator implementation in Python
# Found on https://gist.github.com/badstreff/541cf2e6953b3c666f83127a1d4f6a47

from ctypes import *

class Random:
    def __init__(self, seed):
        self.seed = c_int(seed).value
        self.MBIG = 2147483647
        self.MMIN = -2147483648
        self.MZ = 0
        self.MSEED = 161803398
        self.SeedArray = [0] * 56

        if seed == self.MMIN:
            subtraction = self.MBIG
        else:
            subtraction = abs(seed)

        mj = c_int(self.MSEED - subtraction).value
        self.SeedArray[55] = mj
        mk = 1
        for i in range(1, 55):
            ii = (21 * i) % 55
            self.SeedArray[ii] = mk
            mk = mj - mk
            if mk < 0:
                mk += self.MBIG
            mj = self.SeedArray[ii]
        for k in range(1, 5):
            for i in range(1, 56):
                self.SeedArray[i] -= self.SeedArray[1 + (i + 30) % 55]
                if self.SeedArray[i] < 0:
                    self.SeedArray[i] = c_int(self.SeedArray[i] + self.MBIG).value
        self.inext = 0
        self.inextp = 21
        self.seed = 1

    def InternalSample(self):
        locINext = self.inext + 1
        locINextp = self.inextp + 1

        if locINext >= 56:
            locINext = 1
        if locINextp >= 56:
            locINextp = 1

        retVal = c_int(self.SeedArray[locINext] - self.SeedArray[locINextp]).value
        if retVal == self.MBIG:
            retVal -= 1
        if retVal < 0:
            retVal = c_int(retVal + self.MBIG).value
        self.SeedArray[locINext] = retVal
        self.inext = locINext
        self.inextp = locINextp
        return retVal

    def Next(self, maxValue=None):
        if maxValue == None:
            return self.InternalSample()
        return int(c_float(self.Sample() * maxValue).value)

    def Sample(self):
        s = self.InternalSample()
        ret = c_double(s * c_double(1.0/self.MBIG).value).value
        return ret