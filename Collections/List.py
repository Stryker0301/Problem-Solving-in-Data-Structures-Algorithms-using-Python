class MyClass:     
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        a = []
        a.append(5)
        a.append(4)
        a.append(2)
        a.append(40)
        print a
        print a + a
        print len(a)
        a.remove(4)
        print a
        print a.pop()
        a.sort()
        print a
        a.reverse()
        print a


if __name__ == '__main__':
    import sys
    MyClass.main(sys.argv)