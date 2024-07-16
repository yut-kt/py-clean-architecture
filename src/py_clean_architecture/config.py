from os import getenv

# Database
RDB_HOST = getenv("RDB_HOST", "py-clean-architecture-db")
RDB_USER = getenv("RDB_USER", "mysql_user")
RDB_PASSWORD = getenv("RDB_PASSWORD", "passwd")
RDB_DATABASE = getenv("RDB_DATABASE", "sample")
RDB_PORT = int(getenv("RDB_PORT", "3306"))
