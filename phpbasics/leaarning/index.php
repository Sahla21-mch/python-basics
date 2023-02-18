<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <form action = "./link.php" method = "POST">
        <h3>LOGIN FORM</h3>
        <div id="first">
            <label>Name</label>
            <input type ="text" name="name" id="name">
            <label>Email</label>
            <input type="email" name="email" id="mail">
        </div>
        <div id="second">
            <label>Address</label>
            <input type="address" name="address" >
            <label>Password</label>
            <input type="password" name="password" >
        </div>
        <button id="submit" type="submit" name="submit" value="submit">submit</button>

    </form>
</body>
</html>