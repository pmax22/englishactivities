import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
SOC, PRA = "Anglais · Sociolinguistique", "Anglais · Pragmatique"
FO, IN = "Formal", "Informal"

# ════════════════════ SOCIOLINGUISTIQUE ════════════════════
LES = '''      <p>On ne parle pas de la même façon à un ami et à un directeur. C'est le <b>registre</b> : <span class="hl">informal</span> (familier) ou <span class="hl">formal</span> (soutenu, poli).</p>
      <p><b>Informel :</b> contractions (<i>I'm, don't</i>), mots courts (<i>get, buy, help</i>), impératif direct, <i>Hi! / Cheers! / See you!</i></p>
      <p><b>Formel :</b> formes complètes (<i>I am, do not</i>), mots d'origine latine (<i>obtain, purchase, assist</i>), questions indirectes (<i>Could you…? Would you mind…? I was wondering if…</i>).</p>
      <p><b>Email formel :</b> <i>Dear Sir or Madam, … Yours faithfully</i> (destinataire inconnu) · <i>Dear Mr Smith, … Yours sincerely</i> (nom connu) · <i>Kind regards</i> (neutre).</p>
      <p><b>Plus c'est indirect, plus c'est poli :</b> <i>Open the window.</i> → <i>Can you open the window?</i> → <i>Could you open the window, please?</i> → <i>Would you mind opening the window?</i></p>'''
R1 = [C("Hi Tom! How's it going?", [IN, FO], keep=True, tip="Hi + How's it going ? = entre amis."),
      C("Dear Sir or Madam, I am writing to enquire about the position.", [FO, IN], keep=True, tip="Dear Sir or Madam, I am writing to…"),
      C("Gimme a sec!", [IN, FO], keep=True, tip="gimme = give me, très familier."),
      C("I would be grateful if you could send me further information.", [FO, IN], keep=True, tip="I would be grateful if… = très poli."),
      C("Cheers, mate!", [IN, FO], keep=True, tip="Cheers, mate = merci / salut, l'ami."),
      C("We regret to inform you that the event has been cancelled.", [FO, IN], keep=True, tip="We regret to inform you… = annonce officielle."),
      C("Wanna come to the party?", [IN, FO], keep=True, tip="wanna = want to."),
      C("Should you require any assistance, please do not hesitate to contact us.", [FO, IN], keep=True, tip="Should you require… = tournure très soutenue."),
      C("No worries, see you later!", [IN, FO], keep=True), C("Please find attached my CV.", [FO, IN], keep=True, tip="Formule d'email professionnel.")]
R2 = [C("informal: get → formal:", ["obtain", "take", "grab"], fr="Choisis l'équivalent formel."), C("informal: buy → formal:", ["purchase", "pay", "shop"], fr="Choisis l'équivalent formel."),
      C("informal: help → formal:", ["assist", "save", "hand"], fr="Choisis l'équivalent formel."), C("informal: ask for → formal:", ["request", "tell", "beg"], fr="Choisis l'équivalent formel."),
      C("informal: need → formal:", ["require", "want", "must"], fr="Choisis l'équivalent formel."), C("informal: start → formal:", ["commence", "go", "open up"], fr="Choisis l'équivalent formel."),
      C("informal: tell → formal:", ["inform", "chat", "speak"], fr="Choisis l'équivalent formel."), C("informal: kids → formal:", ["children", "guys", "teens"], fr="Choisis l'équivalent formel."),
      C("informal: Thanks a lot! → formal:", ["Thank you very much indeed.", "Cheers!", "Ta!"], fr="Choisis l'équivalent formel."),
      C("informal: Sorry! → formal:", ["Please accept my apologies.", "My bad!", "Oops!"], fr="Choisis l'équivalent formel.")]
