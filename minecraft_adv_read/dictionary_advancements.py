import json
import copy
copy.copy_raw_files()


#d = open('launcher_profiles.json')

#jsonObject_datas = json.load(d) #creates dictionary of values

#print(jsonObject_datas)

#print(datas)

#print(jsonObject_datas[3])
#d.close()


m = open('raw_data_file1.json')
n = open('raw_data_file2.json')

jsonObject_data = json.load(m) #creates dictionary of values
jsonObject_data2 = json.load(n)
#print(jsonObject_data)


#for keys in jsonObject_data:
#    print("Value: "  + "\tKeys: " + keys)
#print(jsonObject_data['accounts'])
#m.close()

#@variable importante
dictionary_advancements = {}

def main():
    global dictionary_advancements
    # print the keys and values
    for key in jsonObject_data:
        #value = jsonObject_data[key]['done']
        if key != 'DataVersion':
            #print("The key and completion are ({}) = ({})".format(key,jsonObject_data[key]['done']),end="\n\n")
            #print("The key and completion are ({}) = ({})".format(key, value),end="\n\n")
            dictionary_advancements[key] = jsonObject_data[key]['done']

        
    #print(jsonObject_data[key]['done'])     #this is what we need for all!!


    
    pass


    for key in jsonObject_data2:
        #value = jsonObject_data[key]['done']
        if key != 'DataVersion':
            #print("The key and completion are ({}) = ({})".format(key,jsonObject_data2[key]['done']),end="\n\n")
            #print("The key and completion are ({}) = ({})".format(key, value),end="\n\n")
            dictionary_advancements[key] = jsonObject_data2[key]['done']

        
    #print(jsonObject_data[key]['done'])     #this is what we need for all!!


    
    pass
    #print(dictionary_advancements)
if __name__ == '__main__':
    main()

m.close()
n.close()
