# VK_Users_analyse
Курсовая работа по ММАД
Участники: Сергей Прозоров, Дмитрий Акатов

Формулировка:

Работа скрипта должна заключаться в следующем: методом последовательного перебора
«рассмотреть» всех подписчиков группы Абитуриенты ВятГУ, собрать информацию о возрасте, поле, о тематических группах, в которых они состоят;
постах, под которыми они поставили лайки и оставили комментарии, сделали репосты.
На основе сформированного отчета подготовить анализ о тематической активности участников с учетом возрастных групп
и гендерных особенностей.

Структура проекта:
1) В файле db.py происходит непосредственно взаимодействие с базой данных, заполнение ее в автоматическом режиме.
Каждый раз генерируется новая база данных. В имени файла бд содержится тема проекта и дата его формирования 
(vk_members_YYYY_MM_DD)

2) Вся бизнес-логика: работа с vk api, получение и формирование данных для последующего добавление их базу данных,
располагается в main.py. 
    
    Получено:
    1) Участники сообщества
    2) Сообщества на которые подписан каждый участник
    
    Необходимо получить:
    1. id постов в группе Абитуриенты ВятГУ
    2. подписчиков, которые лайкнули\прокомментировали\репостнули эти посты

3) Тут еще один файл, в котором будет выполнятся работа с шаблонизатором jinja2, генерирующим html - отчет
с графиками seaborn для нашей базы данных. Он должен включать некоторую аналитику по собранным данным:
    1. статистика количества сообществ\лайков\репостов\комментариев приходится на человека с разделением по возрастам и полу.
    2. наиболее встречаемые 5 сообществ по каждому из возрастов с разделением по полу
    3. распределить лайки\репосты\комментарии по возрастам"# vk_analyse" 
