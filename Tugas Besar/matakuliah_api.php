<?php
require_once 'database.php';
require_once 'Matakuliah.php';
$db = new MySQLDatabase();
$matakuliah = new Matakuliah($db);
$id=0;
$kode_matakuliah=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_matakuliah'])){
            $kode_matakuliah = $_GET['kode_matakuliah'];
        }
        if($id>0){    
            $result = $matakuliah->get_by_id($id);
        }elseif($kode_matakuliah>0){
            $result = $matakuliah->get_by_kode_matakuliah($kode_matakuliah);
        } else {
            $result = $matakuliah->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new matakuliah
        $matakuliah->kode_matakuliah = $_POST['kode_matakuliah'];
        $matakuliah->nama_matakuliah = $_POST['nama_matakuliah'];
        $matakuliah->sks = $_POST['sks'];
       
        $matakuliah->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Matakuliah created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Matakuliah not created.';
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
        if(isset($_GET['kode_matakuliah'])){
            $kode_matakuliah = $_GET['kode_matakuliah'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $matakuliah->kode_matakuliah = $_PUT['kode_matakuliah'];
        $matakuliah->nama_matakuliah = $_PUT['nama_matakuliah'];
        $matakuliah->sks = $_PUT['sks'];
        if($id>0){    
            $matakuliah->update($id);
        }elseif($kode_matakuliah<>""){
            $matakuliah->update_by_kode_matakuliah($kode_matakuliah);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Matakuliah updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Matakuliah update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_matakuliah'])){
            $kode_matakuliah = $_GET['kode_matakuliah'];
        }
        if($id>0){    
            $matakuliah->delete($id);
        }elseif($kode_matakuliah>0){
            $matakuliah->delete_by_kode_matakuliah($kode_matakuliah);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Matakuliah deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Matakuliah delete failed.';
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