R3 = [C(None, ["Could you tell me where the station is, please?", "Where's the station?", "Tell me where the station is."], fr="Tu demandes ton chemin à un inconnu. Quelle phrase est la plus polie ?"),
      C(None, ["Would you mind closing the door?", "Close the door!", "Door!"], fr="Tu demandes à ton professeur de fermer la porte."),
      C(None, ["Dear Mr Brown,", "Hey Brown!", "Yo Mr Brown,"], fr="Début d'un email à un futur employeur dont tu connais le nom."),
      C(None, ["Yours sincerely,", "Love,", "See ya,"], fr="Fin d'un email qui commence par « Dear Mr Brown ».", tip="Nom connu → Yours sincerely."),
      C(None, ["Yours faithfully,", "Yours sincerely,", "Bye,"], fr="Fin d'un email qui commence par « Dear Sir or Madam ».", tip="Destinataire inconnu → Yours faithfully."),
      C(None, ["I was wondering if I could leave early today.", "I'm leaving early today.", "Let me go early."], fr="Tu demandes à ton tuteur de stage de partir plus tôt."),
      C(None, ["Excuse me, I think there may be a mistake on the bill.", "Your bill is wrong!", "Hey, mistake here."], fr="Au restaurant, tu signales poliment une erreur sur l'addition."),
      C(None, ["Good afternoon, how may I help you?", "What do you want?", "Yeah?"], fr="Tu es vendeur / vendeuse et un client entre."),
      C(None, ["I'm afraid we don't have that size.", "No, we haven't got it.", "Nope."], fr="Tu annonces poliment au client que la taille n'est pas disponible.", tip="I'm afraid… adoucit une mauvaise nouvelle."),
      C(None, ["Hi Sam, thanks for your message!", "Dear Sir, I acknowledge receipt of your message.", "To whom it may concern,"], fr="Tu réponds au message d'un ami.")]
newpage("so_registres.html", "Registres de langue : formal or informal?", 'Formal or <span>informal?</span>', "Adapter sa façon de parler à la situation et à la personne",
  ("#f0abfc", "#a21caf"), LES,
  {"r1": ("choice", "Cette phrase est-elle formelle ou informelle ?", R1), "r2": ("choice", "Choisis l'équivalent formel", R2), "r3": ("choice", "Choisis la phrase adaptée à la situation", R3)},
  [M("r1", "🎚️", "Formel ou informel ?", "Reconnais le registre d'une phrase.", ["r1"], 10),
   M("r2", "🎩", "Version soutenue", "Remplace le mot familier par un mot formel.", ["r2"], 10),
   M("r3", "🤝", "La bonne phrase au bon moment", "Choisis ce qu'il faut dire selon la personne et la situation.", ["r3"], 10)], tag=SOC)

LES = '''      <p>L'anglais britannique (<span class="hl">BrE</span>) et l'anglais américain (<span class="hl">AmE</span>) se comprennent parfaitement, mais ils diffèrent par le vocabulaire, l'orthographe, un peu la grammaire et beaucoup l'accent.</p>
      <p><b>Vocabulaire :</b> flat / apartment · lift / elevator · holiday / vacation · trousers / pants · rubbish / trash · queue / line · petrol / gas · autumn / fall · mobile / cell phone · chips / fries · crisps / chips · biscuit / cookie · football / soccer</p>
      <p><b>Orthographe :</b> colour / color · centre / center · organise / organize · travelled / traveled · programme / program · defence / defense</p>
      <p><b>Grammaire :</b> <i>Have you got…? / Do you have…?</i> · <i>Have you eaten yet? / Did you eat yet?</i> · <i>at the weekend / on the weekend</i></p>
      <p><b>Dates :</b> 4/7 = le 4 juillet au Royaume-Uni (jour/mois) mais le 7 avril aux États-Unis (mois/jour) !</p>'''
BA = [("flat", "apartment", "appartement"), ("lift", "elevator", "ascenseur"), ("holiday", "vacation", "vacances"), ("trousers", "pants", "pantalon"), ("rubbish", "trash", "ordures"),
      ("queue", "line", "file d'attente"), ("petrol", "gas", "essence"), ("autumn", "fall", "automne"), ("mobile phone", "cell phone", "téléphone portable"), ("chips", "fries", "frites"),
      ("crisps", "chips", "chips"), ("biscuit", "cookie", "biscuit"), ("football", "soccer", "football"), ("underground", "subway", "métro"), ("sweets", "candy", "bonbons"), ("pavement", "sidewalk", "trottoir")]
