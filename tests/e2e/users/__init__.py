def setup_function():
    with database as tx:
        table = tx.get_table("user", primary_id="id", primary_type=Types.string)
        table.insert_many([user.dict() for user in get_initial_users()])
