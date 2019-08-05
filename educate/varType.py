#자료형 종류를 나열하고 타입을 확인한다.
v_str1 = "fireMan"
print(type(v_str1))

v_bool = False
print(type(v_bool))

v_str2 = "junlina"
print(type(v_str2))

v_float = 10.3
print(type(v_float))

v_int = 7
print(type(v_int))

v_dic = {
    "name" : "youngeun",
    "age" : 29
}
print(type(v_dic))

v_tuple = 3,5,7
print(type(v_tuple))

v_set = {1,2,3}
print(type(v_set))

v_list = [3,56,67]
print(type(v_list))

# 빅사이즈
big_int1 = 99999999999999999999999999999999999999999999999999999999
big_int2 = 34985289572348912734089175098327562093572390392450782309

print(big_int1, type(big_int1))
print(big_int2, type(big_int2))
print(big_int1 + big_int2)
print(big_int1 - big_int2)
print(big_int1 * big_int2)

# /나누기, //몫, %나머지, **제곱
print(4**4)

#형변환
print(float(big_int1))
print(int(True))
print(int('3'))
print(str(18), type(str(18)))

# 수치연산
print(abs(-1818))
n,m = divmod(100, 8) #나눔과 나머지
print(n, m) 

import math
print(math.ceil(5.1))


