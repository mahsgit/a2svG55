class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        out=[]
        out.append(celsius + 273.15)
        out.append(celsius * 1.80 + 32.00)
        return(out)