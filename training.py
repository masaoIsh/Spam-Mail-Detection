import csv
import sys
import string

csv.field_size_limit(sys.maxsize)

class Trainer():
  
  def __init__(self):
    self.spam = 0
    self.ham = 0
    self.unique_words = set()
    self.total_spam_words = 0
    self.total_ham_words = 0
    self.spam_words = {}
    self.ham_words = {}
  
  def parsecsv(self):
    with open('spam_ham_dataset.csv', newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for i, row in enumerate(reader):
        if i == 0:
          continue
        first_val_is_integer = False
        try:
          first_val_is_integer = int(row[0])
          first_val_is_integer = True
        except:
          pass
        second_val_is_ham_or_spam = False
        try:
          if row[1] == 'spam' or row[1] == 'ham':
            second_val_is_ham_or_spam = True
        except IndexError:
          pass

        is_new_email = first_val_is_integer and second_val_is_ham_or_spam
        if is_new_email:
          is_spam = row[1] == 'spam'
        email = self.clean_string(row[2]).split()
        for word in email:
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
  
  def clean_string(self, m):
    m = m.lower()
    # remove punctuations
    m = m.translate(str.maketrans('', '', string.punctuation))
    # remove numbers
    m = m.translate(str.maketrans('', '', string.digits))
    return m
          

trainer = Trainer()
trainer.parsecsv()

print(trainer.ham_words['subject'])
print(trainer.spam_words)



    
    