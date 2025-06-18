<?php
ini_set('log_errors', 1);
ini_set('error_log', '/tmp/php-error.log');
error_reporting(E_ALL);

$conn = new mysqli("localhost", "root", "", "ctf_db");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$user = $_POST['username'];
$pass = $_POST['password'];

$sql = "SELECT * FROM users WHERE username = '$user' AND password = '$pass'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<h3>Login success! ACS{you_got_injection_right}</h3>";
} else {
    echo "Invalid credentials.";
}
?>
