<?php
session_start();
if (!isset($_SESSION['username'])) {
    die("Please login first.");
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>User Panel</title>
</head>
<body>
    <h2>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?></h2>
    <form method="POST" action="send.php">
        Send To:
        <select name="to">
            <option value="caesar">Caesar</option>
            <option value="robert">Robert</option>
            <option value="rose">Rose</option>
        </select><br><br>
        Message:<br>
        <textarea name="message" rows="4" cols="30"></textarea><br><br>
        <button type="submit">Send</button>
    </form>
</body>
</html>