V1 = [C(f"BrE: {b} → AmE:", [a] + [x[1] for x in BA if x[1] != a][i % 5:i % 5 + 2], fr=f"« {f} » en anglais américain ?") for i, (b, a, f) in enumerate(BA)]
V2 = [C(f"AmE: {a} → BrE:", [b] + [x[0] for x in BA if x[0] != b][i % 5 + 3:i % 5 + 5], fr=f"« {f} » en anglais britannique ?") for i, (b, a, f) in enumerate(BA)]
SP = [C(None, ["colour", "color"], fr="Orthographe britannique de « couleur » ?", keep=True), C(None, ["center", "centre"], fr="Orthographe américaine de « centre » ?", keep=True),
      C(None, ["organize", "organise"], fr="Orthographe américaine de « organiser » ?", keep=True), C(None, ["travelled", "traveled"], fr="Orthographe britannique de « voyagé » ?", keep=True),
      C(None, ["theatre", "theater"], fr="Orthographe britannique de « théâtre » ?", keep=True), C(None, ["favorite", "favourite"], fr="Orthographe américaine de « préféré » ?", keep=True),
      C(None, ["programme", "program"], fr="Orthographe britannique d'un programme télé ?", keep=True), C(None, ["defense", "defence"], fr="Orthographe américaine de « défense » ?", keep=True),
      C("I'll meet you on the weekend.", ["American English", "British English"], keep=True, tip="BrE : at the weekend."),
      C("Have you got a pen?", ["British English", "American English"], keep=True, tip="AmE préfère : Do you have a pen?"),
      C("Did you eat yet?", ["American English", "British English"], keep=True, tip="BrE : Have you eaten yet?"),
      C("The date 4/7/2026 means 4 July.", ["British English", "American English"], keep=True, tip="BrE : jour/mois ; AmE : mois/jour → 7 avril.")]
newpage("so_british_american.html", "British or American English?", 'British or <span>American?</span>', "Vocabulaire, orthographe et grammaire des deux côtés de l'Atlantique",
  ("#bfdbfe", "#dc2626"), LES,
  {"v1": ("choice", "Choisis le mot américain", V1), "v2": ("choice", "Choisis le mot britannique", V2), "sp": ("choice", "Orthographe et grammaire", SP)},
  [M("v1", "🗽", "Du britannique à l'américain", "Trouve le mot utilisé aux États-Unis.", ["v1"], 10),
   M("v2", "☕", "De l'américain au britannique", "Trouve le mot utilisé au Royaume-Uni.", ["v2"], 10),
   M("sp", "✏️", "Orthographe et grammaire", "colour ou color ? Have you got ou Do you have ?", ["sp"], 12)], tag=SOC)

LES = '''      <p>À l'oral et entre amis, les anglophones utilisent beaucoup de <b>formes réduites</b> et de mots familiers. Il faut les <b>comprendre</b>, mais les éviter à l'écrit formel et dans un entretien !</p>
      <p><b>Formes réduites :</b> <i>gonna</i> = going to · <i>wanna</i> = want to · <i>gotta</i> = (have) got to · <i>dunno</i> = don't know · <i>kinda</i> = kind of · <i>gimme</i> = give me · <i>innit?</i> = isn't it? (Londres)</p>
      <p><b>Royaume-Uni :</b> <i>mate</i> (ami) · <i>cheers</i> (merci / salut) · <i>ta</i> (merci) · <i>quid</i> (livre sterling) · <i>knackered</i> (crevé) · <i>gutted</i> (dégoûté) · <i>brilliant</i> (génial)</p>
      <p><b>États-Unis :</b> <i>buddy / dude</i> (mec) · <i>awesome</i> (génial) · <i>bucks</i> (dollars) · <i>y'all</i> (vous tous, Sud) · <i>What's up?</i> (quoi de neuf ?)</p>
      <p><b>Australie :</b> <i>G'day</i> (bonjour) · <i>arvo</i> (après-midi) · <i>brekkie</i> (petit-déj) · <i>No worries</i> (pas de souci)</p>'''
A1 = [C("I'm gonna call you tonight.", ["going to", "want to", "got to"], fr="Que signifie « gonna » ?"), C("I wanna go home.", ["want to", "going to", "won't"], fr="Que signifie « wanna » ?"),
      C("I dunno.", ["don't know", "do now", "done know"], fr="Que signifie « dunno » ?"), C("I gotta go!", ["have got to", "going to", "got a"], fr="Que signifie « gotta » ?"),
      C("It's kinda weird.", ["kind of", "kind and", "kinder"], fr="Que signifie « kinda » ?"), C("Gimme that!", ["give me", "get me", "gave me"], fr="Que signifie « gimme » ?"),
      C("It's cold, innit?", ["isn't it", "in it", "is it not cold inside"], fr="Que signifie « innit » ?"), C("Lemme help you.", ["let me", "lend me", "lemon"], fr="Que signifie « lemme » ?")]
