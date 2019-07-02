statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"

  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 2.0) and (credits < 120):
    return "You do not meet either requirement to graduate!"

graduation_reqs(1.0, 119)


def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."




def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  elif donation >= 500:
    print("Thank you for your donation! You have achieved gold donation status!")
  elif donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!")




def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
     return "C"
  elif gpa >= 1.0:
     return "D"
  else:
    return "F"
  return gpa
score = input("Enter your score here: ")
score = float(score)
print(grade_converter(score))

def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
  	return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and (ec_count < 3):
  	return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

print(applicant_selector(3.0, 90, 2))
