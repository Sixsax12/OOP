try:
    all_prop = ["tracks","albumTitle","artist"]
    def update_records(record, id, prop, value):
        if int(id)<=0:
            exit()
        if id not in record and  value == '':
            exit()
        if id not in record:
            record[id] = {prop:value}
        if prop not in all_prop:
            exit()
        if value == "":
            if prop in record[id]:
                del record[id][prop]
            else:
                exit()
            return record

        if prop != "tracks":
            record[id][prop] = value
            return record

        if "tracks" not in record[id]:
            record[id]["tracks"] = []
        record[id]["tracks"].append(value)
        return record

    raw_input = input("Input : ").split(" | ")

    record_collection = eval(raw_input[0])
    id = raw_input[1]              
    prop = raw_input[2]
    value = raw_input[3]
    value = value.replace('"',"")
    value = value.replace("'","")
    result = update_records(record_collection, id, prop, value)


    print(result)
except:
    print("Invalid")
