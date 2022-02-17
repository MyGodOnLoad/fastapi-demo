import orm as orm


class User(orm.Model):
    __tablename__ = 'user'

    id = orm.Integer(primary_key=True)
    username = orm.String(max_length=50, allow_null=True, allow_blank=True)
    email = orm.String(max_length=50, unique=True, index=True)
    password = orm.String(max_length=255)
    tel = orm.String(max_length=11, min_length=11, allow_null=True, allow_blank=True)
    permission = orm.String(max_length=50, default='normal')
