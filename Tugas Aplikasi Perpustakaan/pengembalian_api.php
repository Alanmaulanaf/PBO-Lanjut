<?php
require_once 'database.php';
require_once 'Pengembalian.php';
$db = new MySQLDatabase();
$pengembalian = new Pengembalian($db);
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
            $result = $pengembalian->get_by_id($id);
        }elseif($NIM>0){
            $result = $pengembalian->get_by_NIM($NIM);
        } else {
            $result = $pengembalian->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pengembalian
        $pengembalian->NIM = $_POST['NIM'];
        $pengembalian->Tanggal_pengembalian = $_POST['Tanggal_pengembalian'];
        $pengembalian->Status = $_POST['Status'];
        $pengembalian->Denda = $_POST['Denda'];
        $pengembalian->Id_anggota = $_POST['Id_anggota'];
        $pengembalian->Id_petugas = $_POST['Id_petugas'];
        $pengembalian->Id_buku = $_POST['Id_buku'];
       
        $pengembalian->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian not created.';
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
        $pengembalian->NIM = $_PUT['NIM'];
        $pengembalian->Tanggal_pengembalian = $_PUT['Tanggal_pengembalian'];
        $pengembalian->Status = $_PUT['Status'];
        $pengembalian->Denda = $_PUT['Denda'];
        $pengembalian->Id_anggota = $_PUT['Id_anggota'];
        $pengembalian->Id_petugas = $_PUT['Id_petugas'];
        $pengembalian->Id_buku = $_PUT['Id_buku'];
        if($id>0){    
            $pengembalian->update($id);
        }elseif($NIM<>""){
            $pengembalian->update_by_NIM($NIM);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian update failed.';
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
            $pengembalian->delete($id);
        }elseif($NIM>0){
            $pengembalian->delete_by_NIM($NIM);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian delete failed.';
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