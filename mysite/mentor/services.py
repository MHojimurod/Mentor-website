from django.db import connection
from contextlib import closing


def get_course():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mentor_faculty."name" ,mentor_trainers.image as trimg, mentor_trainers.full_name ,mentor_course.* 
        from mentor_faculty inner join (mentor_course inner join mentor_trainers on
         mentor_course.trainer_id=mentor_trainers.id) on mentor_faculty.id =mentor_course.faculty_id """)
        course = dict_fetchall(cursor)
        return course


def get_trainers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mentor_trainers.*, mentor_faculty."name"as name 
           from mentor_trainers inner join mentor_faculty on mentor_faculty.id=mentor_trainers.faculty_id  """)
        trainers = dict_fetchall(cursor)
        return trainers


def get_events():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_events""")
        events = dict_fetchall(cursor)
        return events


def get_newsletter():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_newsletter""")
        emails = dict_fetchall(cursor)
        return emails


def get_course_by_id(course_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mentor_course.*,mentor_trainers.full_name from mentor_course inner
         join mentor_trainers on mentor_course.trainer_id = mentor_trainers.id where mentor_course.id=%s""",
                       [course_id])
        course = dict_fetchone(cursor)
        return course

def get_trainers_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(mentor_trainers.id) from mentor_trainers""")
        count = dict_fetchall(cursor)
        return count

def get_events_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(mentor_events.id) from mentor_events""")
        count = dict_fetchall(cursor)
        return count

def get_courses_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(mentor_course.id) from mentor_course""")
        count = dict_fetchall(cursor)
        return count

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