A2 = [C("Cheers, mate!", ["Merci, l'ami !", "Santé, maman !", "Au revoir, monsieur."], fr="Traduis (Royaume-Uni)."), C("It costs ten quid.", ["dix livres sterling", "dix dollars", "dix pièces"], fr="Que signifie « quid » ?"),
      C("I'm knackered.", ["Je suis crevé.", "Je suis fâché.", "Je suis en retard."], fr="Que signifie « knackered » ?"), C("I was gutted when we lost.", ["dégoûté, très déçu", "content", "surpris"], fr="Que signifie « gutted » ?"),
      C("That's awesome, dude!", ["C'est génial, mec !", "C'est horrible !", "C'est cher, mec !"], fr="Traduis (États-Unis)."), C("It's twenty bucks.", ["vingt dollars", "vingt livres", "vingt cerfs"], fr="Que signifie « bucks » ?"),
      C("See you this arvo!", ["cet après-midi", "ce soir", "demain matin"], fr="Que signifie « arvo » (Australie) ?"), C("Hey y'all!", ["Salut tout le monde !", "Salut toi !", "Bonjour monsieur !"], fr="Que signifie « y'all » (sud des USA) ?"),
      C("What's up?", ["Quoi de neuf ?", "Qu'y a-t-il en haut ?", "Lève-toi !"], fr="Que signifie « What's up? » ?"), C("No worries!", ["Pas de souci !", "Ne t'inquiète pas pour moi, je pars.", "Aucune chance !"], fr="Que signifie « No worries » ?")]
A3 = [C(None, ["I am going to apply for the job.", "I'm gonna apply for the job.", "Gonna apply for the job, mate."], fr="Lettre de motivation : choisis la phrase acceptable."),
      C(None, ["I don't know the answer.", "Dunno the answer.", "I dunno, dude."], fr="Réponse à l'examen oral du CAP."),
      C(None, ["That would be great, thank you.", "Awesome, cheers mate!", "Kinda cool."], fr="Tu réponds à ton futur employeur qui te propose un stage."),
      C(None, ["Hey mate, wanna grab a pizza?", "Would you like to have dinner with me, Sir?", "I would be delighted to invite you to a meal."], fr="Message à un très bon ami (registre adapté).")]
newpage("so_familier.html", "Anglais familier et argot", 'Informal English <span>&amp; slang</span>', "Comprendre l'anglais parlé entre amis… et savoir quand l'éviter",
  ("#fdba74", "#c2410c"), LES,
  {"a1": ("choice", "Que signifie la forme réduite ?", A1), "a2": ("choice", "Que signifie l'expression familière ?", A2), "a3": ("choice", "Le bon registre", A3)},
  [M("a1", "🗣️", "Formes réduites", "gonna, wanna, dunno… : retrouve la forme complète.", ["a1"], 8),
   M("a2", "😎", "Argot du monde anglophone", "Royaume-Uni, États-Unis, Australie.", ["a2"], 10),
   M("a3", "⚖️", "Familier ou pas ?", "Choisis la phrase adaptée à la situation.", ["a3"], 4)], tag=SOC)

# ════════════════════ PRAGMATIQUE ════════════════════
LES = '''      <p>Parler, c'est <b>agir</b> : demander, remercier, s'excuser, proposer, refuser… Ce sont les <b>actes de parole</b>. Chaque situation a ses formules.</p>
      <p><b>Demander :</b> <i>Could you…? / Can I have…? / Would you mind + -ing?</i> · <b>Proposer :</b> <i>Shall I…? / Would you like…? / Why don't we…? / Let's…</i></p>
      <p><b>Accepter :</b> <i>Sure! / That sounds great. / I'd love to.</i> · <b>Refuser poliment :</b> <i>I'd love to, but… / I'm afraid I can't. / Thanks, but…</i></p>
      <p><b>S'excuser :</b> <i>Sorry! / I'm so sorry. / I apologise for…</i> → réponse : <i>That's OK. / Never mind. / Don't worry.</i></p>
      <p><b>Remercier :</b> <i>Thanks a lot. / Thank you so much. / I really appreciate it.</i> → réponse : <i>You're welcome. / No problem. / My pleasure.</i></p>
      <p><b>Se plaindre poliment :</b> <i>I'm sorry, but… / I'm afraid there's a problem with…</i></p>'''
