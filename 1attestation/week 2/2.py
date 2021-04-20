class Solution(object):
    def interpret(self, command):
        res = ''
        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                i += 1
                if command[i] == ')':
                    res += 'o'
                else:
                    i += 2
                    res += 'al'
        return res