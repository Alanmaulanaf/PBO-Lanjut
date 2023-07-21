<?php
require_once 'database.php';
require_once 'Prodi.php';
$db = new MySQLDatabase();
$prodi = new Prodi($db);
$id=0;
$kode_prodi=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_prodi'])){
            $kode_prodi = $_GET['kode_prodi'];
        }
        if($id>0){    
            $result = $prodi->get_by_id($id);
        }elseif($kode_prodi>0){
            $result = $prodi->get_by_kode_prodi($kode_prodi);
        } else {
            $result = $prodi->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new prodi
        $prodi->kode_prodi = $_POST['kode_prodi'];
        $prodi->nama_prodi = $_POST['nama_prodi'];
       
        $prodi->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Prodi created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Prodi not created.';
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
        if(isset($_GET['kode_prodi'])){
            $kode_prodi = $_GET['kode_prodi'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $prodi->kode_prodi = $_PUT['kode_prodi'];
        $prodi->nama_prodi = $_PUT['nama_prodi'];
        if($id>0){    
            $prodi->update($id);
        }elseif($kode_prodi<>""){
            $prodi->update_by_kode_prodi($kode_prodi);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Prodi updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Prodi update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_prodi'])){
            $kode_prodi = $_GET['kode_prodi'];
        }
        if($id>0){    
            $prodi->delete($id);
        }elseif($kode_prodi>0){
            $prodi->delete_by_kode_prodi($kode_prodi);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Prodi deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Prodi delete failed.';
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