S1 = [C(None, ["Would you like a cup of tea?", "Do you want tea!", "Give me tea."], fr="Tu proposes une boisson à un invité."),
      C(None, ["I'd love to, but I have to work.", "No.", "I don't want to."], fr="Un ami t'invite au cinéma, tu refuses poliment."),
      C(None, ["I'm so sorry I'm late.", "I'm late, that's it.", "Sorry for nothing."], fr="Tu arrives en retard en cours."),
      C(None, ["Thank you so much for your help.", "OK help.", "Good help."], fr="Ton tuteur t'a beaucoup aidé, tu le remercies."),
      C(None, ["You're welcome.", "Yes, thank you.", "Me too."], fr="On te dit « Thank you! ». Que réponds-tu ?"),
      C(None, ["Never mind.", "You're welcome.", "Me neither."], fr="Un ami s'excuse d'avoir oublié ton livre. Tu le rassures."),
      C(None, ["Shall I carry your bag?", "Carry your bag.", "Do I carry bag?"], fr="Tu proposes ton aide pour porter un sac."),
      C(None, ["Why don't we go to the park?", "We go park.", "Go to the park!"], fr="Tu suggères une activité à des amis."),
      C(None, ["I'm afraid there's a problem with my order.", "Your order is rubbish!", "Problem!"], fr="Tu te plains poliment au service client."),
      C(None, ["Sorry, could you repeat that, please?", "What?", "Again!"], fr="Tu n'as pas compris ton interlocuteur."),
      C(None, ["Congratulations!", "Bless you!", "Cheers!"], fr="Un ami vient d'obtenir son diplôme."),
      C(None, ["Bless you!", "Congratulations!", "Good luck!"], fr="Quelqu'un éternue.")]
S2 = [C("Could you open the window?", ["une demande", "une excuse", "un remerciement"], fr="Quel acte de parole ?"), C("Let's go to the beach!", ["une proposition", "un refus", "un reproche"], fr="Quel acte de parole ?"),
      C("I apologise for the delay.", ["une excuse", "une proposition", "un conseil"], fr="Quel acte de parole ?"), C("You should see a doctor.", ["un conseil", "un ordre", "une excuse"], fr="Quel acte de parole ?"),
      C("I'm afraid I can't come.", ["un refus poli", "une acceptation", "une demande"], fr="Quel acte de parole ?"), C("I really appreciate it.", ["un remerciement", "une plainte", "une demande"], fr="Quel acte de parole ?"),
      C("Don't touch that!", ["une interdiction", "une proposition", "un remerciement"], fr="Quel acte de parole ?"), C("That sounds great!", ["une acceptation", "un refus", "une excuse"], fr="Quel acte de parole ?")]
newpage("pr_actes_parole.html", "Actes de parole : demander, proposer, s'excuser", 'Speech <span>acts</span>', "Demander, proposer, accepter, refuser, s'excuser, remercier",
  ("#a5b4fc", "#4f46e5"), LES,
  {"s1": ("choice", "Que dis-tu dans cette situation ?", S1), "s2": ("choice", "Quel est l'acte de parole ?", S2)},
  [M("s1", "💬", "Que dire ?", "Choisis la phrase qui convient à la situation.", ["s1"], 12),
   M("s2", "🎯", "Reconnaître l'intention", "Demande, excuse, refus, conseil… ?", ["s2"], 8)], tag=PRA)

LES = '''      <p>Ce qu'on dit n'est pas toujours ce qu'on veut dire : c'est l'<b>implicite</b>. Les Britanniques sont célèbres pour l'<span class="hl">understatement</span> (l'euphémisme) et la politesse indirecte.</p>
      <p><i>Not bad</i> = bien, voire très bien · <i>Quite good</i> = moyen (BrE) · <i>That's interesting…</i> = je ne suis pas convaincu · <i>I'll bear it in mind</i> = je ne le ferai sans doute pas</p>
      <p><i>With all due respect…</i> = je ne suis pas d'accord du tout · <i>I hear what you say</i> = je ne suis pas d'accord · <i>Correct me if I'm wrong, but…</i> = je suis sûr d'avoir raison</p>
      <p><i>It's a bit chilly</i> = il fait très froid · <i>We should meet up some time</i> = (souvent) simple formule de politesse · <i>Is it OK if I open the window?</i> = j'ai chaud</p>
      <p>L'<b>intonation</b> et le <b>contexte</b> comptent : <i>Great!</i> peut être ironique.</p>'''
