MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'

blogs = dict()


def menu():
    # show user available blogs
    # wait for user choice
    # do something with choice
    # exit

    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('• {}'.format(blog))