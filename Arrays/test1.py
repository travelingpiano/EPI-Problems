def func1(input1):
    func2(input1)
    def func2(block):
        print('hey')
        print(block)


print(func1(5))
