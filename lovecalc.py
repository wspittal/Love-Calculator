print("This is a calculator to see how in love two people are.\nYou input names (use first and last for better precision), and it will output the calculated love percentage.\nCaptialization does NOT matter!")
m = ""
while m != "e":
    name1 = input("First name: ")
    name2 = input("Second name: ")
    if name1.lower() == ("walker" or "walker spittal") or ("avery" or "avery lassiter") and name2.lower() == ("walker" or "walker spittal") or ("avery" or "avery lassiter") and name1.lower() != name2.lower():
      print(name1 + " and " + name2 + "'s love percentage is ∞ %!")
    else:
      nameConglomerate = [char for char in (name1 + name2).lower()]
      points = 1
      totalPoints = 78
      for i in [char for char in "abcdefghijklmnopqrstuvwxyz-0123456789 "]:
        totalPoints += nameConglomerate.count(i) * points
        points += 1
      print(name1 + " and " + name2 + "'s love percentage is " + str(totalPoints % 101) + "%!")
    m = input("Press enter to go again, or type \"e\" to end!")
