MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'
POST_TEMPLATE = '''
--- {} ---

{}

'''

blogs = dict()
from blog import Blog
from post import Post


def menu():
    # show user available blogs
    # wait for user choice
    # do something with choice
    # exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('• {}'.format(blog))

def ask_create_blog():
    title = input('What is the title of the blog? ')
    author = input('What is your name? ')
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Which blog do you want to read? ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_title = input('Which blog do you want to post to? ')
    title = input('What is the title of the post? ')
    content = input('What is the content of the post? ')
    new_post = Post(title, content)
    for blog in blogs:
        if blog['title'] == title:
            blog.posts.append(new_post)