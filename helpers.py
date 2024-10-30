from datetime import datetime

# MongoDB helper functions
def verify_index(collection):
    # Verify the indexes on the collection
    indexes = collection.index_information()

    # Print out the indexes
    for index_name, index_info in indexes.items():
        print(f"Index Name: {index_name}")
        print(f"Index Info: {index_info}")  # 'unique': true should appear


def verify_data_type(collection, field, data_type):
    items = collection.find( { field : { '$type' : data_type } } )
    count = collection.count_documents({ field: { "$type": data_type } })

    if count == 0:
        print("Nothing of that data type found")
    else:
        for item in items:
            print(item)


def convert_str_to_date(collection, field):
    for doc in collection.find( { field : { '$type' : 'string' } } ):
        # Convert string to datetime object
        date_str = doc[field]
        date_obj = datetime.strptime(date_str, '%Y-%m-%d') # Convert str to date obj

        # Update document with new date format
        collection.update_one(
            {'_id': doc['_id']},
            {'$set': {field: date_obj}}
        )
        