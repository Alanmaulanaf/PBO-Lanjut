<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $Kode_buku = "";
    public $Judul = "";
    public $Penulis = "";
    public $Penerbit = "";
    public $Tahun_terbit = "";
    public $Stok = "";
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
    public function get_by_Kode_buku(int $Kode_buku)
    {
        $query = "SELECT * FROM $this->table WHERE Kode_buku = $Kode_buku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`Kode_buku`,`Judul`,`Penulis`,`Penerbit`,`Tahun_terbit`,`Stok`) VALUES ('$this->Kode_buku','$this->Judul','$this->Penulis','$this->Penerbit','$this->Tahun_terbit','$this->Stok')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET Kode_buku = '$this->Kode_buku', Judul = '$this->Judul', Penulis = '$this->Penulis', Penerbit = '$this->Penerbit', Tahun_terbit = '$this->Tahun_terbit', Stok = '$this->Stok' 
        WHERE Id_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_Kode_buku($Kode_buku): int
    {
        $query = "UPDATE $this->table SET Kode_buku = '$this->Kode_buku', Judul = '$this->Judul', Penulis = '$this->Penulis', Penerbit = '$this->Penerbit', Tahun_terbit = '$this->Tahun_terbit', Stok = '$this->Stok' 
        WHERE Kode_buku = $Kode_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE Id_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_Kode_buku($Kode_buku): int
    {
        $query = "DELETE FROM $this->table WHERE Kode_buku = $Kode_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>