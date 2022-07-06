from jsonschema import validate

# A sample schema, like what we'd get from json.load()
schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    }
}
data = [{"name" : "Eggs", "price" : 34.99},{"name" : "Eggs", "price" : 34.99}]
# If no exception is raised by validate(), the instance is valid.
print(type(data[0]))
print(data[0])
validate(instance=data[0], schema=schema)

#validate(instance={"name" : "Eggs", "price" : 12}, schema=schema)