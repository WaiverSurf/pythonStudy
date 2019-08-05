
str1 = "I am linam"
str2 = 'fileman'

#길이 
print(len(str1), len(str2))

escape_str1 = "do you have a \"big mom\" "
print(escape_str1)

escape_str2 = "haha\thoho\thehe"
print(escape_str2)

#RawString옵션 있는그대로 출력
raw_str = r'c:\hahah\men\"king"'
print(raw_str)

#멀티라인 이어버리기
multi_line = \
    "haha"\
        "hehe"
print(multi_line)

# 곱하기도 지원
print(escape_str1 * 10)

# 포함했느냐 안했느냐
print('hah' in raw_str)
print('albert' not in raw_str)

#문자열 함수
print(str1.split(' '), type(str1.split(' ')))

# 분할해서 루프
for str in str1.split(' '):
    print(str)

# 첫글자 대문자
print(str1.capitalize())

# 인덱스 슬라이스
print(str1[0:3], str1[3:6], str1[3:len(str1)])
print(str1[:3])
print(str1[::-1])
