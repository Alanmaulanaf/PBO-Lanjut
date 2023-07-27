<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $NIM = "";
    public $Tanggal_pinjam = "";
    public $Tanggal_kembali = "";
    public $Id_buku = "";
    public $Id_petugas = "";
    public $Id_anggota = "";
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
        $query = "INSERT INTO $this->table (`NIM`,`Tanggal_pinjam`,`Tanggal_kembali`,`Id_buku`,`Id_petugas`,`Id_anggota`) VALUES ('$this->NIM','$this->Tanggal_pinjam','$this->Tanggal_kembali','$this->Id_buku','$this->Id_petugas','$this->Id_anggota')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET NIM = '$this->NIM', Tanggal_pinjam = '$this->Tanggal_pinjam', Tanggal_kembali = '$this->Tanggal_kembali', Id_buku = '$this->Id_buku', Id_petugas = '$this->Id_petugas', Id_anggota = '$this->Id_anggota' 
        WHERE Id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_NIM($NIM): int
    {
        $query = "UPDATE $this->table SET NIM = '$this->NIM', Tanggal_pinjam = '$this->Tanggal_pinjam', Tanggal_kembali = '$this->Tanggal_kembali', Id_buku = '$this->Id_buku', Id_petugas = '$this->Id_petugas', Id_anggota = '$this->Id_anggota' 
        WHERE NIM = $NIM";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE Id_peminjaman = $id";
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