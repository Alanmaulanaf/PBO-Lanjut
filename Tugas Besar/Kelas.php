<?php
//Simpanlah dengan nama file : Kelas.php
require_once 'database.php';
class Kelas 
{
    private $db;
    private $table = 'kelas';
    public $kode_kelas = "";
    public $nama_kelas = "";
    public $semester = "";
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
    public function get_by_kode_kelas(int $kode_kelas)
    {
        $query = "SELECT * FROM $this->table WHERE kode_kelas = $kode_kelas";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_kelas`,`nama_kelas`,`semester`) VALUES ('$this->kode_kelas','$this->nama_kelas','$this->semester')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_kelas = '$this->kode_kelas', nama_kelas = '$this->nama_kelas', semester = '$this->semester' 
        WHERE id_kelas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_kelas($kode_kelas): int
    {
        $query = "UPDATE $this->table SET kode_kelas = '$this->kode_kelas', nama_kelas = '$this->nama_kelas', semester = '$this->semester' 
        WHERE kode_kelas = $kode_kelas";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_kelas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_kelas($kode_kelas): int
    {
        $query = "DELETE FROM $this->table WHERE kode_kelas = $kode_kelas";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>