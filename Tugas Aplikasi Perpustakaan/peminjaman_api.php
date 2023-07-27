<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$NIM=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['NIM'])){
            $NIM = $_GET['NIM'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($NIM>0){
            $result = $peminjaman->get_by_NIM($NIM);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->NIM = $_POST['NIM'];
        $peminjaman->Tanggal_pinjam = $_POST['Tanggal_pinjam'];
        $peminjaman->Tanggal_kembali = $_POST['Tanggal_kembali'];
        $peminjaman->Id_buku = $_POST['Id_buku'];
        $peminjaman->Id_petugas = $_POST['Id_petugas'];
        $peminjaman->Id_anggota = $_POST['Id_anggota'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['NIM'])){
            $NIM = $_GET['NIM'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->NIM = $_PUT['NIM'];
        $peminjaman->Tanggal_pinjam = $_PUT['Tanggal_pinjam'];
        $peminjaman->Tanggal_kembali = $_PUT['Tanggal_kembali'];
        $peminjaman->Id_buku = $_PUT['Id_buku'];
        $peminjaman->Id_petugas = $_PUT['Id_petugas'];
        $peminjaman->Id_anggota = $_PUT['Id_anggota'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($NIM<>""){
            $peminjaman->update_by_NIM($NIM);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['NIM'])){
            $NIM = $_GET['NIM'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($NIM>0){
            $peminjaman->delete_by_NIM($NIM);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>