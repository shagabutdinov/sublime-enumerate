import sublime
import sublime_plugin
import re

class Enumerate(sublime_plugin.TextCommand):
  def run(self, edit):
    sel1 = self.view.sel()[0]
    word1 = self.view.substr(self.view.word(sel1.a))

    sel2 = self.view.sel()[1]
    word2 = self.view.substr(self.view.word(sel2.a))

    try:
      number1 = int(word1)
    except:
      number1 = 1

    try:
      number2 = int(word2)
    except:
      number2 = 1

    difference = number2 - number1
    if difference == 0:
      difference = 1

    current = number1
    for sel in self.view.sel():
      if re.search(r'^\d+$', self.view.substr(self.view.word(sel.a)).strip()):
        self.view.replace(edit, self.view.word(sel.a), str(current))
      else:
        self.view.insert(edit, sel.a, str(current))

      current += difference

class Translitirate(sublime_plugin.TextCommand):
  def run(self, edit):
    for sel in self.view.sel():
      self.view.replace(edit, sel, self.translitirate(self.view.substr(sel)))

  def translitirate(self, text):
     """
     Автор: LarsKort
     Дата: 16/07/2011; 1:05 GMT-4;
     Не претендую на "хорошесть" словарика. В моем случае и такой пойдет,
     вы всегда сможете добавить свои символы и даже слова. Только
     это нужно делать в обоих списках, иначе будет ошибка.
     """
     # Слоаврь с заменами
     slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
        'ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n',
        'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
        'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
        'ю':'u','я':'ja', 'А':'a','Б':'b','В':'v','Г':'g','Д':'d','Е':'e','Ё':'e',
        'Ж':'zh','З':'z','И':'i','Й':'i','К':'k','Л':'l','М':'m','Н':'n',
        'О':'o','П':'p','Р':'r','С':'s','Т':'t','У':'u','Ф':'Х','х':'h',
        'Ц':'c','Ч':'cz','Ш':'sh','Щ':'scz','Ъ':'','Ы':'y','Ь':'','Э':'e',
        'Ю':'u','Я':'ja',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
        '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
        ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
        '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
        'Є':'e', '_': '-'}

     # Циклически заменяем все буквы в строке
     for key in slovar:
        text = text.replace(key, slovar[key])

     return text
