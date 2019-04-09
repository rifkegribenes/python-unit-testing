blogs = dict()


def menu():
    # show user available blogs
    # wait for user choice
    # do something with choice
    # exit

    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('• {}'.format(blog))