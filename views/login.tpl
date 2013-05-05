<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
Добро пожаловать, зайдите в свою учетную запись

<h2>Вход в систему</h2>
<form method="post">
<table>
<tr>
<td class="label">Логин:</td>
<td><input type="text" name="username" value="{{username}}"></td>
<td class="error"></td>
</tr>
<tr>
<td class="label">Пароль:</td>
<td><input type="password" name="password" value=""></td>
<td class="error">{{login_error}}</td>
</tr>
</table>
<input type="submit">
</form>
</body>
</html>