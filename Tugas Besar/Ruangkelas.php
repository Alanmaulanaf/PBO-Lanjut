<?php
//Simpanlah dengan nama file : Ruangkelas.php
require_once 'database.php';
class Ruangkelas 
{
    private $db;
    private $table = 'ruangkelas';
    public $kode_ruang = "";
    public $nama_ruang = "";
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
    public function get_by_kode_ruang(int $kode_ruang)
    {
        $query = "SELECT * FROM $this->table WHERE kode_ruang = $kode_ruang";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_ruang`,`nama_ruang`) VALUES ('$this->kode_ruang','$this->nama_ruang')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_ruang = '$this->kode_ruang', nama_ruang = '$this->nama_ruang' 
        WHERE id_ruang = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_ruang($kode_ruang): int
    {
        $query = "UPDATE $this->table SET kode_ruang = '$this->kode_ruang', nama_ruang = '$this->nama_ruang' 
        WHERE kode_ruang = $kode_ruang";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_ruang = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_ruang($kode_ruang): int
    {
        $query = "DELETE FROM $this->table WHERE kode_ruang = $kode_ruang";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>