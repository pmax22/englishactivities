import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
T, F = "True", "False"
def TF(doc, statement, ok, tip=""):
    return C(None, ["True", "False"], fr=statement, doc=doc, c=0 if ok else 1, keep=True, tip=tip)
def Q(doc, question, opts, tip=""):
    return C(question, opts, doc=doc, tip=tip)
def W(doc, consigne, ans, tip=""):
    return G("____", ans, doc=doc, fr=consigne, tip=tip, w=240)

METH_CE = '''      <p><b>Méthode pour comprendre un texte :</b></p>
      <p>1. Lis le <b>titre</b> et regarde le type de document (lettre, article, message…).</p>
      <p>2. Fais une <b>première lecture</b> rapide : qui ? où ? quand ? quoi ?</p>
      <p>3. Repère les <b>mots transparents</b> (qui ressemblent au français) et les <b>noms propres</b>.</p>
      <p>4. Lis les questions, puis <b>relis le passage</b> utile pour chaque réponse.</p>
      <p>Pas besoin de comprendre chaque mot pour comprendre le texte !</p>'''
METH_CO = '''      <p><b>Méthode pour comprendre un document audio :</b></p>
      <p>1. Lis d'abord les <b>questions</b> : tu sauras quoi chercher.</p>
      <p>2. Première écoute : <b>qui parle ? où ? de quoi ?</b></p>
      <p>3. Deuxième écoute : concentre-toi sur les <b>détails</b> (chiffres, heures, noms, lieux).</p>
      <p>4. Tu peux réécouter autant de fois que tu veux avec 🔊. N'affiche le texte qu'en dernier recours !</p>'''

def comp(file, title, h1, sub, colors, docs, tf, qs, ws, audio, tag):
    data = {"tf": ("choice", "Vrai ou faux ?", tf), "q": ("choice", "Choisis la bonne réponse", qs)}
    ms = [M("tf", "✅", "Vrai ou faux ?", "Lis chaque affirmation et vérifie dans le document.", ["tf"], len(tf), ordered=True),
          M("q", "❓", "Questions de compréhension", "Choisis la bonne réponse.", ["q"], len(qs), ordered=True)]
    if ws:
        data["w"] = ("gap", "Trouve le mot dans le document", ws)
        ms.append(M("w", "🔍", "Trouve le mot", "Retrouve le mot anglais dans le document.", ["w"], len(ws), ordered=True))
    newpage(file, title, h1, sub, colors, METH_CO if audio else METH_CE, data, ms, tag=tag, docs=docs)

# ═════════════ CE 1 : FAMILLE (novice) ═════════════
D = "fam"
comp("ce_famille.html", "Compréhension écrite : Meet the Parkers", 'Meet the <span>Parkers</span>',
  "Compréhension écrite · une famille anglaise", ("#fde68a", "#f59e0b"),
  {D: {"title": "Meet the Parkers", "audio": False, "lines": [
    "Hi! My name is Lily Parker and I'm fourteen. I live in Bristol, in the south-west of England, with my family.",
    "My dad, Tom, is a nurse at the hospital. My mum, Sarah, works in a bakery. She gets up very early, at five o'clock!",
    "I have got a brother and a sister. My brother Jack is seventeen. He loves football and he plays every Saturday. My little sister, Amy, is six. She is very funny.",
    "We have got a dog called Biscuit. He is brown and white and he is very lazy: he sleeps all day!",
    "At the weekend, we often visit my grandparents. They live in a small village near the sea. My grandma makes delicious apple pies."]}},
  [TF(D, "Lily is fourteen.", True, "« I'm fourteen »."), TF(D, "Lily lives in London.", False, "Elle habite à Bristol."),
   TF(D, "Her dad works at the hospital.", True, "« My dad, Tom, is a nurse at the hospital »."), TF(D, "Her mum gets up late.", False, "Elle se lève à 5 heures : very early."),
   TF(D, "Jack plays football every Saturday.", True, "« he plays every Saturday »."), TF(D, "Amy is older than Lily.", False, "Amy a 6 ans : c'est la petite sœur."),
   TF(D, "Biscuit is a cat.", False, "« We have got a dog called Biscuit »."), TF(D, "The grandparents live near the sea.", True, "« a small village near the sea ».")],
  [Q(D, "What is Sarah's job?", ["She works in a bakery.", "She is a nurse.", "She is a teacher."]),
   Q(D, "How old is Jack?", ["Seventeen.", "Fourteen.", "Six."]),
   Q(D, "What is Biscuit like?", ["Brown, white and lazy.", "Black and very active.", "Small and noisy."]),
   Q(D, "What does Lily's grandma make?", ["Apple pies.", "Bread.", "Chocolate cakes."]),
   Q(D, "Where is Bristol?", ["In the south-west of England.", "In Scotland.", "Near London."])],
  [W(D, "Trouve le mot qui veut dire « paresseux ».", "lazy"), W(D, "Trouve le mot qui veut dire « boulangerie ».", "bakery"),
   W(D, "Trouve le mot qui veut dire « drôle ».", "funny"), W(D, "Trouve le mot qui veut dire « délicieux ».", "delicious")], False, "Anglais · Compréhension écrite")

