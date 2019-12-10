# -*- coding: utf-8 -*-
import sqlite3
import vk
import pandas as pand
import db
import matplotlib.pyplot as plt
from jinja2 import Environment, FunctionLoader, PackageLoader, PrefixLoader, DictLoader, FileSystemLoader
session = vk.Session(access_token='d5b441ccd5b441ccd5b441cc0bd5d94752dd5b4d5b441cc883ce57ed215c145977b71cd')
api = vk.API(session)
v = 5.103

def create_conn(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn


def select_mem(conn):
    rows = []
    cur = conn.cursor()
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age < 18")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 18 and age < 21")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 21 and age < 24")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 24 and age < 27")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 27 and age < 30")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 30 and age < 35")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 35 and age < 45")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age > 45")
    rows.append(cur.fetchall()[0])
    rows = list(sum(rows, ()))
    summa = sum(rows)
    x_row = ["< 18","18-21","21-24","24-27","27-30","30-35","35-45","> 45"]
    dataframe = pand.DataFrame()
    dataframe['Количество'] = rows
    dataframe['Категории'] = x_row
    agraph = dataframe.plot(x='Категории', kind='bar', color='teal')
    agraph.set(xlabel="Категории возрастов", ylabel="Количество")
    plt.tight_layout()
    plt.savefig('templates/screenshots/categoryGroupscount.png')
    for i in range(rows.__len__()):
        if rows[i] == 0:
            continue
        else:
            rows[i] = rows[i] * 100 / summa
    dataframe = pand.DataFrame()
    dataframe['Проценты'] = rows
    dataframe['Категории'] = x_row
    agraph = dataframe.plot(x = 'Категории', kind = 'bar', color = 'teal')
    agraph.set(xlabel = "Категории возрастов", ylabel = "Проценты")
    plt.tight_layout()
    plt.savefig('templates/screenshots/categoryGroups.png')
    plt.close('all')
    return rows


def select_member_noedc(conn):
    rows = []
    cur = conn.cursor()
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age < 18 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 18 and age < 21 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 21 and age < 24 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 24 and age < 27 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 27 and age < 30 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 30 and age < 35 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age >= 35 and age < 45 and university is null ")
    rows.append(cur.fetchall()[0])
    cur.execute("SELECT count(name) FROM VSU_Member WHERE age > 45 and university is null ")
    rows.append(cur.fetchall()[0])
    rows = list(sum(rows, ()))
    summa = sum(rows)
    x_row = ["< 18","18-21","21-24","24-27","27-30","30-35","35-45","> 45"]
    # for i in range(rows.__len__()):
    #     if rows[i] == 0:
    #         continue
    #     else:
    #         rows[i] = rows[i] * 100 / summa
    dataframe = pand.DataFrame()
    dataframe['Количество'] = rows
    dataframe['Категории'] = x_row
    agraph = dataframe.plot(x = 'Категории', kind = 'bar', color = 'teal')
    agraph.set(xlabel = "Категории возрастов", ylabel = "Количество")
    plt.tight_layout()
    plt.savefig('templates/screenshots/membersNOEDC.png')
    plt.close('all')
    return rows


def top_community(conn, gen):
    cur = conn.cursor()
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data = cur.fetchall()
    name =  []
    count = []
    for row in data:
        name.append(row[0])
        count.append(row[1])
    dataframe = pand.DataFrame()
    dataframe["Имена"] = name
    dataframe["Количество"] = count
    cgraph = dataframe.plot(x = 'Имена', kind = 'bar', color = 'c')
    cgraph.set(xlabel = "Названия групп", ylabel = "Количество")
    plt.tight_layout()
    if gen == 'Муж.':
        plt.savefig('templates/screenshots/mensTOP5.png')
    else:
        plt.savefig('templates/screenshots/womensTOP5.png')


def top_ages(conn, gen):
    data = []
    cur = conn.cursor()
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age < 18 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 18 and VSU_Member.age < 21 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 21 and VSU_Member.age < 24 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 24 and VSU_Member.age < 27 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 27 and VSU_Member.age < 30 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 30 and VSU_Member.age < 35 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 35 and VSU_Member.age < 45 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender =:gen and VSU_Member.age >= 45 group by VSU_Member_Community.name order by count(*) DESC limit 5", {"gen": gen})
    data.append(cur.fetchall())
    x_row = ["меньше 18", "от 18 до 21", "от 21 до 24", "от 24 до 27", "от 27 до 30", "от 30 до 35", "от 35 до 45", "больше 45"]
    graphs = []
    for i in range(data.__len__()):
        name = []
        count = []
        for row in data[i]:
            name.append(row[0])
            count.append(row[1])
        dataframe = pand.DataFrame()
        dataframe["Имена"] = name
        dataframe["Количество"] = count
        if gen == 'Жен.':
            cgraph = dataframe.plot(x='Имена', kind='bar', color='c', title  = "Женщины " + x_row[i])
            cgraph.set(xlabel="Названия групп", ylabel="Количество")
            plt.tight_layout()
            plt.savefig('templates/screenshots/top5_W'+str(i)+'.png')
            graphs.append('screenshots/top5_W'+str(i)+'.png')
        else:
            cgraph = dataframe.plot(x='Имена', kind='bar', color='c', title="Мужчины " + x_row[i])
            cgraph.set(xlabel="Названия групп", ylabel="Количество")
            plt.tight_layout()
            plt.savefig('templates/screenshots/top5_M' + str(i) + '.png')
            graphs.append('screenshots/top5_M' + str(i) + '.png')
    return graphs


