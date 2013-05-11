<!DOCTYPE html>
<html>
<head>
<title>Просмотр таблиц</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header>
    <div class="meta-link">Назад — <a href="/">на главную</a></div>
    <h1 class="main-title">Просмотр данных</h1>
</header>

<section id="content-table">
    <form method="post" class="form-box content-box">
        <ul>
            <li>Выбрать здание</li>
            <li><select name="building" value="" class="form-select">
                %for doc in buildings:
                <option value="{{doc['Здание'.decode('utf-8')]}}">{{doc['Здание'.decode('utf-8')]}}</option>
                %end
            </select></li>
            <li>Выбрать аудиторию</li>
            <li><select name="room" value="" class="form-select">
                %for doc in rooms:
                <option value="{{doc['Ответственный'.decode('utf-8')]}}">{{doc['Ответственный'.decode('utf-8')]}}</option>
                %end
            </select></li>
            <li><input type="submit" value="Искать" class="form-submit"></li>
            <li><input type="button" onClick="window.print()" value="Печать" class="form-submit"></li>
        </ul>
    </form>
    <table>
        <tr>
            <td>Наименование</td>
            <td>Инвентарный номер</td>
            <td>Дата поступления</td>
            <td>Начальное количество</td>
            <td>Цена</td>
            <td>Дата выдачи</td>
            <td>Выданое количество</td>
            <td>Здание</td>
            <td>Ответственный</td>
        </tr>
        %for doc in data:
        <tr>
            <td>{{doc['Наименование'.decode('utf-8')]}}</td>
            <td>{{doc['Инвентарный номер'.decode('utf-8')]}}</td>
            <td>{{doc['Дата поступления'.decode('utf-8')]}}</td>
            <td>{{doc['Начальное количество'.decode('utf-8')]}}</td>
            <td>{{doc['Цена'.decode('utf-8')]}}</td>
            <td>{{doc['Дата выдачи'.decode('utf-8')]}}</td>
            <td>{{doc['Выдано количество'.decode('utf-8')]}}</td>
            <td>{{doc['Здание'.decode('utf-8')]}}</td>
            <td>{{doc['Ответственный'.decode('utf-8')]}}</td>
        </tr>
        %end		
    </table>
</section>

<footer>
    © 2013 Саня Гончаров. Челябинск    
</footer>
    
</body>
</html>