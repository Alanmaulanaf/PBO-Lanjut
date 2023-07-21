<?php
require_once 'database.php';
require_once 'Dosen.php';
$db = new MySQLDatabase();
$dosen = new Dosen($db);
$id=0;
$nidn=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nidn'])){
            $nidn = $_GET['nidn'];
        }
        if($id>0){    
            $result = $dosen->get_by_id($id);
        }elseif($nidn>0){
            $result = $dosen->get_by_nidn($nidn);
        } else {
            $result = $dosen->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new dosen
        $dosen->nidn = $_POST['nidn'];
        $dosen->nama = $_POST['nama'];
        $dosen->jk = $_POST['jk'];
       
        $dosen->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Dosen created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Dosen not created.';
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
        if(isset($_GET['nidn'])){
            $nidn = $_GET['nidn'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $dosen->nidn = $_PUT['nidn'];
        $dosen->nama = $_PUT['nama'];
        $dosen->jk = $_PUT['jk'];
        if($id>0){    
            $dosen->update($id);
        }elseif($nidn<>""){
            $dosen->update_by_nidn($nidn);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Dosen updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Dosen update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nidn'])){
            $nidn = $_GET['nidn'];
        }
        if($id>0){    
            $dosen->delete($id);
        }elseif($nidn>0){
            $dosen->delete_by_nidn($nidn);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Dosen deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Dosen delete failed.';
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