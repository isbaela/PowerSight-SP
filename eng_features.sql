
	WITH processed_data AS (
    SELECT 
        ds_fator,
        LOWER(TRIM(
            REGEXP_REPLACE(
                CASE
                    WHEN ds_fator LIKE '%-%' THEN SPLIT_PART(ds_fator, '-', 4)
                    ELSE SPLIT_PART(ds_fator, ';', 4)
                END,
                ';|-', '', 'g'
            ))) as ds_falha,
        
        LOWER(TRIM(
            REGEXP_REPLACE(
                CASE
                    WHEN ds_fator LIKE '%-%' THEN SPLIT_PART(ds_fator, '-', 3)
                    ELSE SPLIT_PART(ds_fator, ';', 3)
                END,
                ';|-', '', 'g'
            ))) as tp_falha
    FROM 
        public.tb_interrupcao
    GROUP BY ds_fator
)

UPDATE public.tb_interrupcao ti
SET
    ds_falha = pd.ds_falha,
    tp_falha = pd.tp_falha
FROM
    processed_data pd
WHERE
    ti.ds_fator = pd.ds_fator;
