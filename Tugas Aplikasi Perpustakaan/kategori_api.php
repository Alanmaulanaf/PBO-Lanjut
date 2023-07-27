<?php
require_once 'database.php';
require_once 'Kategori.php';
$db = new MySQLDatabase();
$kategori = new Kategori($db);
$id=0;
$Kode_Kategori=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Kode_Kategori'])){
            $Kode_Kategori = $_GET['Kode_Kategori'];
        }
        if($id>0){    
            $result = $kategori->get_by_id($id);
        }elseif($Kode_Kategori>0){
            $result = $kategori->get_by_Kode_Kategori($Kode_Kategori);
        } else {
            $result = $kategori->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new kategori
        $kategori->Kode_Kategori = $_POST['Kode_Kategori'];
        $kategori->Jenis = $_POST['Jenis'];
        $kategori->Id_buku = $_POST['Id_buku'];
       
        $kategori->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kategori created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kategori not created.';
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
        if(isset($_GET['Kode_Kategori'])){
            $Kode_Kategori = $_GET['Kode_Kategori'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $kategori->Kode_Kategori = $_PUT['Kode_Kategori'];
        $kategori->Jenis = $_PUT['Jenis'];
        $kategori->Id_buku = $_PUT['Id_buku'];
        if($id>0){    
            $kategori->update($id);
        }elseif($Kode_Kategori<>""){
            $kategori->update_by_Kode_Kategori($Kode_Kategori);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kategori updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kategori update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Kode_Kategori'])){
            $Kode_Kategori = $_GET['Kode_Kategori'];
        }
        if($id>0){    
            $kategori->delete($id);
        }elseif($Kode_Kategori>0){
            $kategori->delete_by_Kode_Kategori($Kode_Kategori);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kategori deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kategori delete failed.';
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