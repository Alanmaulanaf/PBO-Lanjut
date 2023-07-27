CREATE TABLE `Peminjaman` (
	`Id_peminjaman` int(12) NOT NULL AUTO_INCREMENT UNIQUE,
	`NIM` char(15) NOT NULL UNIQUE,
	`Tanggal_pinjam` DATE NOT NULL,
	`Tanggal_kembali` DATE NOT NULL,
	`Id_buku` int(12) NOT NULL,
	`Id_petugas` int(12) NOT NULL,
	`Id_anggota` int(12) NOT NULL,
	PRIMARY KEY (`Id_peminjaman`)
); 

CREATE TABLE `Pengembalian` (
	`Id_pengembalian` int(12) NOT NULL AUTO_INCREMENT UNIQUE,
	`NIM` char(15) NOT NULL UNIQUE,
	`Tanggal_pengembalian` DATE NOT NULL,
	`Status` varchar(20) NOT NULL,
	`Denda` int(12) NOT NULL,
	`Id_anggota` int(12) NOT NULL,
	`Id_petugas` int(12) NOT NULL,
	`Id_buku` int(12) NOT NULL,
	PRIMARY KEY (`Id_pengembalian`)
);

CREATE TABLE `Anggota` (
	`Id_anggota` int(12) NOT NULL AUTO_INCREMENT UNIQUE,
	`NIM` char(15) NOT NULL UNIQUE,
	`Nama` varchar(30) NOT NULL,
	`Jenis_kelamin` enum ('L','P') NOT NULL DEFAULT 'L',
	`Alamat` varchar(50) NOT NULL,
	`No_telpon` char(15) NOT NULL,
	PRIMARY KEY (`Id_anggota`)
);

CREATE TABLE `Buku` (
	`Id_buku` int(12) NOT NULL AUTO_INCREMENT UNIQUE,
	`Kode_buku` char(12) NOT NULL UNIQUE,
	`Judul` varchar(30) NOT NULL,
	`Penulis` varchar(20) NOT NULL,
	`Penerbit` varchar(30) NOT NULL,
	`Tahun_terbit` char(10) NOT NULL,
	`Stok` char(10) NOT NULL,
	PRIMARY KEY (`Id_buku`)
);

CREATE TABLE `Kategori` (
	`Id_Kategori` int(12) NOT NULL AUTO_INCREMENT UNIQUE,
	`Kode_Kategori` varchar(10) NOT NULL UNIQUE,
	`Jenis` varchar(30) NOT NULL,
	`Id_buku` int(12) NOT NULL,
	PRIMARY KEY (`Id_Kategori`)
);

CREATE TABLE `Petugas` (
	`Id_petugas` int(12) NOT NULL AUTO_INCREMENT UNIQUE,
	`NIP` char(15) NOT NULL UNIQUE,
	`Nama` varchar(30) NOT NULL,
	`Jabatan` varchar(20) NOT NULL,
	`Alamat` varchar(50) NOT NULL,
	PRIMARY KEY (`Id_petugas`)
);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk0` FOREIGN KEY (`Id_buku`) REFERENCES `Buku`(`Id_buku`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk1` FOREIGN KEY (`Id_petugas`) REFERENCES `Petugas`(`Id_petugas`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk2` FOREIGN KEY (`Id_anggota`) REFERENCES `Anggota`(`Id_anggota`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk0` FOREIGN KEY (`Id_anggota`) REFERENCES `Anggota`(`Id_anggota`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk1` FOREIGN KEY (`Id_petugas`) REFERENCES `Petugas`(`Id_petugas`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk2` FOREIGN KEY (`Id_buku`) REFERENCES `Buku`(`Id_buku`);

ALTER TABLE `Kategori` ADD CONSTRAINT `Kategori_fk0` FOREIGN KEY (`Id_buku`) REFERENCES `Buku`(`Id_buku`);







