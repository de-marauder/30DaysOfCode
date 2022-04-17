def email_checker():
  emails = []
  email_no = input("How many emails will you be entering? ")

  for i in range(int(email_no)):
    email = input("Enter email: ")
    emails.append(email)
  
  for email in emails:
    if ("@prof.college.edu" in email):
      print(f"{email} belongs to a professor\n")
  
    elif ("@student.college.edu" in email):
      print(f"{email} belongs to a student\n")
  
    
  return emails


print(email_checker())
