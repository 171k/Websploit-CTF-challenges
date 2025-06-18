<?php
$conn = new mysqli("localhost", "ctf", "", "ctf_sqli1");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$new_username = $_POST['new_username'] ?? '';
$new_password = $_POST['new_password'] ?? '';

// Cek input tidak kosong
if ($new_username == '' || $new_password == '') {
    die("Username dan password tidak boleh kosong.");
}

// Cek apakah username sudah dipakai
$check = $conn->query("SELECT * FROM users WHERE username = '$new_username'");
if ($check->num_rows > 0) {
    die("Username sudah digunakan.");
}

// Insert user baru (sengaja raw SQL agar cocok dengan CTF SQLi)
$insert = "INSERT INTO users (username, password) VALUES ('$new_username', '$new_password')";
if ($conn->query($insert)) {
    echo "Akun berhasil dibuat. <a href='index.php'>Login sekarang</a>";
} else {
    echo "Gagal membuat akun: " . $conn->error;
}
?>
