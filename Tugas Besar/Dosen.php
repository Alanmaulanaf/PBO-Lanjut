<?php
//Simpanlah dengan nama file : Dosen.php
require_once 'database.php';
class Dosen 
{
    private $db;
    private $table = 'dosen';
    public $nidn = "";
    public $nama = "";
    public $jk = "";
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
    public function get_by_nidn(int $nidn)
    {
        $query = "SELECT * FROM $this->table WHERE nidn = $nidn";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nidn`,`nama`,`jk`) VALUES ('$this->nidn','$this->nama','$this->jk')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nidn = '$this->nidn', nama = '$this->nama', jk = '$this->jk' 
        WHERE id_dosen = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nidn($nidn): int
    {
        $query = "UPDATE $this->table SET nidn = '$this->nidn', nama = '$this->nama', jk = '$this->jk' 
        WHERE nidn = $nidn";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_dosen = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nidn($nidn): int
    {
        $query = "DELETE FROM $this->table WHERE nidn = $nidn";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>