I1 = [C("\"Not bad at all!\" says your teacher about your essay.", ["C'est bien, voire très bien.", "C'est mauvais.", "C'est moyen, sans plus."], fr="Que veut-il vraiment dire ?"),
      C("\"That's an interesting idea…\" says your manager, with a long pause.", ["Il n'est pas convaincu.", "Il adore l'idée.", "Il veut en parler tout de suite."], fr="Que veut-il vraiment dire ?"),
      C("\"I'll bear it in mind.\"", ["Il ne le fera probablement pas.", "Il va le faire tout de suite.", "Il a mal à la tête."], fr="Que veut-il vraiment dire ?"),
      C("\"With all due respect, I think you're mistaken.\"", ["Il n'est pas du tout d'accord.", "Il a beaucoup de respect et il est d'accord.", "Il s'excuse."], fr="Que veut-il vraiment dire ?"),
      C("\"It's a bit chilly in here, isn't it?\"", ["Il fait froid : pourrait-on fermer la fenêtre ?", "Il fait bon.", "Il veut un piment."], fr="Que veut-elle vraiment dire ?"),
      C("\"We should have lunch some time!\"", ["Souvent une simple formule polie.", "Un rendez-vous précis demain.", "Une invitation obligatoire."], fr="Que veut-il vraiment dire ?"),
      C("You spill coffee on your new shirt. Your friend says: \"Great. Just great.\"", ["C'est ironique : c'est une catastrophe.", "Il trouve ça génial.", "Il veut un café."], fr="Que veut-il vraiment dire ?"),
      C("\"Correct me if I'm wrong, but the meeting was on Monday.\"", ["Il est sûr d'avoir raison.", "Il n'en a aucune idée.", "Il veut être corrigé."], fr="Que veut-il vraiment dire ?"),
      C("\"I might be a little late.\" (a British colleague)", ["Il sera sans doute bien en retard.", "Il sera en avance.", "Il ne viendra jamais."], fr="Que veut-il vraiment dire ?"),
      C("A customer looks at the price and says: \"Hmm, it's a bit expensive…\"", ["Il hésite : propose une alternative moins chère.", "Il va acheter tout de suite.", "Il veut payer plus."], fr="Que veut-il vraiment dire ?")]
I2 = [C(None, ["Do you think you could turn the music down a bit?", "Turn the music down!", "Your music is horrible."], fr="Ton voisin met la musique trop fort. Quelle demande est la plus diplomatique ?"),
      C(None, ["I see your point, but I'm not sure I agree.", "You're wrong.", "That's stupid."], fr="Tu n'es pas d'accord avec un collègue, poliment."),
      C(None, ["It might be a good idea to check the figures again.", "Your figures are wrong.", "Check again, it's bad."], fr="Tu signales une erreur à ton supérieur, avec tact."),
      C(None, ["I'm not really a fan of horror films.", "I hate horror films, they're stupid.", "Horror films? No way!"], fr="Ton ami propose un film d'horreur ; tu refuses avec tact."),
      C(None, ["Could I possibly borrow your notes?", "Give me your notes.", "Notes!"], fr="Tu demandes un service à un camarade que tu connais peu.")]
newpage("pr_implicite.html", "L'implicite : ce qu'on dit vraiment", 'Reading between <span>the lines</span>', "Understatement, ironie, politesse indirecte",
  ("#fbcfe8", "#be185d"), LES,
  {"i1": ("choice", "Que veut vraiment dire la personne ?", I1), "i2": ("choice", "Choisis la formulation la plus diplomatique", I2)},
  [M("i1", "🕵️", "Que veut-il vraiment dire ?", "Décode l'implicite et l'understatement.", ["i1"], 10),
   M("i2", "🕊️", "Dire les choses avec tact", "Choisis la formulation diplomatique.", ["i2"], 5)], tag=PRA)