# ═════════════ CE 2 : VENDEUSE (intermédiaire, CAP) ═════════════
D = "shop"
comp("ce_vendeuse.html", "Compréhension écrite : A day at the shop", 'A day at <span>the shop</span>',
  "Compréhension écrite · le quotidien d'une vendeuse", ("#99f6e4", "#14b8a6"),
  {D: {"title": "My job as a shop assistant — by Chloe, 19", "audio": False, "lines": [
    "I work in a clothes shop in the centre of Manchester. I started working there last September, after my vocational diploma in sales.",
    "My day starts at 8.45. First, I check the shelves and I tidy the clothes that customers left in the fitting rooms the day before. The shop opens at 9.30.",
    "When customers come in, I always say hello and ask if they need help. Some people know exactly what they want, but others like to get advice. Yesterday, an old man wanted a present for his granddaughter. We chose a blue scarf together and he was very happy.",
    "At lunchtime, I have a 45-minute break. I usually eat a sandwich with my colleague, Priya, in the staff room.",
    "In the afternoon, I often work at the till. I take payments by card or in cash and I give customers their receipts. Sometimes it's difficult: last week, a customer was angry because she couldn't return a dress without the receipt. I stayed calm and polite, and I called my manager.",
    "I finish at 6 pm. My feet hurt at the end of the day, but I love my job because I meet new people every day."]}},
  [TF(D, "Chloe works in a shoe shop.", False, "« a clothes shop »."), TF(D, "She started her job last September.", True, "« I started working there last September »."),
   TF(D, "The shop opens at 8.45.", False, "Chloe arrive à 8 h 45, le magasin ouvre à 9 h 30."), TF(D, "Yesterday, she helped an old man choose a present.", True, "« We chose a blue scarf together »."),
   TF(D, "Her lunch break is one hour.", False, "« a 45-minute break »."), TF(D, "Customers can pay by card or in cash.", True, "« by card or in cash »."),
   TF(D, "Chloe got angry with a customer.", False, "« I stayed calm and polite »."), TF(D, "Chloe likes her job.", True, "« I love my job »." )],
  [Q(D, "What does Chloe do first in the morning?", ["She checks the shelves and tidies the clothes.", "She opens the till.", "She has a coffee with Priya."]),
   Q(D, "What did the old man buy?", ["A blue scarf.", "A dress.", "A pair of shoes."]),
   Q(D, "Who is Priya?", ["Chloe's colleague.", "Chloe's manager.", "A customer."]),
   Q(D, "Why was a customer angry last week?", ["She couldn't return a dress without the receipt.", "The shop was closed.", "Chloe was rude to her."]),
   Q(D, "Why does Chloe love her job?", ["Because she meets new people every day.", "Because she finishes early.", "Because her feet never hurt."])],
  [W(D, "Trouve le mot qui veut dire « cabines d'essayage ».", ["fitting rooms", "fitting room"]), W(D, "Trouve le mot qui veut dire « la caisse ».", "till"),
   W(D, "Trouve le mot qui veut dire « ticket de caisse ».", ["receipt", "receipts"]), W(D, "Trouve le mot qui veut dire « collègue ».", "colleague"),
   W(D, "Trouve le mot qui veut dire « poli ».", "polite")], False, "Anglais · Compréhension écrite")

