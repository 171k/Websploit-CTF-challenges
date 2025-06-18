<?php
$conn = new mysqli("localhost", "root", "", "ctf_db");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$result = '';
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $query = "SELECT name FROM products WHERE id = $id";
    $res = $conn->query($query); // use $conn, not $db

    if ($res) {
        while ($row = $res->fetch_assoc()) { // use fetch_assoc() for MySQLi
            $result .= "Product: " . htmlspecialchars($row['name']) . "<br>";
        }
    } else {
        $result = "Error: " . htmlspecialchars($conn->error);
    }
}
?>


<!DOCTYPE html>
<html>
<head>
    <title>Union-Based SQLi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 40px;
        }

        h2 {
            color: #333;
        }

        form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            width: 300px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        input[type="text"], input[name="id"] {
            padding: 8px;
            width: 90%;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="submit"] {
            padding: 8px 16px;
            background: #007BFF;
            border: none;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background: #0056b3;
        }

        div {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h2>Find Product</h2>
    <form method="GET">
        ID: <input name="id" type="text">
        <input type="submit" value="Search">
    </form>
    <div><?= $result ?></div>
</body>
</html>

