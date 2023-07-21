<?php
require_once 'database.php';
require_once 'Ruangkelas.php';
$db = new MySQLDatabase();
$ruangkelas = new Ruangkelas($db);
$id=0;
$kode_ruang=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_ruang'])){
            $kode_ruang = $_GET['kode_ruang'];
        }
        if($id>0){    
            $result = $ruangkelas->get_by_id($id);
        }elseif($kode_ruang>0){
            $result = $ruangkelas->get_by_kode_ruang($kode_ruang);
        } else {
            $result = $ruangkelas->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new ruangkelas
        $ruangkelas->kode_ruang = $_POST['kode_ruang'];
        $ruangkelas->nama_ruang = $_POST['nama_ruang'];
       
        $ruangkelas->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Ruangkelas created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Ruangkelas not created.';
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
        if(isset($_GET['kode_ruang'])){
            $kode_ruang = $_GET['kode_ruang'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $ruangkelas->kode_ruang = $_PUT['kode_ruang'];
        $ruangkelas->nama_ruang = $_PUT['nama_ruang'];
        if($id>0){    
            $ruangkelas->update($id);
        }elseif($kode_ruang<>""){
            $ruangkelas->update_by_kode_ruang($kode_ruang);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Ruangkelas updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Ruangkelas update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_ruang'])){
            $kode_ruang = $_GET['kode_ruang'];
        }
        if($id>0){    
            $ruangkelas->delete($id);
        }elseif($kode_ruang>0){
            $ruangkelas->delete_by_kode_ruang($kode_ruang);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Ruangkelas deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Ruangkelas delete failed.';
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