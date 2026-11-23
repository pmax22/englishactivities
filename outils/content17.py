import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content11.py", encoding="utf-8").read().split("# ═════════════ CE 1")[0])
CE, CO = "Anglais · Compréhension écrite", "Anglais · Compréhension orale"

# ═════════════ CE 4 : SCHOOL DAY (novice) ═════════════
D = "school"
comp("ce_ecole.html", "Compréhension écrite : A school day in England", 'A school day <span>in England</span>',
  "Compréhension écrite · la journée d'un collégien anglais", ("#fecaca", "#ef4444"),
  {D: {"title": "My school day — by Oliver, 13", "audio": False, "lines": [
    "Hello! I'm Oliver and I go to Hillside School in Leeds, in the north of England.",
    "I get up at seven o'clock. I have breakfast with my mum: cereal and orange juice. Then I take the bus to school with my best friend, Sam.",
    "At my school, we wear a uniform: black trousers, a white shirt, a blue jumper and a tie. I don't like the tie!",
    "Lessons start at 8.50. We have five lessons a day. My favourite subject is science because the teacher is great. I don't like maths very much: it's difficult for me.",
    "At lunchtime, I eat in the canteen. On Fridays, there is fish and chips. After lunch, I play football with my friends in the playground.",
    "School finishes at 3.20. On Tuesdays, I stay for the drama club. In the evening, I do my homework and I watch TV."]}},
  [TF(D, "Oliver lives in Leeds.", True, "« Hillside School in Leeds »."), TF(D, "He goes to school by car.", False, "« I take the bus to school »."),
   TF(D, "Students wear a uniform at his school.", True, "« we wear a uniform »."), TF(D, "Oliver likes his tie.", False, "« I don't like the tie! »"),
   TF(D, "Lessons start at 8.50.", True, "« Lessons start at 8.50 »."), TF(D, "His favourite subject is maths.", False, "C'est science ; maths is difficult for him."),
   TF(D, "There is fish and chips on Fridays.", True, "« On Fridays, there is fish and chips »."), TF(D, "He goes to the drama club on Tuesdays.", True, "« On Tuesdays, I stay for the drama club »." )],
  [Q(D, "What does Oliver have for breakfast?", ["Cereal and orange juice.", "Toast and tea.", "Eggs and bacon."]),
   Q(D, "Who is Sam?", ["His best friend.", "His brother.", "His science teacher."]),
   Q(D, "Why does he like science?", ["Because the teacher is great.", "Because it's easy.", "Because there is no homework."]),
   Q(D, "What does he do after lunch?", ["He plays football in the playground.", "He goes home.", "He does his homework."]),
   Q(D, "What time does school finish?", ["At 3.20.", "At 8.50.", "At 5 o'clock."])],
  [W(D, "Trouve le mot qui veut dire « cantine ».", "canteen"), W(D, "Trouve le mot qui veut dire « cour de récréation ».", "playground"),
   W(D, "Trouve le mot qui veut dire « matière (scolaire) ».", "subject"), W(D, "Trouve le mot qui veut dire « pull ».", "jumper"),
   W(D, "Trouve le mot qui veut dire « devoirs ».", "homework")], False, CE)

