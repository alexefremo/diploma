<!DOCTYPE html>
<html>
<head>
<title>My Blog</title>
</head>
<body>

%if (username != None):
Добро пожаловать, {{username}}        <a href="/logout">Logout</a>
%end

<h1>Домашняя страница</h1>

<ul>
<li></li>
<li></li>
<li></li>
</ul>
<table>
%for doc in data:
<tr>
<td>{{doc['a']}}</td><td>{{doc['b']}}</td><td>{{doc['c']}}</td>
</tr>
%end
</table>

</body>
</html>


