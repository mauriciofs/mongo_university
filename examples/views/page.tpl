<html>
<head>
<title>
    Hey
</title>
</head>
<body>
    <p>Hello</p>
    <ul>
        %for thing in things:
            <li>{{thing}}</li>
        %end
    </ul>
    <form action="/addfruit" method="POST">
        <input type="text" name="fruit" value="banana"><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>