import sqlite3
from datetime import datetime
import re
import os


def generate_db_name():
    year_now = str(datetime.now().year)
    month_now = str(datetime.now().month)
    day_now = str(datetime.now().day)

    date_now = year_now + '_' + month_now + '_' + day_now

    db_name = 'vk_members_' + str(date_now) + '.db'
    return db_name


def create_db(remove):
    db_name = generate_db_name()

    if os.path.isfile(db_name) and remove:
        os.remove(db_name)

    connection = sqlite3.connect(db_name)
    return connection


def create_tables():
    connection = create_db(True)
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE VSU_Community'
                   '(id integer primary key, '
                   'name text, '
                   'info text, '
                   'href text)')

    cursor.execute('CREATE TABLE VSU_Member'
                   '(id integer primary key, '
                   'name varchar(100), '
                   'gender varchar(10), '
                   'age integer, '
                   'university varchar(150),'
                   'faculty varchar(150))')

    cursor.execute('CREATE TABLE VSU_Member_Activity'
                   '(like integer,'
                   'repost integer,'
                   'comment integer,'
                   'postID integer,'
                   'memberID integer,'
                   'communityID integer,'
                   'foreign key(postID) references VSU_Post(id),'
                   'foreign key(memberID) references VSU_Member(id),'
                   'foreign key(communityID) references VSU_Community(id))')

    cursor.execute('CREATE TABLE VSU_Member_Community'
                   '(memberID integer,'
                   'communityID integer, '
                   'href text, '
                   'name text,'
                   'foreign key(memberID) references VSU_Member(id))')

    cursor.execute('CREATE TABLE VSU_Post'
                   '(id integer,'
                   'content text,'
                   'publishDate DATE,'
                   'publishTime TIME,'
                   'views integer,'
                   'likes integer,'
                   'comments integer,'
                   'reposts integer'
                   ')')

    connection.commit()
    connection.close()


def members_insert(members):
    connection = create_db(False)
    cursor = connection.cursor()

    for member in members:
        # print(member)
        for info in member:
            # print(info)
            member_id = info['id']
            member_name = info['first_name'] + ' ' + info['last_name']
            university = None
            faculty = None
            try:
                if info['university']:
                    university = info['university_name']
                    if info['faculty']:
                        faculty = info['faculty_name']
            except:
                print('education is null')
            gender = ''
            if info['sex'] == 1:
                gender = 'Жен.'
            else:
                gender = 'Муж.'

            # Do Age calculating
            bdate = ''
            # Check bdate for exist in dictionary
            if 'bdate' in info:
                # Check bdate for completeness ( dd-mm-yy )
                bdate = re.match('([0-9]+?.[0-9]+?.[0-9]+)', info['bdate'])
            age = None
            if bdate:
                birth_date = bdate.group(0).split('.')
                day_bdate = int(birth_date[0])
                month_bdate = int(birth_date[1])
                year_bdate = int(birth_date[2])
                year_now = int(datetime.now().year)
                month_now = int(datetime.now().month)
                day_now = int(datetime.now().day)

                if day_now > day_bdate and month_now > month_bdate:
                    age = str(year_now - year_bdate)
                else:
                    age = str(year_now - year_bdate - 1)
            elif bdate is None:
                age = None

            cursor.execute('INSERT INTO VSU_Member(id, name, gender, age, university, faculty) '
                           'VALUES(?, ?, ?, ?, ?, ?)', [member_id, member_name, gender, age, university, faculty])

    connection.commit()
    connection.close()


def member_community_insert(members_communities):
    connection = create_db(False)
    cursor = connection.cursor()
    # print(*members_communities, sep='\n')
    for member_communities in members_communities:
        member_id = member_communities['id']
        for subscription in member_communities['subscriptions']:
            community_id = subscription['id']
            community_name = subscription['name']

            cursor.execute('INSERT INTO VSU_Member_Community(memberID, communityID, href, name)'
                           ' VALUES(?, ?, ?, ?)', [member_id, community_id, '', community_name])

    connection.commit()
    connection.close()


def vsu_community_insert(vsu_group):
    connection = create_db(False)
    cursor = connection.cursor()
    for item in vsu_group:
        # print(item)
        group_id = item['id']
        group_name = item['name']
        description = item['description']
        href = ''

        cursor.execute('INSERT INTO VSU_Community(id, name, info, href)'
                       'VALUES(?, ?, ?, ?)', [group_id, group_name, description, href])

    connection.commit()
    connection.close()


def select_users_ids():
    connection = create_db(False)
    cursor = connection.cursor()

    cursor.execute('SELECT id FROM VSU_Member')
    users = cursor.fetchall()
    users = list(sum(users, ()))

    connection.commit()
    connection.close()
    return users


def select_posts_text():
    connection = create_db(False)
    cursor = connection.cursor()

    cursor.execute('SELECT content FROM VSU_Post ORDER BY likes')
    texts = cursor.fetchall()
    texts = list(sum(texts, ()))

    connection.commit()
    connection.close()
    return texts


def insert_activities(activities):
    connection = create_db(False)
    cursor = connection.cursor()
    # print(activities)
    for activity in activities:
        user_id = activity['userID']
        post_id = activity['postID']
        like = activity['like']
        comment = activity['comment']
        # print(userID, postID, like, comment)
        cursor.execute('INSERT INTO VSU_Member_Activity(like, repost, comment, postID, memberID, communityID )'
                       'VALUES(?, ?, ?, ?, ?, ?)', [like, 0, comment, post_id, user_id, 108366262])

    connection.commit()
    connection.close()


def insert_posts(posts):
    connection = create_db(False)
    cursor = connection.cursor()

    for post in posts:
        id = post['postID']
        likes = post['likes']
        comments = post['comments']
        reposts = post['reposts']
        date = post['date']
        time = post['time']
        text = post['text']
        views = post['views']
        cursor.execute('INSERT INTO VSU_Post(id, content, publishDate, publishTime, views, likes, comments, reposts)'
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?)', [id, text, date, time, views, likes, comments, reposts])

    connection.commit()
    connection.close()