"""Helper functions for test tear down"""

from mapswipe_workers import auth


def delete_test_project(project_id: str) -> None:
    """
    Delete test project indluding groups, tasks and results
    from Firebase and Postgres
    """
    fb_db = auth.firebaseDB()
    ref = fb_db.reference("v2/results/{0}".format(project_id))
    ref.set({})
    ref = fb_db.reference("v2/tasks/{0}".format(project_id))
    ref.set({})
    ref = fb_db.reference("v2/groups/{0}".format(project_id))
    ref.set({})
    ref = fb_db.reference("v2/projects/{0}".format(project_id))
    ref.set({})
    ref = fb_db.reference("v2/projectDrafts/{0}".format(project_id))
    ref.set({})

    pg_db = auth.postgresDB()
    sql_query = "DELETE FROM results WHERE project_id = '{0}'".format(project_id)
    pg_db.query(sql_query)
    sql_query = "DELETE FROM tasks WHERE project_id = '{0}'".format(project_id)
    pg_db.query(sql_query)
    sql_query = "DELETE FROM groups WHERE project_id = '{0}'".format(project_id)
    pg_db.query(sql_query)
    sql_query = "DELETE FROM projects WHERE project_id = '{0}'".format(project_id)
    pg_db.query(sql_query)


def delete_test_user(user_id: str) -> None:
    """Delete test user from Firebase and Postgres"""

    fb_db = auth.firebaseDB()
    ref = fb_db.reference("v2/users/{0}".format(user_id))
    ref.set({})

    pg_db = auth.postgresDB()
    sql_query = "DELETE FROM users WHERE user_id = '{0}'".format(user_id)
    pg_db.query(sql_query)
