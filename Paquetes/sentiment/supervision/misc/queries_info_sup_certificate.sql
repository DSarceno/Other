SELECT *, dbo.Traer_Tipologia(tp_supervision_certificate_status) AS supervision_certificate_status 
FROM ine_supervision_certificate AS isc
LEFT JOIN (
	SELECT 
       aur.user_id,
		au.person_id,
		CONCAT(ap.first_name, ' ', ap.middle_name, ' ', ap.last_name) AS Nombre,
		   au.nickname,
		   aur.role_id,
		   ar.name AS Puesto,
		   dbo.Traer_Tipologia(au.status) AS Estado
	FROM dbo.adm_user_role AS aur
	JOIN dbo.adm_user AS au ON aur.user_id = au.user_id
	JOIN dbo.adm_person AS ap ON au.person_id = ap.person_id
	JOIN dbo.adm_role AS ar ON aur.role_id = ar.role_id
	--WHERE au.status <> 350050
) AS people ON isc.pollster_user_id = people.user_id



SELECT * FROM ine_supervision_certificate_question_group
SELECT * FROM ine_supervision_certificate_question_group_detail
SELECT * FROM ine_supervision_certificate_question_group_detail_op