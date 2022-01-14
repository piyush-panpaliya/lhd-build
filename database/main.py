from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

print(bcolors.WARNING +"Hii this is a anime list maker"+ bcolors.ENDC)
input1=input(bcolors.BOLD+"Whats ur user token if no token the write na:"+ bcolors.ENDC)
input2=input(bcolors.BOLD+"write the list of anime seperated by coma and no space: "+ bcolors.ENDC)
data = input2.split(",")
client = FaunaClient(
  secret="<the api key comes here which i am currently hiding>",
  domain="db.eu.fauna.com",
  port=443,
  scheme="https"
)

indexes = client.query(q.if_(q.not_(q.exists(q.match(q.index("valid"), input1))),
    q.do(q.create(q.collection("user-data")["ref"],
        { 
          "data": {
            "token": q.new_id(),
            "anime": data
          }   
        }
      ),
      q.select(["data","token"],q.get(q.match(q.index("valid"), input1)))
    ),
      q.do( 
        q.update(
          q.select(["ref"],q.get(q.match(q.index("valid"), input1))),
          {
            "data":{
              "anime":q.append(q.select(["data","anime"],q.get(q.match(q.index("valid"), input1))),data)
            }
          }
        )
)))

print(indexes)
