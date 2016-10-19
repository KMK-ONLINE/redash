from redash.models import db, Dashboard 
from playhouse.migrate import PostgresqlMigrator, migrate

if __name__ == '__main__':
    migrator = PostgresqlMigrator(db.database)

    with db.database.transaction():
        migrate(
            migrator.add_column('dashboards', 'time_filters_enabled', Dashboard.time_filters_enabled),
        )