LES = '''      <p>Pour <b>convaincre</b>, il faut organiser son discours : introduire, donner son avis, argumenter, nuancer, conclure.</p>
      <p><b>Introduire :</b> <i>Nowadays, … / These days, … / Let's talk about…</i> · <b>Donner son avis :</b> <i>In my opinion, / I think that… / As far as I'm concerned,</i></p>
      <p><b>Ordonner :</b> <i>First (of all), / Secondly, / Then, / Finally,</i> · <b>Ajouter :</b> <i>Moreover, / What's more, / Besides,</i> · <b>Illustrer :</b> <i>For example, / For instance, / such as</i></p>
      <p><b>Nuancer / opposer :</b> <i>However, / On the other hand, / Although… / Even if…</i> · <b>Conclure :</b> <i>To conclude, / All in all, / To sum up,</i></p>
      <p><b>Réagir :</b> <i>I agree with you. / That's a good point. / I see what you mean, but… / I'm not sure about that. / I totally disagree.</i></p>'''
P1 = [G("____ my opinion, school uniforms are a good idea.", "In", fr="Donner son avis."), G("____ of all, they are cheaper for families.", "First", fr="Premier argument."),
      G("____, they reduce differences between rich and poor students.", ["Secondly", "Moreover", "What's more", "Besides"], fr="Ajouter un argument."),
      G("____ example, nobody can show off expensive brands.", "For", fr="Illustrer."), G("____, some students feel they can't express their personality.", ["However", "On the other hand"], fr="Opposer un argument."),
      G("To ____ up, uniforms have more advantages than drawbacks.", "sum", fr="Conclure."), G("I see what you ____, but I don't agree.", "mean", fr="Nuancer."),
      G("That's a good ____.", "point", fr="Approuver un argument."), G("As far as I'm ____, homework is useful.", "concerned", fr="Donner son avis (soutenu)."),
      G("All in ____, it was a great experience.", "all", fr="Conclure.")]
P2 = [O("Nowadays, many teenagers spend hours on their phones.|In my opinion, this can be a problem.|First, they sleep less.|Moreover, they spend less time with their family.|However, phones are also useful to learn and to stay in touch.|To conclude, we must learn to use them reasonably.",
        "Remets le paragraphe dans l'ordre logique : les téléphones."),
      O("These days, more and more people work from home.|I think it has many advantages.|First of all, workers don't waste time in transport.|What's more, they can organise their day.|On the other hand, some feel lonely.|All in all, a mix of home and office is the best solution.",
        "Remets le paragraphe dans l'ordre logique : le télétravail."),
      O("Let's talk about fast food.|As far as I'm concerned, we should eat less of it.|For example, burgers contain a lot of fat and salt.|Besides, it's not cheaper than cooking at home.|Of course, it's quick and tasty.|To sum up, fast food is fine, but only from time to time.",
        "Remets le paragraphe dans l'ordre logique : le fast food.")]
P3 = [C("A: \"Video games make people violent.\" — B: \"I see what you mean, but…\"", ["B n'est pas vraiment d'accord.", "B est totalement d'accord.", "B ne comprend pas."], fr="Quelle est la position de B ?"),
      C("\"That's a good point.\"", ["J'approuve cet argument.", "Je ne suis pas d'accord.", "Je change de sujet."], fr="Que signifie cette réaction ?"),
      C(None, ["I totally disagree.", "I partly agree.", "I agree with you."], fr="Choisis le désaccord le plus fort."),
      C(None, ["To sum up,", "For instance,", "Moreover,"], fr="Quel connecteur sert à conclure ?"),
      C(None, ["For instance,", "However,", "Finally,"], fr="Quel connecteur introduit un exemple ?"),
      C(None, ["On the other hand,", "What's more,", "First,"], fr="Quel connecteur introduit un argument opposé ?")]
newpage("pr_argumenter.html", "Argumenter et structurer son discours", 'Give your <span>opinion</span>', "Introduire, argumenter, nuancer, conclure, réagir",
  ("#86efac", "#15803d"), LES,
  {"p1": ("gap", "Complète avec le mot qui manque", P1), "p2": ("order", "Remets les phrases dans l'ordre", P2), "p3": ("choice", "Réagir et structurer", P3)},
  [M("p1", "🧱", "Les mots du discours", "Complète les expressions pour argumenter.", ["p1"], 10),
   M("p2", "🧩", "Construire un paragraphe", "Remets les phrases dans l'ordre logique.", ["p2"], 3),
   M("p3", "🎙️", "Réagir dans un débat", "Comprends les réactions et choisis le bon connecteur.", ["p3"], 6)], tag=PRA)
print("ok")
