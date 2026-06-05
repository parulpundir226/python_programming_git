#input 11  player scores an ddisplay them
scores = [0] * 11 

for i in range(11):
    scores[i] = int(input("Enter score of Player " + str(i+1) + ": "))

print("\nScores of Players:")

for i in range(11):
    print("Player", i+1, ":", scores[i])
