run:
	docker-compose up -d

open:
	open http://localhost:8069

enter:
	docker exec -it odoo_web bash

get_requirements:
	docker exec odoo_web pip freeze > requirements.txt && docker cp odoo_web:/requirements.txt .

update:
	odoo --db_host=odoo_db --db_port=5432 --db_user=odoo --db_password=odoo -d odoo -u app_contacts --stop-after-init

download_conf:
	docker cp odoo_web:/etc/odoo/odoo.conf .

create_new_module:
	odoo scaffold app_contacts /mnt/extra-addons

install:
	odoo --db_host=odoo_db --db_port=5432 --db_user=odoo --db_password=odoo -d odoo -i app_contacts --stop-after-init

logs:
	tail -f /var/log/odoo/odoo.log
