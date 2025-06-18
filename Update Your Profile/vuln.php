<?php
// vulnerable-upload-avatar.php
// PERINGATAN: KODE INI SENGAJA DIBUAT TIDAK AMAN UNTUK TUJUAN EDUKASI.
// JANGAN GUNAKAN DI LINGKUNGAN PRODUKSI.

$uploadDir = 'uploads/'; // Direktori untuk menyimpan file yang diunggah
// Tidak ada pembuatan direktori yang aman atau pemeriksaan izin yang ketat saat runtime,
// namun Dockerfile akan membuat dan mengatur izin awal.

header('Content-Type: application/json');

$response = [
    'success' => false,
    'message' => 'An unknown error occurred.',
    'filePath' => null,
    'debug_original_filename' => null,
    'debug_file_type' => null
];

// Coba buat direktori 'uploads' jika belum ada (walaupun Dockerfile seharusnya sudah membuat)
// Ini hanya sebagai fallback jika Dockerfile tidak membuat atau izinnya salah.
if (!is_dir($uploadDir)) {
    // @mkdir sengaja dibuat untuk menekan error jika sudah ada atau tidak bisa dibuat
    // Dalam skenario rentan, kita mungkin tidak peduli dengan error handling yang baik.
    @mkdir($uploadDir, 0777, true); // 0777 sangat permisif, bagian dari 'vulnerable by design'
}


if (isset($_FILES['avatar'])) {
    $file = $_FILES['avatar'];

    $response['debug_original_filename'] = $file['name'];
    $response['debug_file_type'] = $file['type']; // Tipe MIME dari klien, bisa dipalsukan.

    // KERENTANAN 1: Tidak ada validasi tipe file yang kuat di sisi server.
    // KERENTANAN 2: Menggunakan nama file asli tanpa sanitasi yang memadai.
    $fileName = basename($file['name']); // basename() mencegah sebagian besar ../ tapi tidak semua masalah.
    $targetFilePath = $uploadDir . $fileName;

    // KERENTANAN 3: Tidak ada pemeriksaan ukuran file yang ketat di sisi server.
    // KERENTANAN 4: File disimpan di direktori yang mungkin dapat diakses web dengan ekstensi asli.

    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        $response['success'] = true;
        $response['message'] = ' File uploaded to ' . $targetFilePath . '.';
        $response['filePath'] = $targetFilePath;
        http_response_code(200);
    } else {
        $response['message'] = 'Failed to move uploaded file. PHP error code: ' . $file['error'];
        http_response_code(500);
    }
} else {
    $response['message'] = 'No file uploaded with field name "avatar".';
    http_response_code(400);
}

echo json_encode($response);
exit;
?>
