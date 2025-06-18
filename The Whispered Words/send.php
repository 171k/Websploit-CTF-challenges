<?php
session_start();
$conn = new mysqli("localhost", "ctf", "", "ctf_sqli1");

$from = $_SESSION['username'];
$to = $_POST['to'];
$msg = $_POST['message'];

$stmt = $conn->prepare("INSERT INTO messages (sender, recipient, content) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $from, $to, $msg);
$stmt->execute();

echo "Message sent! <a href='user.php'>Back</a>";
