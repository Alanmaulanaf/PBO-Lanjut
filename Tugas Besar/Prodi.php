<?php
//Simpanlah dengan nama file : Prodi.php
require_once 'database.php';
class Prodi 
{
    private $db;
    private $table = 'prodi';
    public $kode_prodi = "";
    public $nama_prodi = "";
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
    public function get_by_kode_prodi(int $kode_prodi)
    {
        $query = "SELECT * FROM $this->table WHERE kode_prodi = $kode_prodi";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_prodi`,`nama_prodi`) VALUES ('$this->kode_prodi','$this->nama_prodi')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_prodi = '$this->kode_prodi', nama_prodi = '$this->nama_prodi' 
        WHERE id_prodi = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_prodi($kode_prodi): int
    {
        $query = "UPDATE $this->table SET kode_prodi = '$this->kode_prodi', nama_prodi = '$this->nama_prodi' 
        WHERE kode_prodi = $kode_prodi";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_prodi = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_prodi($kode_prodi): int
    {
        $query = "DELETE FROM $this->table WHERE kode_prodi = $kode_prodi";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>