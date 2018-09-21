#!/usr/bin/python
import yaml

myfileobj = open("/Users/pankaj/Desktop/YAML_TRAINING/training_yaml.input.txt","r")
content = myfileobj.read() #read entire file and put it into variable
print content
print(type(content))

document_dict = yaml.load(content)
print document_dict
print "type on varialble document_dict:", (type(document_dict))


document_dict['total'] = "100101001"
print (document_dict)

pyoutputfileobj = open("/Users/pankaj/Desktop/YAML_TRAINING/training_yaml.output.txt","w")

print yaml.dump(document_dict) # checking if dump is fine with old variable

pyoutputfileobj.write(yaml.dump(document_dict))

pyoutputfileobj.close()
myfileobj.close()
