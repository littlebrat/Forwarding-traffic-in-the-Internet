from proj1.tests.test_read_files import files_test

trees = files_test()

i = 0
for tree in trees:
    print("\n>>> Initial %d" % i)
    tree.print()

    print("\n>>> After %d" % i)
    tree.normalize()
    tree.print()

    i += 1
