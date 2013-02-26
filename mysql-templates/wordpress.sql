create database '{{ domain_list[0]|replace('.','_') }}';
create user '{{ domain_list[0]|replace('.','_') }}'@'localhost' identified by '{{mysql_password[0]}}';
grant usage on *.* to '{{ domain_list[0]|replace('.','_')  }}'@'localhost' identified by '{{mysql_password[0]}}';
grant all privileges on '{{ domain_list[0]|replace('.','_')  }}'.* to '{{domain_list[0]|replace('.','_') }}'@'localhost';
