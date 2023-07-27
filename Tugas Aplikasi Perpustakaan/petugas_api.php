<?php
require_once 'database.php';
require_once 'Petugas.php';
$db = new MySQLDatabase();
$petugas = new Petugas($db);
$id=0;
$NIP=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['NIP'])){
            $NIP = $_GET['NIP'];
        }
        if($id>0){    
            $result = $petugas->get_by_id($id);
        }elseif($NIP>0){
            $result = $petugas->get_by_NIP($NIP);
        } else {
            $result = $petugas->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new petugas
        $petugas->NIP = $_POST['NIP'];
        $petugas->Nama = $_POST['Nama'];
        $petugas->Jabatan = $_POST['Jabatan'];
        $petugas->Alamat = $_POST['Alamat'];
       
        $petugas->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas not created.';
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
        if(isset($_GET['NIP'])){
            $NIP = $_GET['NIP'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $petugas->NIP = $_PUT['NIP'];
        $petugas->Nama = $_PUT['Nama'];
        $petugas->Jabatan = $_PUT['Jabatan'];
        $petugas->Alamat = $_PUT['Alamat'];
        if($id>0){    
            $petugas->update($id);
        }elseif($NIP<>""){
            $petugas->update_by_NIP($NIP);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['NIP'])){
            $NIP = $_GET['NIP'];
        }
        if($id>0){    
            $petugas->delete($id);
        }elseif($NIP>0){
            $petugas->delete_by_NIP($NIP);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas delete failed.';
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