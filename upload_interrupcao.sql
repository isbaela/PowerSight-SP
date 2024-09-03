copy public.tb_interrupcao (dt_geracao, id_unidade, ds_unidade, ds_ali_sub, ds_sub_dist, num_ordem, ds_tipo, id_motivo, dt_inicio, dt_fim, ds_fator, num_nivel, num_unidade, num_consumidor, ano, ds_agente, sg_agente, num_cpf_cnpj) 
  FROM 'C:/Users/isabe/DOWNLO~1/IN0770~1.CSV'
  DELIMITER ';' CSV ENCODING 'UTF8' QUOTE '\"' ESCAPE '''';""
