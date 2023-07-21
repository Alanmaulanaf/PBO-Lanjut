<?php
//Simpanlah dengan nama file : Jadwal.php
require_once 'database.php';
class Jadwal 
{
    private $db;
    private $table = 'jadwal';
    public $kode_jadwal = "";
    public $matakuliah = "";
    public $dosen = "";
    public $kelas = "";
    public $ruang = "";
    public $prodi = "";
    public $hari = "";
    public $jam_mulai = "";
    public $jam_selesai = "";
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
    public function get_by_kode_jadwal(int $kode_jadwal)
    {
        $query = "SELECT * FROM $this->table WHERE kode_jadwal = $kode_jadwal";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_jadwal`,`matakuliah`,`dosen`,`kelas`,`ruang`,`prodi`,`hari`,`jam_mulai`,`jam_selesai`) VALUES ('$this->kode_jadwal','$this->matakuliah','$this->dosen','$this->kelas','$this->ruang','$this->prodi','$this->hari','$this->jam_mulai','$this->jam_selesai')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_jadwal = '$this->kode_jadwal', matakuliah = '$this->matakuliah', dosen = '$this->dosen', kelas = '$this->kelas', ruang = '$this->ruang', prodi = '$this->prodi', hari = '$this->hari', jam_mulai = '$this->jam_mulai', jam_selesai = '$this->jam_selesai' 
        WHERE id_jadwal = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_jadwal($kode_jadwal): int
    {
        $query = "UPDATE $this->table SET kode_jadwal = '$this->kode_jadwal', matakuliah = '$this->matakuliah', dosen = '$this->dosen', kelas = '$this->kelas', ruang = '$this->ruang', prodi = '$this->prodi', hari = '$this->hari', jam_mulai = '$this->jam_mulai', jam_selesai = '$this->jam_selesai' 
        WHERE kode_jadwal = $kode_jadwal";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_jadwal = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_jadwal($kode_jadwal): int
    {
        $query = "DELETE FROM $this->table WHERE kode_jadwal = $kode_jadwal";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>