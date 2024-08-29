shp2pgsql -I -s 4674 "C:\Users\isabe\Documents\projeto energeo\zipfolder\Linhas_de_Transmissão_-_Base_Existente.shp" tb_inf_trans > tb_inf_trans.sql
psql -U postgres -d db_fiap -f tb_inf_trans.sql
