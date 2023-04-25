a=[{"question_id":4167,"question_type":"yes_or_no","question_title":"Not Applicable","answer":"1"},
{"question_id":4168,"question_type":"drop_down_single","question_title":"Question 1","answer":"2593"},
{"question_id":4169,"question_type":"rating","question_title":"Store Rating","answer":"0"}]
for valuedict in a:
    for i,j in valuedict.items():
        if(i == "question_title" ):
            if(j == "Not Applicable"):
                print(valuedict)
                final = valuedict
for i,j in final.items():
    if(i=="answer"):
        print(j)
