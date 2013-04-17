<!DOCTYPE html>
<html>
<head>
<title>Диплом Сани Гончарова</title>
</head>
<body>

%if (username != None):
Сменить пользователя — <a href="/logout">Logout</a>
%end

%if (username == 'luzlol'):
<h1>Админская панель</h1>
%else:
<h1>Здравствуйте, {{username}}!</h1>
%end

<table>
%for doc in data:
<tr>
<td>{{doc['a']}}</td><td>{{doc['b']}}</td><td>{{doc['c']}}</td>
</tr>
%end
</table>

</body>
</html>