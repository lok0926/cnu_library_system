from config.config_db import connection_db


# 회원목록 조회
def get_members():
    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = '''
                SELECT *
                FROM tbl_member;
              '''
        curs.execute(sql)
        rows = curs.fetchall()
    finally:
        conn.close()

    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: ISBN\tNAME\tPHONE\tDATA')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    for row in rows:
        print(f':: {row.values()}')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')


# 회원 유무 판단
def member_match(member_num):
    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = f'''
               SELECT *
               FROM tbl_member
               WHERE member_id = "{member_num}"
              '''
        curs.execute(sql)
        result = curs.rowcount
    finally:
        conn.close()

    return result


def serch_members(member_Name):
    print(':: 회원 이름을 검색하세요.' )
    member_name = input('>> 회원 이름: ')

    result = member_Match(member_Name)

    if result == 1:
        print('회원이 맞습니다.')
    else:
        print('존재하지 않는 회원입니다.')


def member_Match(member_Name):
    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = f'''
                SELECT *
                FROM tbl_member
                WHERE member_name = "{member_Name}"
               '''
        curs.execute(sql)
        result = curs.rowcount
    finally:
        conn.close()

    return result