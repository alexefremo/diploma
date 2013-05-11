<!DOCTYPE html>
<html>
<head>
<title>Добавить пользователя</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
    
<header>
    <div class="meta-link">Назад — <a href="/">на главную</a></div>
    <h1 class="main-title">Добавить пользователя</h1>
</header>   

<section id="content">
    <form method="post" class="form-box content-box">
        <ul>
            <li>Имя пользователя</li>
            <li><input type="text" name="username" value="{{username}}"></li>
            <li class="error">{{username_error}}</li>
            <li>Пароль</li>
            <li><input type="password" name="password" value=""></li>
            <li class="error">{{password_error}}</li>
            <li>Подтвердите пароль</li>
            <li><input type="password" name="verify" value=""></li>
            <li class="error">{{verify_error}}</li>
            <li>Email (optional)</li>
            <li><input type="text" name="email" value="{{email}}"></li>
            <li class="error">{{email_error}}</li>
            <li><input type="submit" class="form-submit"></li>
        </ul>
    </form>
</section>

<footer>
    © 2013 Саня Гончаров. Челябинск    
</footer>

</body>
</html>