# ═════════════ CE 3 : LONDRES (avancé) ═════════════
D = "ldn"
comp("ce_londres.html", "Compréhension écrite : A weekend in London", 'A weekend in <span>London</span>',
  "Compréhension écrite · un récit au passé", ("#bfdbfe", "#3b82f6"),
  {D: {"title": "Our school trip to London", "audio": False, "lines": [
    "Last month, our class went on a three-day trip to London. We left Paris on Friday morning and took the Eurostar from Gare du Nord. The journey only took two hours and twenty minutes!",
    "When we arrived at St Pancras station, it was raining, of course. Our teacher, Mr Martin, had booked a youth hostel near the British Museum, so we walked there with our suitcases.",
    "On Saturday, we visited the Tower of London, where we saw the Crown Jewels. Then we crossed Tower Bridge and had lunch at Borough Market. I tried fish and chips for the first time: it was better than I expected. In the afternoon, we took a boat on the Thames to Westminster and saw Big Ben and the Houses of Parliament.",
    "On Sunday morning, we had some free time in Camden. I bought a T-shirt and some souvenirs for my family, but I spent too much money! We took the train home at 4 pm.",
    "It was an amazing trip. Although the weather was terrible, I would love to go back, and next time I want to visit the Natural History Museum, which we didn't have time to see."]}},
  [TF(D, "The trip lasted three days.", True, "« a three-day trip »."), TF(D, "They travelled to London by plane.", False, "Ils ont pris l'Eurostar (train)."),
   TF(D, "It was sunny when they arrived.", False, "« it was raining, of course »."), TF(D, "They stayed in a youth hostel.", True, "« a youth hostel near the British Museum »."),
   TF(D, "The narrator didn't like fish and chips.", False, "« it was better than I expected »."), TF(D, "They saw Big Ben from a boat.", True, "« we took a boat on the Thames… and saw Big Ben »."),
   TF(D, "The narrator spent very little money in Camden.", False, "« I spent too much money! »."), TF(D, "They visited the Natural History Museum.", False, "« which we didn't have time to see »." )],
  [Q(D, "How long was the journey on the Eurostar?", ["Two hours and twenty minutes.", "Three hours.", "One hour and a half."]),
   Q(D, "What did they see at the Tower of London?", ["The Crown Jewels.", "Big Ben.", "The British Museum."]),
   Q(D, "Where did they have lunch on Saturday?", ["At Borough Market.", "In Camden.", "At the youth hostel."]),
   Q(D, "What did the narrator buy in Camden?", ["A T-shirt and some souvenirs.", "A suitcase.", "Fish and chips."]),
   Q(D, "What does the narrator want to do next time?", ["Visit the Natural History Museum.", "Take the plane.", "Stay longer in Camden."])],
  [W(D, "Trouve le mot qui veut dire « le trajet, le voyage ».", "journey"), W(D, "Trouve le mot qui veut dire « valises ».", ["suitcases", "suitcase"]),
   W(D, "Trouve le mot qui veut dire « auberge de jeunesse ».", "youth hostel"), W(D, "Trouve le mot qui veut dire « bien que ».", "although")], False, "Anglais · Compréhension écrite")

# ═════════════ CO 1 : AU MAGASIN (novice / CAP) ═════════════
D = "dlg"
comp("co_magasin.html", "Compréhension orale : In a clothes shop", 'In a <span>clothes shop</span>',
  "Compréhension orale · un dialogue au magasin", ("#5eead4", "#0d9488"),
  {D: {"title": "In a clothes shop", "audio": True, "lines": [
    "Assistant: Good morning! Can I help you?",
    "Customer: Yes, please. I'm looking for a jumper for my son. It's for his birthday.",
    "Assistant: How old is he?",
    "Customer: He's twelve.",
    "Assistant: OK. We have these jumpers here. They're very popular. What colour would you like?",
    "Customer: Hmm, he likes green. Have you got this one in green?",
    "Assistant: Yes, we have. What size is he?",
    "Customer: Medium, I think.",
    "Assistant: Here you are. A medium green jumper.",
    "Customer: Great. How much is it?",
    "Assistant: It's twenty-five pounds.",
    "Customer: Perfect, I'll take it. Can I pay by card?",
    "Assistant: Of course. Would you like a gift bag?",
    "Customer: Oh yes, thank you!"]}},
  [TF(D, "The customer is looking for a jumper.", True), TF(D, "The jumper is for her daughter.", False, "C'est pour son fils (son)."),
   TF(D, "The boy is twelve.", True), TF(D, "The boy likes blue.", False, "Il aime le vert (green)."),
   TF(D, "The customer pays in cash.", False, "Elle paie par carte."), TF(D, "The assistant offers a gift bag.", True)],
  [Q(D, "Why does the customer want a jumper?", ["It's a birthday present.", "It's for Christmas.", "It's for her."]),
   Q(D, "What size does she take?", ["Medium.", "Small.", "Large."]),
   Q(D, "How much is the jumper?", ["£25.", "£15.", "£35."]),
   Q(D, "What colour is the jumper?", ["Green.", "Blue.", "Red."])], [], True, "Anglais · Compréhension orale")

