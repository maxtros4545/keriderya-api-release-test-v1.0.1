from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    user_uuid = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    email = fields.Str(required=True)
    role = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)