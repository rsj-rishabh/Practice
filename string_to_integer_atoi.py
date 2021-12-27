class Solution:
    def myAtoi(self, s: str) -> int:
        # states = 0 - any, 1 - sign, 2 - number, 3 - end
        state = 0
        result = 0
        sign = 0
        MAX = (2**31) - 1
        MIN = 2**31
        for i in s:
            
            if state == 0:
                if i.isdigit():
                    state = 2
                    result += int(i)
                elif i in ['+', '-']:
                    state = 1
                    if i == '-':
                        sign = 1
                elif i == ' ':
                    pass
                else:
                    state = 3
                    break
            
            elif state == 1:
                if i.isdigit():
                    state = 2
                    result += int(i)
                else:
                    state = 3
                    break
            
            elif state == 2:
                if i.isdigit():
                    temp = result * 10
                    i = int(i)
                    if (temp<MAX and sign==0):
                        if i>(MAX-temp):
                            result = MAX
                            state = 4
                            break
                        else:
                            result = temp + int(i)
                    elif(temp<MIN and sign==1):
                        if i>(MIN-temp):
                            result = MIN
                            state = 4
                            break
                        else:
                            result = temp + int(i)
                    else:
                        if sign==0:
                            result = MAX
                        else:
                            result = MIN
                        state = 4
                        break
                else:
                    state = 4
                    break
                    
        if state in [2, 4]:
            if sign == 0:
                return result
            else:
                return (-1 * result)
        else:
            return 0
