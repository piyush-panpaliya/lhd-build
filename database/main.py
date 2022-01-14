from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(
  secret="fnAEc5nb2IAAxaG4ubeJK-tuGt7Avqhzg49KW3cR",
  domain="db.eu.fauna.com",
  # NOTE: Use the correct domain for your database's Region Group.
  port=443,
  scheme="https"
)

indexes = client.query(q.paginate(q.indexes()))

print(indexes)