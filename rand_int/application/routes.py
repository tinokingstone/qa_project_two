import random

@app.route('/rand_int', methods=['POST'])
def rand_int():
    rand_int = ""
    for i in range(4):
        rand_int += str(random.randint(0, 9))
    return {"rand_int":rand_int}

