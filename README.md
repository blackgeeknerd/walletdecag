# Wallet Application
A wallet system built with django and contanerized with docker. 
This system would only be accessible to authenticated users.

[![Wallet Application](https://github.com/Resa-Obamwonyi/wallet_system/workflows/Wallet%20System/badge.svg)](https://github.com/Resa-Obamwonyi/wallet_system/actions)

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description
A wallet system for a product used in multiple countries.

### User types
#### Noob
- Can only have a wallet in a single currency selected at signup (main).
- All wallet funding in a different currency should be converted to the main currency.
- All wallet withdrawals in a different currency should be converted to the main currency before transactions are approved.
- All wallet funding has to be approved by an administrator.
- Cannot change main currency.

#### Elite
- Can have multiple wallets in different currencies with a main currency selected at signup.
- Funding in a particular currency should update the wallet with that currency or create it.
- Withdrawals in a currency with funds in the wallet of that currency should reduce the wallet balance for that currency.
- Withdrawals in a currency without a wallet balance should be converted to the main currency and withdrawn.
- Cannot change main currency

#### Admin
- Cannot have a wallet.
- Cannot withdraw funds from any wallet.
- Can fund wallets for Noob or Elite users in any currency.
- Can change the main currency of any user.
- Approves wallet funding for Noob users.
- Can promote or demote Noobs or Elite users


### How to Use and Test this Application
- Clone the Repository
- Create a .env file & fill in the values accordingly
- Run `docker-compose up --build`
- run migrations `docker-compose exec web python manage.py makemigrations`
- run `docker-compose exec web python manage.py migrate`
- run tests `docker-compose exec web python manage.py test`

#### As a User
- Using the API endpoints Make requests to register a user, add wallet, fund wallet and make withdrawals.

#### As an Admin using the hosted API
- Hit the login endpoint using the following admin credentials

```
email= seyi@test.com
password= striker
```

- Or hit the register admin endpoint to register an admin.
- Login with admin email and password
- Hit the promote user endpoint to promote a Noob to Elite.
- Hit the demote user endpoint to demote an Elite.
- Hit the approve transactions endpoint to approve withdrawal transactions for Noob users.

### Link to Heroku
- https://walletdecag.herokuapp.com
- https://walletdecag.herokuapp.com/api
- https://walletdecag.herokuapp.com/admin

## Link to API Documentation
https://documenter.getpostman.com/view/2920412/UVRGF4UE

### Comments