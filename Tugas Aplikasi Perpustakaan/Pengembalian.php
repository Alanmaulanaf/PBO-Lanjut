<?php
//Simpanlah dengan nama file : Pengembalian.php
require_once 'database.php';
class Pengembalian 
{
    private $db;
    private $table = 'pengembalian';
    public $NIM = "";
    public $Tanggal_pengembalian = "";
    public $Status = "";
    public $Denda = "";
    public $Id_anggota = "";
    public $Id_petugas = "";
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
    public function get_by_NIM(int $NIM)
    {
        $query = "SELECT * FROM $this->table WHERE NIM = $NIM";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`NIM`,`Tanggal_pengembalian`,`Status`,`Denda`,`Id_anggota`,`Id_petugas`,`Id_buku`) VALUES ('$this->NIM','$this->Tanggal_pengembalian','$this->Status','$this->Denda','$this->Id_anggota','$this->Id_petugas','$this->Id_buku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET NIM = '$this->NIM', Tanggal_pengembalian = '$this->Tanggal_pengembalian', Status = '$this->Status', Denda = '$this->Denda', Id_anggota = '$this->Id_anggota', Id_petugas = '$this->Id_petugas', Id_buku = '$this->Id_buku' 
        WHERE Id_pengembalian = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_NIM($NIM): int
    {
        $query = "UPDATE $this->table SET NIM = '$this->NIM', Tanggal_pengembalian = '$this->Tanggal_pengembalian', Status = '$this->Status', Denda = '$this->Denda', Id_anggota = '$this->Id_anggota', Id_petugas = '$this->Id_petugas', Id_buku = '$this->Id_buku' 
        WHERE NIM = $NIM";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE Id_pengembalian = $id";
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