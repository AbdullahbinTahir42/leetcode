class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        while i < length:
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i] == 0:
                if i < (length - 1):
                    if flowerbed[i + 1] == 0:
                        n -= 1
                        i += 2
                    else:
                        i += 1
                else:
                    n -= 1
                    break
            else:
                return  
        return True if n <= 0 else False
        

            
            



        
