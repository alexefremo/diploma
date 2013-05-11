<!DOCTYPE html>
<html>
<head>
<title>Вход в систему</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header>
    <h1>Вход в систему</h1>
</header>    

<section id="content">
    <form method="post" class="form-box content-box">
        <ul>
            <li>Логин</li>
            <li><input type="text" name="username" value="{{username}}"></li>
            <li>Пароль</li>
            <li><input type="password" name="password" value=""></li>
            <li><span class="error">{{login_error}}</span></li>
            <li><input type="submit" class="form-submit"></li>
        </ul>
    </form>
</section>

<footer>
    © 2013 Саня Гончаров. Челябинск    
</footer>

</body>
</html>