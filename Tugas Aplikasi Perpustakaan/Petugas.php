<?php
//Simpanlah dengan nama file : Petugas.php
require_once 'database.php';
class Petugas 
{
    private $db;
    private $table = 'petugas';
    public $NIP = "";
    public $Nama = "";
    public $Jabatan = "";
    public $Alamat = "";
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
    public function get_by_NIP(int $NIP)
    {
        $query = "SELECT * FROM $this->table WHERE NIP = $NIP";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`NIP`,`Nama`,`Jabatan`,`Alamat`) VALUES ('$this->NIP','$this->Nama','$this->Jabatan','$this->Alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET NIP = '$this->NIP', Nama = '$this->Nama', Jabatan = '$this->Jabatan', Alamat = '$this->Alamat' 
        WHERE Id_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_NIP($NIP): int
    {
        $query = "UPDATE $this->table SET NIP = '$this->NIP', Nama = '$this->Nama', Jabatan = '$this->Jabatan', Alamat = '$this->Alamat' 
        WHERE NIP = $NIP";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE Id_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_NIP($NIP): int
    {
        $query = "DELETE FROM $this->table WHERE NIP = $NIP";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>