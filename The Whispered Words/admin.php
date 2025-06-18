<?php
session_start();
if ($_SESSION['username'] !== 'admin') {
    die("Access denied.");
}

$conn = new mysqli("localhost", "ctf", "", "ctf_sqli1");
$result = $conn->query("SELECT * FROM messages");

echo "<h2>All Messages</h2>";
while ($row = $result->fetch_assoc()) {
    echo "<b>{$row['sender']} → {$row['recipient']}</b>: " . htmlspecialchars($row['content']) . "<br><br>";
}
