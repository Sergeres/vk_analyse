# -*- coding: utf-8 -*-
import sqlite3
import pandas as pand
import matplotlib.pyplot as plt
from jinja2 import Environment, FunctionLoader, PackageLoader, PrefixLoader, DictLoader, FileSystemLoader

html = '''
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href="style.css" rel="stylesheet" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script src="script.js"></script>
    <style>
    /*!
     * chiefSlider (https://itchief.ru/lessons/php/feedback-form-for-website)
     * Copyright 2018 Alexander Maltsev
     * Licensed under MIT (https://github.com/itchief/feedback-form/blob/master/LICENSE)
     */

    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
      color: #fff;
      height: 300px;
    }

    .slider {
      position: relative;
      overflow: hidden;
    }

    .slider__wrapper {
      display: flex;
      transition: transform 0.6s ease;
    }

    .slider__item {
      flex: 0 0 100%;
      max-width: 100%;
    }

    .slider__control {
      position: absolute;
      top: 50%;
      display: none;
      align-items: center;
      justify-content: center;
      width: 40px;
      color: #fff;
      text-align: center;
      opacity: 0.5;
      height: 50px;
      transform: translateY(-50%);
      background: rgba(0, 0, 0, .5);
    }

    .slider__control_show {
      display: flex;
    }

    .slider__control:hover,
    .slider__control:focus {
      color: #fff;
      text-decoration: none;
      outline: 0;
      opacity: .9;
    }

    .slider__control_left {
      left: 0;
    }

    .slider__control_right {
      right: 0;
    }

    .slider__control::before {
      content: '';
      display: inline-block;
      width: 20px;
      height: 20px;
      background: transparent no-repeat center center;
      background-size: 100% 100%;
    }

    .slider__control_left::before {
      background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
    }

    .slider__control_right::before {
      background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
    }

    .slider__item>div {
      line-height: 500px;
      font-size: 100px;
      text-align: center;
    }
  </style>
  </head>
  <body>
      <br>
      {% for user in members %}
        <li>{{ user }}</li>
      {% endfor %}
      <br>
        <div id="slider-wrap">
            <div id="slider">
            {% for name in memsss %}
                <div class="slide"><img src="{{ name }}" width="500" height="300"></div>
            {% endfor %}
            </div>
        </div>	
        
            
      <table align="center">
        <tr>
            <td colspan="2" align="center">
            <p></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" align="center">
            
            </td>
        </tr>
        <tr>
            <td colspan="2" align="center">
            <img src="{{ url1 }}" alt="альтернативный текст">
            </td>
        </tr>
        <tr>
            <td align="center">
            <p>Top 5 groups of Women</p>
            </td>
            <td align="center">
            <p>Top 5 groups of Men</p>
            </td>
        </tr>
        <tr>
            <td>
            <img src="{{ url2 }}" alt="альтернативный текст">
            </td>
            <td>
            <img src="{{ url3 }}" alt="альтернативный текст">
            </td>
        <tr>
        <tr>
            <td>
            
            </td>
            <td>
            
            </td>
        </tr>
      </table>
      <div class="slider" >
                <div class="slider__wrapper">
                {% for name in mems %}
                    <div class="slider__item">
                        <div style="height: 475px; background: white;"> <img src="{{ name }}"> </div>
                    </div>
                {% endfor %}
                </div>
                <a class="slider__control slider__control_left" href="#" role="button"></a>
                <a class="slider__control slider__control_right slider__control_show" href="#" role="button"></a>
        </div>
        <br>
        <div class="slider" >
                <div class="slider__wrapper">
                {% for name in mems %}
                    <div class="slider__item">
                        <div style="height: 475px; background: white;"> <img src="{{ name }}"> </div>
                    </div>
                {% endfor %}
                </div>
                <a class="slider__control slider__control_left" href="#" role="button"></a>
                <a class="slider__control slider__control_right slider__control_show" href="#" role="button"></a>
        </div>
  </body>
  
  <script>
    'use strict';
    var multiItemSlider = (function () {
      return function (selector, config) {
        var
          _mainElement = document.querySelector(selector), // основный элемент блока
          _sliderWrapper = _mainElement.querySelector('.slider__wrapper'), // обертка для .slider-item
          _sliderItems = _mainElement.querySelectorAll('.slider__item'), // элементы (.slider-item)
          _sliderControls = _mainElement.querySelectorAll('.slider__control'), // элементы управления
          _sliderControlLeft = _mainElement.querySelector('.slider__control_left'), // кнопка "LEFT"
          _sliderControlRight = _mainElement.querySelector('.slider__control_right'), // кнопка "RIGHT"
          _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
          _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента    
          _positionLeftItem = 0, // позиция левого активного элемента
          _transform = 0, // значение транфсофрмации .slider_wrapper
          _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
          _items = []; // массив элементов
        // наполнение массива _items
        _sliderItems.forEach(function (item, index) {
          _items.push({ item: item, position: index, transform: 0 });
        });

        var position = {
          getMin: 0,
          getMax: _items.length - 1,
        }

        var _transformItem = function (direction) {
          if (direction === 'right') {
            if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
              return;
            }
            if (!_sliderControlLeft.classList.contains('slider__control_show')) {
              _sliderControlLeft.classList.add('slider__control_show');
            }
            if (_sliderControlRight.classList.contains('slider__control_show') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
              _sliderControlRight.classList.remove('slider__control_show');
            }
            _positionLeftItem++;
            _transform -= _step;
          }
          if (direction === 'left') {
            if (_positionLeftItem <= position.getMin) {
              return;
            }
            if (!_sliderControlRight.classList.contains('slider__control_show')) {
              _sliderControlRight.classList.add('slider__control_show');
            }
            if (_sliderControlLeft.classList.contains('slider__control_show') && _positionLeftItem - 1 <= position.getMin) {
              _sliderControlLeft.classList.remove('slider__control_show');
            }
            _positionLeftItem--;
            _transform += _step;
          }
          _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
        }

        // обработчик события click для кнопок "назад" и "вперед"
        var _controlClick = function (e) {
          var direction = this.classList.contains('slider__control_right') ? 'right' : 'left';
          e.preventDefault();
          _transformItem(direction);
        };

        var _setUpListeners = function () {
          // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
          _sliderControls.forEach(function (item) {
            item.addEventListener('click', _controlClick);
          });
        }

        // инициализация
        _setUpListeners();

        return {
          right: function () { // метод right
            _transformItem('right');
          },
          left: function () { // метод left
            _transformItem('left');
          }
        }

      }
    }());

    var slider = multiItemSlider('.slider')

  </script>
</html>
'''


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
    for i in range(rows.__len__()):
        rows[i] = rows[i] * 100 / summa
    dataframe = pand.DataFrame()
    dataframe['Проценты'] = rows
    dataframe['Категории'] = x_row
    agraph = dataframe.plot(x = 'Категории', kind = 'bar', color = 'teal')
    agraph.set(xlabel = "Категории возрастов", ylabel = "Проценты")
    plt.tight_layout()
    plt.savefig('1.png')
    return rows


