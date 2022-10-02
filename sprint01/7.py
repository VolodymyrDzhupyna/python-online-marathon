def Cipher_Zeroes(N):

    score_count = 0

    for item in N:
        if item == "0" or item == "6" or item == "9":
            score_count += 1
        if item == "8":
            score_count += 2

    if score_count % 2 == 1:
        score_count += 1
    elif score_count % 2 == 0 and score_count > 0:
        score_count -= 1
         
    if not score_count:
        return 0
    return bin(score_count)[2:]
    

print(Cipher_Zeroes("565"))
