from training import Trainer
import string
import math

data  = Trainer()
data.parse('spam_ham_dataset.csv')

PROB_SPAM_LOG = math.log(data.num_spam / data.num_emails)
PROB_HAM_LOG = math.log(data.num_ham / data.num_emails)

def clean_email(email):
  m = email.lower()
  m = m.translate(str.maketrans('', '', string.punctuation))
  m = m.translate(str.maketrans('', '', string.digits))
  return m.split()

def probablity_spam(email):
  sum = 0
  for word in email:
    sum += math.log(((data.spam_words.get(word) or 0) + 1) / (data.total_spam_words + len(data.unique_words)))
  return sum

def probablity_ham(email):
  sum = 0
  for word in email:
    sum += math.log(((data.ham_words.get(word) or 0) + 1) / (data.total_ham_words + len(data.unique_words)))
  return sum



def spam_detector(email) -> bool:
  return probablity_spam(email) > probablity_ham(email)



with open("randommail.txt", mode='r') as email_file:
  email = email_file.read()
  email = clean_email(email)
  is_spam = spam_detector(email)
  if is_spam:
    print("The email is spam")
  else:
    print("The email is not spam")