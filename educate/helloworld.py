# 실행방법 CTRL + SHIFT + B
print('hello world')

import simplejson as json
test_dict = {'1':95, '4':77, '3':12, '2':14}
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))