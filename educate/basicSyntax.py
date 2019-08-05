#section 2-2

# import this
import sys

#  encoding
print('charset stdin : ' + sys.stdin.encoding)
print('charset stdout : ' + sys.stdout.encoding)

myName = 'GoodBoy'

#조건
if myName == 'GoodBoy': 
    print("OK")

#루프 (파라미터는 괄호안에)
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = %d' % (i,j,i*j))

#함수
def test():
    print("하이")
test()

#클래스
class Cookie:
    pass

#객체선언
cookie = Cookie()

print(id(cookie))
print(dir(cookie))