# ═════════════ CE 5 : PEN FRIEND EMAIL (intermédiaire) ═════════════
D = "mail"
comp("ce_email.html", "Compréhension écrite : An email from Emma", 'An email <span>from Emma</span>',
  "Compréhension écrite · le mail d'une correspondante", ("#c4b5fd", "#8b5cf6"),
  {D: {"title": "From: emma.wilson@mail.co.uk — Subject: My summer holidays!", "audio": False, "lines": [
    "Hi Léa,",
    "Thanks for your last email and for the photos of your village. It looks so pretty!",
    "I'm back home in Brighton after an amazing holiday in Scotland. We stayed in a small cottage near Loch Ness for two weeks. We didn't see the monster, of course, but my little brother looked for it every morning!",
    "The weather wasn't great: it rained almost every day. But we visited Edinburgh Castle, we went hiking in the mountains and I tried haggis for the first time. I didn't like it very much…",
    "Next month, I'm starting a new school. I'm a bit nervous because I don't know anyone there. Have you ever changed schools? How did you feel?",
    "Guess what? My parents have said yes: I can visit you in France next spring! I'm going to take the Eurostar to Paris and then a train to your town. I can't wait to practise my French with you.",
    "Write back soon and tell me about your holidays!",
    "Love, Emma"]}},
  [TF(D, "Emma lives in Brighton.", True, "« I'm back home in Brighton »."), TF(D, "She spent two weeks in Scotland.", True, "« for two weeks »."),
   TF(D, "They saw the Loch Ness monster.", False, "« We didn't see the monster »."), TF(D, "The weather was sunny.", False, "« it rained almost every day »."),
   TF(D, "Emma loved haggis.", False, "« I didn't like it very much »."), TF(D, "She is starting a new school next month.", True, "« Next month, I'm starting a new school »."),
   TF(D, "Emma is going to visit Léa next summer.", False, "« next spring » : au printemps."), TF(D, "She is going to travel by plane.", False, "Eurostar puis train.")],
  [Q(D, "Why is Emma writing to Léa?", ["To answer her email and tell her about her holidays.", "To invite her to Scotland.", "To say she can't visit France."]),
   Q(D, "What did her little brother do every morning?", ["He looked for the monster.", "He went hiking.", "He visited the castle."]),
   Q(D, "How does Emma feel about her new school?", ["A bit nervous.", "Very angry.", "Bored."]),
   Q(D, "Why is she nervous?", ["Because she doesn't know anyone there.", "Because the school is far.", "Because she doesn't like her teachers."]),
   Q(D, "What does Emma want to do in France?", ["Practise her French.", "Learn to cook.", "Visit Scotland."]),
   Q(D, "What does Emma ask Léa?", ["If she has ever changed schools.", "If she likes haggis.", "If she can come to Brighton."])],
  [W(D, "Trouve le mot qui veut dire « incroyable, génial ».", "amazing"), W(D, "Trouve le mot qui veut dire « une petite maison de campagne ».", "cottage"),
   W(D, "Trouve l'expression qui veut dire « j'ai hâte ».", ["i can't wait", "can't wait", "i cannot wait"]), W(D, "Trouve le mot qui veut dire « inquiète, nerveuse ».", "nervous"),
   W(D, "Trouve le mot qui veut dire « presque ».", "almost")], False, CE)

# ═════════════ CE 6 : SOCIAL MEDIA (avancé) ═════════════
D = "social"
comp("ce_reseaux.html", "Compréhension écrite : Teens and social media", 'Teens and <span>social media</span>',
  "Compréhension écrite · un article de presse", ("#a5f3fc", "#06b6d4"),
  {D: {"title": "Can teenagers live without their phones? — The Daily Echo", "audio": False, "lines": [
    "Last month, a secondary school in Bristol asked 200 pupils to take part in an unusual experiment: one week without social media.",
    "At first, many students were worried. \"I thought I would miss everything,\" admits Maya, 15. \"My friends post all the time, and I was afraid of being left out.\"",
    "However, after only three days, most pupils noticed positive changes. They said they were sleeping better and that they had more time for hobbies, sport and family. Some of them even started reading books again.",
    "According to a recent survey, British teenagers spend an average of four hours a day on their phones. Doctors warn that too much screen time can lead to stress, poor concentration and a lack of sleep.",
    "Not everyone agrees, though. \"Social media isn't the problem,\" says Mr Hughes, a computer science teacher. \"It helps young people stay in touch and learn new things. What matters is how you use it.\"",
    "At the end of the week, 60% of the pupils said they would try to reduce their screen time. Maya has decided to switch off her phone after 9 pm. \"I feel less tired,\" she says, \"and I actually talk to my parents at dinner now!\""]}},
  [TF(D, "The experiment lasted one month.", False, "Une semaine : « one week without social media »."), TF(D, "At first, Maya was afraid of missing things.", True, "« I thought I would miss everything »."),
   TF(D, "Most pupils noticed positive changes after three days.", True, "« after only three days, most pupils noticed positive changes »."),
   TF(D, "British teenagers spend about two hours a day on their phones.", False, "« an average of four hours a day »."),
   TF(D, "Mr Hughes thinks social media is the main problem.", False, "« Social media isn't the problem »."),
   TF(D, "All the pupils decided to stop using social media.", False, "60 % essaieront de réduire, pas d'arrêter."),
   TF(D, "Maya now switches off her phone in the evening.", True, "« after 9 pm »." )],
  [Q(D, "What is the main idea of the article?", ["A school tested a week without social media, with mostly positive results.", "Doctors want to ban phones at school.", "Teenagers don't use social media any more."]),
   Q(D, "What positive changes did pupils notice?", ["Better sleep and more time for hobbies and family.", "Better marks in every subject.", "More friends online."]),
   Q(D, "According to doctors, too much screen time can cause…", ["stress, poor concentration and a lack of sleep.", "better memory.", "more sport."]),
   Q(D, "What is Mr Hughes's opinion?", ["What matters is how you use social media.", "Phones should be banned.", "Teenagers should never go online."]),
   Q(D, "What is the tone of the end of the article?", ["Optimistic.", "Angry.", "Sad."])],
  [W(D, "Trouve l'expression qui veut dire « mis à l'écart ».", ["left out", "being left out"]), W(D, "Trouve le mot qui veut dire « une enquête, un sondage ».", "survey"),
   W(D, "Trouve le connecteur qui veut dire « cependant ».", "however"), W(D, "Trouve l'expression qui veut dire « rester en contact ».", "stay in touch"),
   W(D, "Trouve le verbe qui veut dire « éteindre ».", ["switch off", "to switch off"])], False, CE)