def peoplewoage(conn):
    data = []
    cur = conn.cursor()
    cur.execute("select count(*) from VSU_Member")
    data.append(cur.fetchall()[0])
    cur.execute("select count(*) from VSU_Member where age not null")
    data.append(cur.fetchall()[0])
    data = list(sum(data, ()))
    data[0] = data[0] - data[1]
    labels = 'Не указали возраст', 'Указали возраст'
    sizes = [(data[0]/(data[0] + data[1])*100), (data[1]/(data[0] + data[1])*100)]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Распределение пользователей по наличию возраста.")
    plt.savefig('templates/screenshots/piemembers' + '.png')
    plt.close('all')


def toplike(conn):
    data, result = [], []
    href = []
    cur = conn.cursor()
    # cur.execute("select postID, count(*) from VSU_Member_Activity where like == 1 group by postID order by count(*) desc limit 5")
    cur.execute("select * from VSU_Post order by likes desc limit 5")
    data.append(cur.fetchall())
    for i in range(data[0].__len__()):
        result.append(['https://vk.com/prcom_vyatsu?w=wall-108366262_' + str(data[0][i][0]), data[0][i][5]])
        href.append('-108366262_' + str(data[0][i][0]))
    return result, href


def topcomment(conn):
    data, result = [], []
    cur = conn.cursor()
    cur.execute("select * from VSU_Post order by comments desc limit 5")
    data.append(cur.fetchall())
    for i in range(data[0].__len__()):
        result.append(['https://vk.com/prcom_vyatsu?w=wall-108366262_' + str(data[0][i][0]), data[0][i][6]])
    return result


def timeanalyse(conn):
    timeset = []
    timeperiods = ["publishTime >= '00-00-00' and publishTime < '01-00-00'", "publishTime >= '01-00-00' and publishTime < '02-00-00'", "publishTime >= '02-00-00' and publishTime < '03-00-00'", "publishTime >= '03-00-00' and publishTime < '04-00-00'",
                   "publishTime >= '04-00-00' and publishTime < '05-00-00'", "publishTime >= '05-00-00' and publishTime < '06-00-00'", "publishTime >= '06-00-00' and publishTime < '07-00-00'", "publishTime >= '07-00-00' and publishTime < '08-00-00'",
                   "publishTime >= '08-00-00' and publishTime < '09-00-00'", "publishTime >= '09-00-00' and publishTime < '10-00-00'", "publishTime >= '10-00-00' and publishTime < '11-00-00'", "publishTime >= '11-00-00' and publishTime < '12-00-00'",
                   "publishTime >= '12-00-00' and publishTime < '13-00-00'", "publishTime >= '13-00-00' and publishTime < '14-00-00'", "publishTime >= '14-00-00' and publishTime < '15-00-00'", "publishTime >= '15-00-00' and publishTime < '16-00-00'",
                   "publishTime >= '16-00-00' and publishTime < '17-00-00'", "publishTime >= '17-00-00' and publishTime < '18-00-00'", "publishTime >= '18-00-00' and publishTime < '19-00-00'", "publishTime >= '19-00-00' and publishTime < '20-00-00'",
                   "publishTime >= '20-00-00' and publishTime < '21-00-00'", "publishTime >= '21-00-00' and publishTime < '22-00-00'", "publishTime >= '22-00-00' and publishTime < '23-00-00'", "publishTime >= '23-00-00' and publishTime < '24-00-00'"]
    cur = conn.cursor()
    for i in timeperiods:
        cur.execute("select count(*), sum(likes) from VSU_Post where "  +  (str)(i))
        timeset.append(cur.fetchall())
    y_row = []
    for i in timeset:
        if i[0][1] == None:
            y_row.append(0)
        else:
            y_row.append(i[0][1]/i[0][0])
    x_row = ["0:00", "1:00", "2:00", "3:00",
             "4:00", "5:00", "6:00", "7:00",
             "8:00", "9:00", "10:00", "11:00",
             "12:00", "13:00", "14:00", "15:00",
             "16:00", "17:00", "18:00", "19:00",
             "20:00", "21:00", "22:00", "23:00"]
    dataframe = pand.DataFrame()
    dataframe["Время"] = x_row
    dataframe["Среднее кол-во лайков"] = y_row
    cgraph = dataframe.plot(x='Время', kind='line', color='c')
    cgraph.set(xlabel="Время", ylabel="Среднее кол-во лайков")
    plt.tight_layout()
    plt.savefig('templates/screenshots/timespread.png')