# ═════════════ CO 2 : MESSAGE TÉLÉPHONIQUE (intermédiaire) ═════════════
D = "msg"
comp("co_message.html", "Compréhension orale : A phone message", 'A <span>phone message</span>',
  "Compréhension orale · un message sur répondeur", ("#c7d2fe", "#6366f1"),
  {D: {"title": "A voicemail message", "audio": True, "lines": [
    "Hello, this is a message for Mrs Thompson. My name is Daniel Carter and I'm calling from Greenwood Care Home.",
    "I'm calling about your mother, Mrs Margaret Thompson. Don't worry, she's fine. But she has a doctor's appointment next Tuesday, the fourteenth, at half past ten, and we need someone from the family to come with her.",
    "Could you call me back before Friday, please? My number is 0 1 6 1, 4 9 6, 0 2 7 3.",
    "Oh, and she asked me to tell you that she needs some new slippers, size six.",
    "Thank you very much. Have a nice day. Goodbye."]}},
  [TF(D, "The caller's name is Daniel Carter.", True), TF(D, "There is a problem with Mrs Thompson's mother.", False, "« Don't worry, she's fine »."),
   TF(D, "The appointment is on Tuesday.", True), TF(D, "Mrs Thompson must call back before Monday.", False, "« before Friday »."),
   TF(D, "Margaret needs new slippers.", True)],
  [Q(D, "Where is Daniel calling from?", ["A care home.", "A hospital.", "A shoe shop."]),
   Q(D, "What time is the appointment?", ["10:30.", "10:15.", "11:30."]),
   Q(D, "What is the date of the appointment?", ["The 14th.", "The 4th.", "The 40th."]),
   Q(D, "What is the phone number?", ["0161 496 0273", "0161 469 0237", "0116 496 0273"]),
   Q(D, "What size are the slippers?", ["Six.", "Seven.", "Sixteen."])], [], True, "Anglais · Compréhension orale")

# ═════════════ CO 3 : ANNONCES (avancé) ═════════════
comp("co_annonces.html", "Compréhension orale : Announcements", 'Station & <span>weather</span>',
  "Compréhension orale · une annonce en gare et un bulletin météo", ("#fecaca", "#ef4444"),
  {"st": {"title": "Station announcement", "audio": True, "lines": [
     "Good afternoon, ladies and gentlemen. This is an announcement for passengers travelling to Edinburgh.",
     "The fourteen fifteen train to Edinburgh is delayed by approximately twenty minutes, due to a signal problem near York.",
     "This train will now depart from platform nine, not platform four.",
     "First class passengers, please note that the café carriage is closed today. We apologise for any inconvenience."]},
   "wx": {"title": "Weather forecast", "audio": True, "lines": [
     "And now, the weather for tomorrow. In the north of England and in Scotland, it will be cold and windy, with heavy rain in the afternoon.",
     "In the south, it will be cloudy in the morning, but the sun will come out after lunch. Temperatures will reach fifteen degrees in London.",
     "And for the weekend: good news! It will be sunny and warm everywhere, so it's the perfect time for a picnic."]}},
  [TF("st", "The train is going to Edinburgh.", True), TF("st", "The train is cancelled.", False, "Il est retardé (delayed), pas annulé."),
   TF("st", "The train will leave from platform four.", False, "« platform nine, not platform four »."), TF("st", "The café carriage is closed today.", True),
   TF("wx", "It will rain in Scotland tomorrow.", True, "« heavy rain in the afternoon »."), TF("wx", "It will be sunny all day in the south.", False, "Nuageux le matin, soleil après le déjeuner."),
   TF("wx", "The weekend will be sunny.", True)],
  [Q("st", "How long is the delay?", ["About 20 minutes.", "About 15 minutes.", "About 2 hours."]),
   Q("st", "Why is the train late?", ["Because of a signal problem.", "Because of the weather.", "Because the driver is ill."]),
   Q("st", "What time was the train supposed to leave?", ["14:15", "14:50", "4:15"]),
   Q("wx", "What will the temperature be in London?", ["15 degrees.", "50 degrees.", "5 degrees."]),
   Q("wx", "What does the forecaster suggest for the weekend?", ["A picnic.", "Staying at home.", "Going skiing."])], [], True, "Anglais · Compréhension orale")
print("content11 ok", REGISTRY)