# ═════════════ CO 4 : AT THE CAFÉ (novice) ═════════════
D = "cafe"
comp("co_cafe.html", "Compréhension orale : At the café", 'At <span>the café</span>',
  "Compréhension orale · commander à boire et à manger", ("#fcd34d", "#d97706"),
  {D: {"title": "At the café", "audio": True, "lines": [
    "Waiter: Good morning! What can I get you?",
    "Lucy: Hello. Can I have a hot chocolate, please?",
    "Waiter: Of course. Small or large?",
    "Lucy: Large, please. And a cheese sandwich.",
    "Waiter: Sorry, we haven't got any cheese sandwiches left. We've got ham or chicken.",
    "Lucy: OK, a chicken sandwich, then.",
    "Waiter: Anything else?",
    "Lucy: Yes, a chocolate muffin for my brother.",
    "Waiter: Is it to eat in or to take away?",
    "Lucy: To take away, please. How much is it?",
    "Waiter: That's eight pounds fifty, please.",
    "Lucy: Here you are. Thank you!",
    "Waiter: Thank you. Have a nice day!"]}},
  [TF(D, "Lucy orders a hot chocolate.", True, "« Can I have a hot chocolate, please? »"), TF(D, "She wants a small drink.", False, "« Large, please »."),
   TF(D, "There are no more cheese sandwiches.", True, "« we haven't got any cheese sandwiches left »."), TF(D, "She takes a ham sandwich.", False, "« a chicken sandwich, then »."),
   TF(D, "The muffin is for her brother.", True, "« for my brother »."), TF(D, "Lucy eats in the café.", False, "« To take away »." )],
  [Q(D, "What sandwiches have they got?", ["Ham or chicken.", "Cheese or tuna.", "Egg or chicken."]),
   Q(D, "What kind of muffin does she order?", ["Chocolate.", "Blueberry.", "Banana."]),
   Q(D, "How much does Lucy pay?", ["£8.50", "£5.80", "£18.50"], "« eight pounds fifty »."),
   Q(D, "What does the waiter say at the end?", ["Have a nice day!", "See you tomorrow!", "Good night!"])],
  [W(D, "Comment dit-on « à emporter » ?", ["to take away", "take away"]), W(D, "Comment Lucy demande-t-elle le prix ? (3 mots + ?)", ["how much is it", "how much is it?"]),
   W(D, "Que dit-on en tendant l'argent ? (« Voilà »)", ["here you are", "here you are."])], True, CO)

