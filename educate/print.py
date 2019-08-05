print('haha')
print()
print(':)')

#Separator 
print('T', 'E', 'S', 'T')
print('2019', '04', '03', sep='-')
print('albertman', 'google.com', sep='@')

#End : 끝에 개행대신 다른기능 부여
print('Welcome To', end='')
print('Albert', end='') # 그냥 이어가기 줄바꿈없음
print('House') # 디폴트 \n

#format : [], {}, ()
print('{} and {}'.format('cel', 'ina')) #일반적인사용
print('{0} and {1} and {0}'.format('cel', 'ina')) #인덱스 번호 사용 
print("{a} are {b}".format(a='albert', b='kim')) # 어트리뷰트로 매핑

#파라미터 매칭은 포멧%S같은거로 해놓고 뒤에 % 붙이고 한다.
print("%s is happy money size -> %d" % ('albert', 18000)) #표현식 매핑

print("Test1: %05d, Price: %4.2f" % (100, 6534.1234)) #  매핑
print("Test1: {0:5d}, Price:{1: 4.2f}".format(612, 1234.1234)) #인덱스로 매핑
print("Test1: {a:5d}, Price:{b: 4.2f}".format(a=432, b=4321.4321)) #속성으로 매핑

#따옴표로 감싸서 표현하기 이스케이프
print("'you'") 
print('"you"') 

