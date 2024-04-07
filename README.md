# wb_rep

WB sync services.

## prepare package distrib
1. activate venv.
2. run: python3 setup.py bdist_wheel --bdist-dir ~/temp/bdistwheel
3. deactivate venv.

## prepare system
1. Make sure environment variables with MySQL database connection parameters are set:
  - DB_HOST
  - DB_PORT
  - DB_DATABASE
  - DB_USERNAME
  - DB_PASSWORD
2. Create database entities in MySQL database (ddls.sql).

## install package from distrib
1. mkdir project_folder.
2. cd project_folder.
3. python3 -m venv .venv.
4. source project_folder/.venv/bin/activate.
5. cd dist_folder.
6. pip install -I dist_folder/distr.whl.

## run package
1. source project_folder/.venv/bin/activate.
2. run without arguments:
	python -m wb.main.
3. run with arguments:
	python -m wb.main -s [synchronizaton service name]
