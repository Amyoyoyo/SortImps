class Solution(object):
    def sortArrayByParityII(self, A):
        oddPointer=1
        for i in range(0,len(A),2):
            if A[i]%2:
                while A[oddPointer]%2:
                    oddPointer+=2
                A[i],A[oddPointer]=A[oddPointer],A[i]
        return A

    def sortArrayByParityII2(self, A):
        evenPointer=0
        oddPointer=1
        result=[None]*len(A)
        for a in A:
            if a%2==0:
                result[evenPointer]=a
                evenPointer+=2
            else:
                result[oddPointer]=a
                oddPointer+=2
        return result

if __name__ == '__main__':
    sol=Solution()

    A=[4,2,5,7]
    print(sol.sortArrayByParityII2(A))