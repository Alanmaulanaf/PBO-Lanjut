<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $NIM = "";
    public $Nama = "";
    public $Jenis_kelamin = "";
    public $Alamat = "";
    public $No_telpon = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_NIM(int $NIM)
    {
        $query = "SELECT * FROM $this->table WHERE NIM = $NIM";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`NIM`,`Nama`,`Jenis_kelamin`,`Alamat`,`No_telpon`) VALUES ('$this->NIM','$this->Nama','$this->Jenis_kelamin','$this->Alamat','$this->No_telpon')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET NIM = '$this->NIM', Nama = '$this->Nama', Jenis_kelamin = '$this->Jenis_kelamin', Alamat = '$this->Alamat', No_telpon = '$this->No_telpon' 
        WHERE Id_anggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_NIM($NIM): int
    {
        $query = "UPDATE $this->table SET NIM = '$this->NIM', Nama = '$this->Nama', Jenis_kelamin = '$this->Jenis_kelamin', Alamat = '$this->Alamat', No_telpon = '$this->No_telpon' 
        WHERE NIM = $NIM";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE Id_anggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_NIM($NIM): int
    {
        $query = "DELETE FROM $this->table WHERE NIM = $NIM";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>