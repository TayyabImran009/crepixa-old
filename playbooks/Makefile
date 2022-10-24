.PHONY: edit-vault
install:
	ansible-playbook playbook.yml -i hosts.ini -l production

.PHONY: deploy
deploy:
	ansible-playbook playbook.yml -i hosts.ini -l production -t deploy,uwsgi,webserver
