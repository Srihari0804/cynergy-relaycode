#SRIHARI

roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
user_input=input("Enter two Roman numbers(with space): ").split()
num=0;x=0;li=[]
for i in user_input:
    if i not in roman_dict:
        for n in i:
            li.append(roman_dict.get(n))
        if li!=sorted(li):
            for n in i:
                x += roman_dict.get(n)
                num += x
        else:
            largest=li[-1];remaining=sum(li[0:-1])
            num+=largest-remaining
    else:
        num+=roman_dict.get(i)

print("sum is",num)
