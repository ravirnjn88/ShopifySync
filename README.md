##Web App to sync shopify orders, products and customer in realtime via the webhooks

Installation Instructions
- Copy etc/config/secrets.ini.sample -> etc/config/secrets.ini and fill all the secrets in secrets.ini
- Create python virtual environment of python 3.5+ and activate it
- Install all the requirements
	` pip install -r requirements.txt`
- Run all migrations
	`python manage.py migrate`
- Create super user for login to the admin
	` python manage.py createsuperuser`
- To sync one time all the orders and products you can run following command
	`python manage.py sync_shopify_products`
	
	`python manage.py sync_shopify_orders`
	
Any product/order created thereafter will be sync automatically via the shopify webhooks. Do not forgot to resgister your webshook in shopify.