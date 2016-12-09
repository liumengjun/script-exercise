# Demo for sys.settrace
# and unittest method
# 探索coverage.py原理
# 执行python $THE_DEMO.py
#  or python -m unittest $THE_DEMO.py

import unittest
import re
import sys


# 获取当前执行的文件名
# print(sys.argv)
# exit()
main_filename = sys.argv[0]
if not main_filename.endswith('.py') and len(sys.argv) >=2 :
    main_filename = sys.argv[1]


# 设定trace方法
def trace_func(frame, event, arg):
    if frame.f_code.co_filename.endswith(main_filename):
        print('Trace: %s, %s, %s' % (frame, event, arg))
        print('code: L%s, @%s' % (frame.f_lineno, frame.f_code.co_filename))
    return trace_func
sys.settrace(trace_func)


class SyntaxTest(unittest.TestCase):

    def test_override_operator(self):
        self.assertTrue(True)
        class Person(object):
            '''
            class of representing person
            '''
            # self.name = ''
            # self.age = 0
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def __eq__(self, other):
                if self is other:
                    return True
                # print("future check")
                if isinstance(other, Person):
                    return self.name == other.name and self.age == other.age
                return False
            def __hash__(self):
                return self.name.__hash__() << 1 | self.age.__hash__()

        a = Person('scott', int(23))
        b = Person('scott', 23)
        print('---')
        print(hash(a))
        print('---')
        print(a.__hash__)
        print('---')
        print(a.__hash__.__self__)
        print('---')
        # print(hash(a))
        print(a.__str__)
        print(a.__repr__)
        print(a.__weakref__)
        print(a.__subclasshook__)
        print(a.__dict__)
        print(a.__doc__)
        self.assertEqual(a, a)
        self.assertEqual(a, b)
        print(dir(a))
        print(vars(a))
        pass

