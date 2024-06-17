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
  

  def clean_message(self, message):
    m = message.lower()
    m = m.translate(str.maketrans('', '', string.punctuation))
    m = m.translate(str.maketrans('', '', string.digits))
    return m.split()
  

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

  def parse(self, training_data):
    with open(training_data, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='|')
      currently_reading_spam = None
      for i, row in enumerate(reader):
          if (i == 0):
            continue

          first_val_is_integer = False

          try:
            first_val_is_integer = int(row[0])
            first_val_is_integer = True
          except:
            pass
          second_val_is_ham_or_spam = False
          try:
            if row[1] == 'ham' or row[1] == 'spam':
              second_val_is_ham_or_spam = True
          except IndexError:
            pass

          is_new_email = first_val_is_integer and second_val_is_ham_or_spam
          if is_new_email:
            is_spam = row[1] == 'spam'
            currently_reading_spam = True if is_spam else False

            if is_spam:
                self.spam += 1
            else:
                self.ham += 1

            self.tally(currently_reading_spam, row[2:])
          else:
              self.tally(currently_reading_spam, row)
    
     
     
     

trainer = Trainer()
trainer.parse('spam_ham_dataset.csv')

print(trainer.ham_words['subject'])
print(trainer.spam_words['subject'])
print(len(trainer.unique_words))



    
    