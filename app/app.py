import avro.io
from avro import schema
from avro.schema import SchemaFromJSONData as make_avsc_object
from avro_json_serializer import AvroJsonSerializer

# need to serialize this data
data = {"id": 1, "name": "Galdino"}

# according to this schema:
schema_dict = {
    "namespace": "example.avro",
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "id",  "type": ["int", "null"]},
        {"name": "name", "type": "string"},
        {"name": "email", "type": ["string", "null"]}
    ]
}

avro_schema = make_avsc_object(schema_dict, avro.schema.Names())

serializer = AvroJsonSerializer(avro_schema)
json_str = serializer.to_json(data)
print(json_str)
