import sqlite3
from settings import *


db_name = 'blog.db'
conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(PATH + db_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query, params=None):
    cursor.execute(query, params)
    conn.commit()

def getPostsByCategory(category_name):
    open()
    cursor.execute(
        '''SELECT * FROM post, category WHERE post.category_id=category.category_id and category_name=(?) ORDER BY post_id DESC''', [category_name])
    posts = cursor.fetchall()
    close()

    return posts


def getIdByCategory(category_id):
    open()
    cursor.execute(
        '''SELECT category_id FROM category WHERE category_name=(?)''', [category_id])
    category_id = cursor.fetchone()['category_id']
    close()
    return category_id


