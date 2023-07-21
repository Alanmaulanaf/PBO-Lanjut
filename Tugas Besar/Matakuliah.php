<?php
//Simpanlah dengan nama file : Matakuliah.php
require_once 'database.php';
class Matakuliah 
{
    private $db;
    private $table = 'matakuliah';
    public $kode_matakuliah = "";
    public $nama_matakuliah = "";
    public $sks = "";
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
    public function get_by_kode_matakuliah(int $kode_matakuliah)
    {
        $query = "SELECT * FROM $this->table WHERE kode_matakuliah = $kode_matakuliah";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_matakuliah`,`nama_matakuliah`,`sks`) VALUES ('$this->kode_matakuliah','$this->nama_matakuliah','$this->sks')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_matakuliah = '$this->kode_matakuliah', nama_matakuliah = '$this->nama_matakuliah', sks = '$this->sks' 
        WHERE id_matakuliah = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_matakuliah($kode_matakuliah): int
    {
        $query = "UPDATE $this->table SET kode_matakuliah = '$this->kode_matakuliah', nama_matakuliah = '$this->nama_matakuliah', sks = '$this->sks' 
        WHERE kode_matakuliah = $kode_matakuliah";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_matakuliah = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_matakuliah($kode_matakuliah): int
    {
        $query = "DELETE FROM $this->table WHERE kode_matakuliah = $kode_matakuliah";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>