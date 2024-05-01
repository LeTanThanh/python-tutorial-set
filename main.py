if __name__ == "__main__":
  # Introduction to the Python Set type

  skills = {  "Python programming", "Databases", "Software design" }
  print(skills)

  empty_set = set()
  print(empty_set)

  if not empty_set:
    print("Empty sets are falsy")

  skills = set(["Problem solving", "Critical Thinking"])
  print(skills)

  characters = set("letter")
  print(characters)

  # Getting sizes of a set

  """
  len(set)
  """

  ratings = {1, 2, 3, 4, 5}
  print(ratings)
  print(len(ratings))
