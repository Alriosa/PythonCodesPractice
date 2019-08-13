#Conditional IF with Function

def evaluation(score):
    result="Failed"
    if score > 70:
        result="Approved"
    return result

score = int(input())

print(evaluation(score)) #Con esto imprimo el Result o lo que este retornando el Evaluation.

