def fibonacciseries(n): 
    if n <= 1:
        return n
    else:
        return(fibonacciseries(n-1) + fibonacciseries(n-2))
    
def fibo2(nterms):
    if (nterms <= 17 and nterms >0):
        for term in range(nterms):
            print(fibonacciseries(term))
    else:
        print("Please enter a number between 1 and 17.")