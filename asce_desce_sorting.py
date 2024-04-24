userLength = input("enter length ")
while not userLength.isdigit():
  userLength = input("enter length ")

userList = []

for i in range(int(userLength)):
  userNum = input("enter numbers ")
  while not userNum.isdigit():
    userNum = input("enter numbers ")
  userList.append(int(userNum))

userOption = input("enter 'asce' or 'desc' ")
userOptionLower = userOption.lower()
while userOptionLower != 'asce' and userOptionLower != 'desc':
  userOption = input("enter 'asce' or 'desc' ")

print(userList)

if userOptionLower == 'asce':
  for item in userList:
    for i in range(len(userList) - 1):
      if userList[i] > userList[i+1]:
        userList[i], userList[i+1] = userList[i+1], userList[i]
elif userOptionLower == 'desc':
  for item in userList:
    for i in range(len(userList) - 1):
      if userList[i] < userList[i+1]:
        userList[i], userList[i+1] = userList[i+1], userList[i]

print(userList)
