import csv
import sys
import string

csv.field_size_limit(sys.maxsize)

class Trainer():
  
  def __init__(self):
    self.num_spam = 0
    self.num_ham = 0
    self.unique_words = set()
    self.total_spam_words = 0
    self.total_ham_words = 0
    self.num_emails = 0
    self.spam_words = {}
    self.ham_words = {}
  

  def clean_message(self, message):
    message = message.lower()
    message = message.translate(str.maketrans('', '', string.punctuation))
    message = message.translate(str.maketrans('', '', string.digits))
    return message.split()
  

  def tally(self, is_spam, row):
    for message in row:
        words = self.clean_message(message)
        for word in words:
            self.unique_words.add(word)
            if is_spam:
                self.total_spam_words += 1
                if self.spam_words.get(word):
                    self.spam_words[word] += 1
                else:
                    self.spam_words[word] = 1
            else:
                self.total_ham_words += 1
                if self.ham_words.get(word):
                    self.ham_words[word] += 1
                else:
                    self.ham_words[word] = 1

  def train(self):
    with open("spam_ham_dataset.csv", newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='|')
      is_spam = None
      for i, row in enumerate(reader):
        if (i == 0): #skip first row since it only contains headers
          continue

        first_val_is_integer = False
        second_val_is_ham_or_spam = False

        try:
          first_val_is_integer = int(row[0])
          first_val_is_integer = True
        except:
          pass
        try:
          if row[1] == 'ham' or row[1] == 'spam':
            second_val_is_ham_or_spam = True
        except IndexError:
          pass

        is_new_email = first_val_is_integer and second_val_is_ham_or_spam
        if is_new_email:
          self.num_emails += 1
          is_spam = row[1] == 'spam'

          if is_spam:
            self.num_spam += 1
          else:
            self.num_ham += 1

          self.tally(is_spam, row[2:])
        else:
           self.tally(is_spam, row)
    





    
    