import os

'''
The before_feature function its executed by behave after the execution of any feature
In this example, the code clear the feature log file
'''


def before_feature(context, feature):
    directory = "logs"
    log_name = feature.filename.split("/")[-1].replace("-","_")
    ft2 = open(directory + os.sep + log_name + ".log", "w")
    ft2.close()

