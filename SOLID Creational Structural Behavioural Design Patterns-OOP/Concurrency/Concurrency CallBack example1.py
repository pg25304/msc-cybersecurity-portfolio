import time #Imports the time module, which provides time-related functions like sleep().
#Defines a function network_request that:
#Simulates a network delay by sleeping for 1 second.
#Returns a dictionary with:
#"success": True (indicating the request succeeded)
#"result": number ** 2 (the square of the input number).

def network_request(number):
    time.sleep(1.0)
    return {"success": True, "result": number ** 2}
#Defines fetch_square:
#Calls network_request(number) and stores the response.
#If "success" is True, prints the squared result.

def fetch_square(number):
    response = network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))
#The string has a placeholder {}.#
#.format(response["result"]) replaces {} with the value of response["result"].
#So if response["result"] = 9, the output becomes:
#"{} squared is {}".format(3, 9)
# Output: "3 squared is 9"

if __name__ == "__main__":
    fetch_square(2)
    fetch_square(3)
    fetch_square(4)