# def top_communityG(conn):
#     cur = conn.cursor()
#     cur.execute("select VSU_Member_Community.name, count(*) from VSU_Member_Community join VSU_Member on VSU_Member_Community.memberID = VSU_Member.id where VSU_Member.gender = 'Жен.' group by VSU_Member_Community.name order by count(*) DESC limit 5")
#     data = cur.fetchall()
#     name =  []
#     count = []
#     for row in data:
#         name.append(row[0])
#         count.append(row[1])
#     dataframe = pand.DataFrame()
#     dataframe["Имена"] = name
#     dataframe["Количество"] = count
#     bgraph = dataframe.plot(x = 'Имена', kind = 'bar', color = 'c')
#     bgraph.set(xlabel = "Имена", ylabel = "Количество")
#     plt.tight_layout()
#     plt.savefig('2.png')


def top_communityM(conn, gen):
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
        plt.savefig('Mtop.png')
    else:
        plt.savefig('Wtop.png')


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
            plt.savefig('top5_W'+str(i)+'.png')
            graphs.append('top5_W'+str(i)+'.png')
        else:
            cgraph = dataframe.plot(x='Имена', kind='bar', color='c', title="Мужчины " + x_row[i])
            cgraph.set(xlabel="Названия групп", ylabel="Количество")
            plt.tight_layout()
            plt.savefig('top5_M' + str(i) + '.png')
            graphs.append('top5_M' + str(i) + '.png')
    return graphs

env = Environment(loader = DictLoader({'index.html': html}))
template = env.get_template('index.html')
# print(template.render(name=members[0], photo_50 = member_communities[0]))
# conn = create_connection(r"D:\5th Semestr\MMAD\vkAnalyse\vk_members_2019_10_21.db")
select_mem(create_conn(r"D:\\5th Semestr\\MMAD\\vkAnalyse\\vk_members_2019_10_22.db"))
top_communityM(create_conn(r"D:\\5th Semestr\\MMAD\\vkAnalyse\\vk_members_2019_10_22.db"), 'Жен.')
top_communityM(create_conn(r"D:\\5th Semestr\\MMAD\\vkAnalyse\\vk_members_2019_10_22.db"), 'Муж.')
graphs = top_ages(create_conn(r"D:\\5th Semestr\\MMAD\\vkAnalyse\\vk_members_2019_10_22.db"), 'Жен.')
tgraphs = top_ages(create_conn(r"D:\\5th Semestr\\MMAD\\vkAnalyse\\vk_members_2019_10_22.db"), 'Муж.')
with open("new.html", "w") as f:
    f.write(template.render(url1 = '1.png', url2 = 'Wtop.png', url3 = 'Mtop.png', mems = graphs, memso = tgraphs))