# ═════════════ CO 5 : DIRECTIONS (intermédiaire) ═════════════
D = "dir"
comp("co_directions.html", "Compréhension orale : Excuse me, where is…?", 'Excuse me, <span>where is…?</span>',
  "Compréhension orale · demander son chemin", ("#86efac", "#16a34a"),
  {D: {"title": "Asking for directions in York", "audio": True, "lines": [
    "Tourist: Excuse me, could you help me? I'm looking for the train station.",
    "Woman: Yes, of course. It's not far. Go straight on along this street until you get to the traffic lights.",
    "Tourist: Straight on to the traffic lights. OK.",
    "Woman: Then turn left into Station Road. Walk past the post office and the cinema. The station is on your right, opposite a big hotel.",
    "Tourist: So, left at the traffic lights, past the post office and the cinema, and it's on the right.",
    "Woman: That's it. It takes about ten minutes on foot.",
    "Tourist: Great. And is there a cash machine near the station?",
    "Woman: Yes, there's one next to the cinema.",
    "Tourist: Thank you so much!",
    "Woman: You're welcome. Have a good trip!"]}},
  [TF(D, "The tourist is looking for the bus station.", False, "« the train station »."), TF(D, "The station is far away.", False, "« It's not far »."),
   TF(D, "First, the tourist must go straight on.", True, "« Go straight on along this street »."), TF(D, "At the traffic lights, he must turn right.", False, "« turn left into Station Road »."),
   TF(D, "The station is opposite a big hotel.", True, "« opposite a big hotel »."), TF(D, "There is a cash machine next to the cinema.", True, "« there's one next to the cinema »." )],
  [Q(D, "What is the name of the street after the traffic lights?", ["Station Road.", "High Street.", "Park Lane."]),
   Q(D, "What does the tourist walk past?", ["The post office and the cinema.", "The bank and the museum.", "The school and the park."]),
   Q(D, "How long does it take on foot?", ["About ten minutes.", "About two minutes.", "About half an hour."]),
   Q(D, "Where is the station?", ["On the right.", "On the left.", "Behind the cinema."])],
  [W(D, "Comment dit-on « tout droit » ?", ["straight on", "go straight on"]), W(D, "Comment dit-on « les feux » ?", ["the traffic lights", "traffic lights"]),
   W(D, "Comment dit-on « en face de » ?", "opposite"), W(D, "Comment dit-on « distributeur de billets » ?", ["cash machine", "a cash machine"])], True, CO)

# ═════════════ CO 6 : JOB INTERVIEW (avancé, CAP) ═════════════
D = "job"
comp("co_entretien.html", "Compréhension orale : A job interview", 'A job <span>interview</span>',
  "Compréhension orale · un entretien pour un job d'été", ("#f9a8d4", "#db2777"),
  {D: {"title": "A job interview at Green's Supermarket", "audio": True, "lines": [
    "Manager: Good afternoon, Ben. Please sit down. Thank you for coming.",
    "Ben: Good afternoon. Thank you for inviting me.",
    "Manager: So, you've applied for the summer job as a sales assistant. Why do you want to work here?",
    "Ben: Well, I'm studying sales at a vocational school, and I'd like to get some real experience. I also shop here with my family, so I know the store well.",
    "Manager: Have you ever worked in a shop before?",
    "Ben: Yes, I did a six-week work placement in a sports shop last year. I served customers, I worked at the till and I put products on the shelves.",
    "Manager: Very good. What are your main qualities?",
    "Ben: I'm punctual, I'm friendly and I like working in a team. I'm also good at staying calm when it's busy.",
    "Manager: The job is from July to August, thirty hours a week, and you sometimes have to work on Saturdays. Is that a problem?",
    "Ben: No, not at all. I'm available all summer.",
    "Manager: Perfect. Do you have any questions?",
    "Ben: Yes, will I have training at the beginning?",
    "Manager: Yes, you'll spend your first two days with an experienced colleague. We'll call you by Friday. Thank you, Ben.",
    "Ben: Thank you very much. Goodbye."]}},
  [TF(D, "Ben is applying for a job as a sales assistant.", True, "« the summer job as a sales assistant »."),
   TF(D, "He has never worked in a shop.", False, "Il a fait un stage de 6 semaines dans un magasin de sport."),
   TF(D, "He did his work placement in a supermarket.", False, "« in a sports shop »."),
   TF(D, "Ben says he likes working in a team.", True, "« I like working in a team »."),
   TF(D, "He can't work on Saturdays.", False, "« No, not at all. I'm available all summer »."),
   TF(D, "The manager will call him by Friday.", True, "« We'll call you by Friday »." )],
  [Q(D, "Why does Ben want this job?", ["To get real experience in sales.", "Because he needs a car.", "Because his friend works there."]),
   Q(D, "What did he do during his work placement?", ["He served customers, worked at the till and filled the shelves.", "He cleaned the warehouse.", "He made deliveries."]),
   Q(D, "How many hours a week is the job?", ["Thirty.", "Thirteen.", "Forty."]),
   Q(D, "When is the job?", ["From July to August.", "From June to September.", "Only in August."]),
   Q(D, "What question does Ben ask?", ["If he will have training.", "How much he will earn.", "If he can work at night."])],
  [W(D, "Comment dit-on « stage (en entreprise) » ?", ["work placement", "a work placement", "placement"]), W(D, "Comment dit-on « ponctuel » ?", "punctual"),
   W(D, "Comment dit-on « disponible » ?", "available"), W(D, "Comment dit-on « formation » ?", "training")], True, CO)

print("ok", REGISTRY)
