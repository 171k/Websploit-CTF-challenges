<?php
session_start();

$conn = new mysqli("localhost", "ctf", "", "ctf_sqli1");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

$result = $conn->query($query);

if (!$result) {
    die("Query error: " . $conn->error);
}

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $_SESSION['username'] = $row['username'];

    // Cek apakah admin
    if ($row['username'] === 'admin') {
        header("Location: admin.php");
        exit();
    } else {
        header("Location: user.php");
        exit();
    }
} else {
    echo "Login failed.";
}
?>
