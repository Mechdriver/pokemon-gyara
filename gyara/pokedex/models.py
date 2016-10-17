from __future__ import unicode_literals

from django.db import models

class Pokemon(models.Model):
   pokemon_name = models.CharField(max_length=200)


   def __str__(self):
      return self.pokemon_name

class Type(models.Model):
   type_name = models.CharField(max_length=200)
   pokemon = models.ManyToManyField(Pokemon)
   strong_attack = models.ManyToManyField('self')
   weak_attack = models.ManyToManyField('self')
   strong_defense = models.ManyToManyField('self')
   weak_defense = models.ManyToManyField('self')
   immune_to = models.ManyToManyField('self')
   cannot_affect = models.ManyToManyField('self')

   def __str__(self):
      return self.type_name

   def getAttributes(self):

      print("Strong Attacks: ")
      if (self.strong_attack.count()):
         print(self.strong_attack.all())
      else:
         print("None")

      print("Weak Attacks: ")
      if (self.weak_attack.count()):
         print(self.weak_attack.all())
      else:
         print("None")

      print("Strong Defenses: ")
      if (self.strong_defense.count()):
         print(self.strong_defense.all())
      else:
         print("None")

      print("Weak Defenses: ")
      if (self.weak_defense.count()):
         print(self.weak_defense.all())
      else:
         print("None")

      print("Immunities: ")
      if (self.immune_to.count()):
         print(self.immune_to.all())
      else:
         print("None")

      print("Cannot Affect: ")
      if (self.cannot_affect.count()):
         print(self.cannot_affect.all())
      else:
         print("None")
