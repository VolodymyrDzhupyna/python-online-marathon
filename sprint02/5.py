import re


def max_population(data): 
    new_result = []
    
    for item in range(1, len(data)):
        new_result.append((re.findall(r"((?<=\,)\w+(?<!\,)\w+)", data[item])))
    
    max_num = new_result[0][int(1)]
    
    for item in range(len(new_result)):
        if new_result[item][int(1)] > max_num:
            max_num = new_result[item][int(1)]

    for item in new_result:
        if str(max_num) in item:
            item[1] = int(max_num)
            return tuple(item)


data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]
print(max_population(data))
