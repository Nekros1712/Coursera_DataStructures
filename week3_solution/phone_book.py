# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None for i in range(10000000)]
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query
            
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
           
        else:
            response = 'not found'
            if contacts[cur_query.number] != None:
                response = contacts[cur_query.number].name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

