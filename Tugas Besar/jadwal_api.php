<?php
require_once 'database.php';
require_once 'Jadwal.php';
$db = new MySQLDatabase();
$jadwal = new Jadwal($db);
$id=0;
$kode_jadwal=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_jadwal'])){
            $kode_jadwal = $_GET['kode_jadwal'];
        }
        if($id>0){    
            $result = $jadwal->get_by_id($id);
        }elseif($kode_jadwal>0){
            $result = $jadwal->get_by_kode_jadwal($kode_jadwal);
        } else {
            $result = $jadwal->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new jadwal
        $jadwal->kode_jadwal = $_POST['kode_jadwal'];
        $jadwal->matakuliah = $_POST['matakuliah'];
        $jadwal->dosen = $_POST['dosen'];
        $jadwal->kelas = $_POST['kelas'];
        $jadwal->ruang = $_POST['ruang'];
        $jadwal->prodi = $_POST['prodi'];
        $jadwal->hari = $_POST['hari'];
        $jadwal->jam_mulai = $_POST['jam_mulai'];
        $jadwal->jam_selesai = $_POST['jam_selesai'];
       
        $jadwal->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Jadwal created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Jadwal not created.';
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
        if(isset($_GET['kode_jadwal'])){
            $kode_jadwal = $_GET['kode_jadwal'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $jadwal->kode_jadwal = $_PUT['kode_jadwal'];
        $jadwal->matakuliah = $_PUT['matakuliah'];
        $jadwal->dosen = $_PUT['dosen'];
        $jadwal->kelas = $_PUT['kelas'];
        $jadwal->ruang = $_PUT['ruang'];
        $jadwal->prodi = $_PUT['prodi'];
        $jadwal->hari = $_PUT['hari'];
        $jadwal->jam_mulai = $_PUT['jam_mulai'];
        $jadwal->jam_selesai = $_PUT['jam_selesai'];
        if($id>0){    
            $jadwal->update($id);
        }elseif($kode_jadwal<>""){
            $jadwal->update_by_kode_jadwal($kode_jadwal);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Jadwal updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Jadwal update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_jadwal'])){
            $kode_jadwal = $_GET['kode_jadwal'];
        }
        if($id>0){    
            $jadwal->delete($id);
        }elseif($kode_jadwal>0){
            $jadwal->delete_by_kode_jadwal($kode_jadwal);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Jadwal deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Jadwal delete failed.';
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