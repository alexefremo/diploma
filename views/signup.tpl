<!DOCTYPE html>
<html>
<head>
<title>Добавить пользователя</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
Назад — <a href="/">на главную</a>

<h1>Добавить пользователя</h1>

<form method="post">
<table>
<tr>
<td class="label">Username</td>
<td><input type="text" name="username" value="{{username}}"></td>
<td class="error">{{username_error}}</td>
</tr>
<tr>
<td class="label">Password</td>
<td><input type="password" name="password" value=""></td>
<td class="error">{{password_error}}</td>
</tr>
<tr>
<td class="label">Verify Password</td>
<td><input type="password" name="verify" value=""></td>
<td class="error">{{verify_error}}</td>
</tr>
<tr>
<td class="label">Email (optional)</td>
<td><input type="text" name="email" value="{{email}}"></td>
<td class="error">{{email_error}}</td>
</tr>
</table>
<input type="submit">
</form>
  
</body>
</html>