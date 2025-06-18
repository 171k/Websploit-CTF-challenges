<?php
$conn = new mysqli("localhost", "root", "", "ctf_db");
if ($conn->connect_error) {
    die("Connection failed.");
}

$msg = '';
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $query = "SELECT name FROM products WHERE id = $id";
    $res = $conn->query($query);
    if ($res && $res->num_rows > 0) {
        $msg = "✅ Product found.";
    } else {
        $msg = "❌ Product not found.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Boolean-Based SQLi</title>
    <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Segoe UI', sans-serif;
            max-width: 600px;
            margin: auto;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h2 { color: #333; }
        form { margin-bottom: 20px; }
        input[type="text"] {
            padding: 8px;
            width: 70%;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            padding: 8px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .result {
            font-size: 1.1em;
            color: #2c662d;
        }
    </style>
</head>
<body>
    <h2>Boolean-Based SQL Injection</h2>
    <form method="GET">
        ID: <input type="text" name="id">
        <input type="submit" value="Check">
    </form>
    <div class="result"><?= $msg ?></div>
</body>
</html>
