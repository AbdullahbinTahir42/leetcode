class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [" "] * n
        m = 0
        for i in range(0,n):
            m += 1
            if m % 3 == 0 and m % 5 == 0:
                answer[i] = "FizzBuzz"
            elif m % 3 == 0:
                 answer[i] = "Fizz"
            elif m % 5 == 0:
                 answer[i] = "Buzz"
            else:
                    answer[i] = f"{m}"

        return answer    

        
