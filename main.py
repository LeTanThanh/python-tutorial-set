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

  # Checking if an element is in a set

  """
  element in set
  """

  ratings = { 1, 2, 3, 4, 5 }
  print(ratings)

  rating = 1
  if rating in ratings:
    print(f"The set contains {rating}")

  ratings = { 1, 2, 3, 4, 5 }
  print(ratings)

  rating = 6
  if rating not in ratings:
    print(f"The set does not contains {rating}")

  # Adding elements to a set

  """
  set.add(element)
  """

  skills = { "Python programming", "Software design" }
  print(skills)

  skills.add("Problem solving")
  print(skills)

  # Removing an element from a set

  """
  set.remove(element)
  """

  skills = { "Python programming", "Software design" }
  print(skills)

  skills.remove("Software design")
  print(skills)

  skills = {  "Problem solving", "Software design", "Python programming"  }
  print(skills)

  # skills.remove("Java")
  # KeyError

  if "Java" in skills:
    skills.remove("Java")

  skills.discard("Java")
  print(skills)

  # Returning an element from a set

  skills = { "Problem solving", "Software design", "Python programming" }
  print(skills)

  skill = skills.pop()
  print(skill)
  print(skills)

  """
  set.clear()
  """

  skills = { "Problem solving", "Software design", "Python programming" }
  print(skills)

  skills.clear()
  print(skills)
