import bench


def func(a):
    pass


def test(num):
    for i in iter(range(num)):
        func(i)


bench.run(test)