def viewanalyse(conn):
    timeset = []
    timeperiods = ["publishTime >= '00-00-00' and publishTime < '01-00-00'", "publishTime >= '01-00-00' and publishTime < '02-00-00'", "publishTime >= '02-00-00' and publishTime < '03-00-00'", "publishTime >= '03-00-00' and publishTime < '04-00-00'",
                   "publishTime >= '04-00-00' and publishTime < '05-00-00'", "publishTime >= '05-00-00' and publishTime < '06-00-00'", "publishTime >= '06-00-00' and publishTime < '07-00-00'", "publishTime >= '07-00-00' and publishTime < '08-00-00'",
                   "publishTime >= '08-00-00' and publishTime < '09-00-00'", "publishTime >= '09-00-00' and publishTime < '10-00-00'", "publishTime >= '10-00-00' and publishTime < '11-00-00'", "publishTime >= '11-00-00' and publishTime < '12-00-00'",
                   "publishTime >= '12-00-00' and publishTime < '13-00-00'", "publishTime >= '13-00-00' and publishTime < '14-00-00'", "publishTime >= '14-00-00' and publishTime < '15-00-00'", "publishTime >= '15-00-00' and publishTime < '16-00-00'",
                   "publishTime >= '16-00-00' and publishTime < '17-00-00'", "publishTime >= '17-00-00' and publishTime < '18-00-00'", "publishTime >= '18-00-00' and publishTime < '19-00-00'", "publishTime >= '19-00-00' and publishTime < '20-00-00'",
                   "publishTime >= '20-00-00' and publishTime < '21-00-00'", "publishTime >= '21-00-00' and publishTime < '22-00-00'", "publishTime >= '22-00-00' and publishTime < '23-00-00'", "publishTime >= '23-00-00' and publishTime < '24-00-00'"]
    cur = conn.cursor()
    for i in timeperiods:
        cur.execute("select count(*), sum(views) from VSU_Post where "  +  (str)(i))
        timeset.append(cur.fetchall())
    y_row = []
    for i in timeset:
        if i[0][1] == None:
            y_row.append(0)
        else:
            y_row.append(i[0][1]/i[0][0])
    x_row = ["0:00", "1:00", "2:00", "3:00",
             "4:00", "5:00", "6:00", "7:00",
             "8:00", "9:00", "10:00", "11:00",
             "12:00", "13:00", "14:00", "15:00",
             "16:00", "17:00", "18:00", "19:00",
             "20:00", "21:00", "22:00", "23:00"]
    dataframe = pand.DataFrame()
    dataframe["Время"] = x_row
    dataframe["Среднее кол-во просмотров"] = y_row
    cgraph = dataframe.plot(x='Время', kind='line', color='c')
    cgraph.set(xlabel="Время", ylabel="Среднее кол-во просмотров")
    plt.tight_layout()
    plt.savefig('templates/screenshots/viewsspred.png')


datamas = (api.wall.getById(posts='-108366262_6011', v=v, offset='0'))
# print(datamas[0].keys())
posttext = (datamas[0]['text'])
urlsrc = (datamas[0]['attachments'][0]['photo']['sizes'][3]['url'])

env = Environment(loader = FileSystemLoader('templates/'))
template = env.get_template('templateRE.html')
# print(db.generate_db_name())
peoplewoage(create_conn(db.generate_db_name()))
select_mem(create_conn(db.generate_db_name()))
top_community(create_conn(db.generate_db_name()), 'Жен.')
top_community(create_conn(db.generate_db_name()), 'Муж.')
graphs = top_ages(create_conn(db.generate_db_name()), 'Жен.')
tgraphs = top_ages(create_conn(db.generate_db_name()), 'Муж.')
datas, href = toplike(create_conn(db.generate_db_name()))
comments = topcomment(create_conn(db.generate_db_name()))
select_member_noedc(create_conn(db.generate_db_name()))
timeanalyse(create_conn(db.generate_db_name()))
viewanalyse(create_conn(db.generate_db_name()))

dataroll =[]
for i in href:
    datamas = (api.wall.getById(posts=i, v=v, offset='0'))
    # print(datamas[0].keys())
    posttext = (datamas[0]['text'])
    urlsrc = (datamas[0]['attachments'][0]['photo']['sizes'][3]['url'])
    dataroll.append([posttext, urlsrc])

with open("templates/new.html", "w", encoding='utf-8') as f:
    f.write(template.render(url1 = 'screenshots/categoryGroups.png', url2 = 'screenshots/womensTOP5.png', url3 = 'screenshots/mensTOP5.png', mems = graphs, mems0 = tgraphs, url4 = 'screenshots/piemembers.png', datas = datas, comments = comments, url5 = 'screenshots/membersNOEDC.png', url6 = 'screenshots/categoryGroupscount.png', dataroll = dataroll, url7='screenshots/viewsspred.png', url8='screenshots/timespread.png'))

