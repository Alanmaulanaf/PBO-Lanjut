<?php
//Simpanlah dengan nama file : Kategori.php
require_once 'database.php';
class Kategori 
{
    private $db;
    private $table = 'kategori';
    public $Kode_Kategori = "";
    public $Jenis = "";
    public $Id_buku = "";
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
    public function get_by_Kode_Kategori(int $Kode_Kategori)
    {
        $query = "SELECT * FROM $this->table WHERE Kode_Kategori = $Kode_Kategori";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`Kode_Kategori`,`Jenis`,`Id_buku`) VALUES ('$this->Kode_Kategori','$this->Jenis','$this->Id_buku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET Kode_Kategori = '$this->Kode_Kategori', Jenis = '$this->Jenis', Id_buku = '$this->Id_buku' 
        WHERE Id_Kategori = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_Kode_Kategori($Kode_Kategori): int
    {
        $query = "UPDATE $this->table SET Kode_Kategori = '$this->Kode_Kategori', Jenis = '$this->Jenis', Id_buku = '$this->Id_buku' 
        WHERE Kode_Kategori = $Kode_Kategori";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE Id_Kategori = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_Kode_Kategori($Kode_Kategori): int
    {
        $query = "DELETE FROM $this->table WHERE Kode_Kategori = $Kode_Kategori";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>