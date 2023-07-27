<?php
require_once 'database.php';
require_once 'Buku.php';
$db = new MySQLDatabase();
$buku = new Buku($db);
$id=0;
$Kode_buku=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Kode_buku'])){
            $Kode_buku = $_GET['Kode_buku'];
        }
        if($id>0){    
            $result = $buku->get_by_id($id);
        }elseif($Kode_buku>0){
            $result = $buku->get_by_Kode_buku($Kode_buku);
        } else {
            $result = $buku->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new buku
        $buku->Kode_buku = $_POST['Kode_buku'];
        $buku->Judul = $_POST['Judul'];
        $buku->Penulis = $_POST['Penulis'];
        $buku->Penerbit = $_POST['Penerbit'];
        $buku->Tahun_terbit = $_POST['Tahun_terbit'];
        $buku->Stok = $_POST['Stok'];
       
        $buku->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku not created.';
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
        if(isset($_GET['Kode_buku'])){
            $Kode_buku = $_GET['Kode_buku'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $buku->Kode_buku = $_PUT['Kode_buku'];
        $buku->Judul = $_PUT['Judul'];
        $buku->Penulis = $_PUT['Penulis'];
        $buku->Penerbit = $_PUT['Penerbit'];
        $buku->Tahun_terbit = $_PUT['Tahun_terbit'];
        $buku->Stok = $_PUT['Stok'];
        if($id>0){    
            $buku->update($id);
        }elseif($Kode_buku<>""){
            $buku->update_by_Kode_buku($Kode_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Kode_buku'])){
            $Kode_buku = $_GET['Kode_buku'];
        }
        if($id>0){    
            $buku->delete($id);
        }elseif($Kode_buku>0){
            $buku->delete_by_Kode_buku($Kode_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku delete failed.';
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