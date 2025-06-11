def solution(numer1, denom1, numer2, denom2):
    
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    # 통분
    tmp_denom = denom1  * denom2
    tmp_numer = numer1  * denom2 + numer2 * denom1
    
    #gcd
    gcd_result = gcd(tmp_numer,tmp_denom)
    
    answer = [tmp_numer//gcd_result,tmp_denom//gcd_result]
    return answer