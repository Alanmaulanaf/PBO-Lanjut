<?php
require_once 'database.php';
require_once 'Kelas.php';
$db = new MySQLDatabase();
$kelas = new Kelas($db);
$id=0;
$kode_kelas=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_kelas'])){
            $kode_kelas = $_GET['kode_kelas'];
        }
        if($id>0){    
            $result = $kelas->get_by_id($id);
        }elseif($kode_kelas>0){
            $result = $kelas->get_by_kode_kelas($kode_kelas);
        } else {
            $result = $kelas->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new kelas
        $kelas->kode_kelas = $_POST['kode_kelas'];
        $kelas->nama_kelas = $_POST['nama_kelas'];
        $kelas->semester = $_POST['semester'];
       
        $kelas->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kelas created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kelas not created.';
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
        if(isset($_GET['kode_kelas'])){
            $kode_kelas = $_GET['kode_kelas'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $kelas->kode_kelas = $_PUT['kode_kelas'];
        $kelas->nama_kelas = $_PUT['nama_kelas'];
        $kelas->semester = $_PUT['semester'];
        if($id>0){    
            $kelas->update($id);
        }elseif($kode_kelas<>""){
            $kelas->update_by_kode_kelas($kode_kelas);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kelas updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kelas update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_kelas'])){
            $kode_kelas = $_GET['kode_kelas'];
        }
        if($id>0){    
            $kelas->delete($id);
        }elseif($kode_kelas>0){
            $kelas->delete_by_kode_kelas($kode_kelas);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kelas deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kelas delete failed.';
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