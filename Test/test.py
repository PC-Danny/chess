testvariable = 'white'
print(testvariable)
class TestClass:
    def methodTest():
        global testvariable
        print(testvariable)
        testvariable = 'white' if testvariable == 'black' else 'black'

testObject = TestClass

testObject.methodTest()

print(testvariable)

print(type(range(5)))

test = (1,1)

print(type(test))

print(test)