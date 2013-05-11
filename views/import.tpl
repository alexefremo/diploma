<!DOCTYPE html>
<html>
<head>
<title>Импорт данных</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header>
    <div class="meta-link">Назад — <a href="/">на главную</a></div>
    <h1 class="main-title">Импортируем данные</h1>
</header>

<section id="content">
    <form method="post" enctype="multipart/form-data" class="form-box content-box">
        <ul>
            <li><input type="file" name="upload"></li>
            <li><input type="submit" class="form-submit"></li>
        </ul>
    </form>
</section>    

<footer>
    © 2013 Саня Гончаров. Челябинск    
</footer>
    
%if data == "ok":
    <script>
        window.alert("ok");
    </script>

</body>
</html>