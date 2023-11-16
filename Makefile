run:
	docker-compose up -d

open:
	open http://localhost:8069

enter:
	docker exec -it odoo_web bash

get_requirements:
	docker exec odoo_web pip freeze > requirements.txt && docker cp odoo_web:/requirements.txt .

update:
	odoo --db_host=odoo_db --db_port=5432 --db_user=odoo --db_password=odoo -d odoo -u estate

download_conf:
	docker cp odoo_web:/etc/odoo/odoo.conf .
