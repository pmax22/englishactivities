import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
# Sections ajoutées aux dossiers pour les étoffer (markdown du dossier)
EXTRA = {
"cu_institutions_uk": """
## Une démocratie à l'oral : les Prime Minister's Questions
Chaque mercredi à midi, le Premier ministre doit répondre pendant une demi-heure, debout, aux questions des députés : ce sont les **PMQs**. Le chef de l'opposition l'interroge directement, les députés applaudissent, protestent, rient. Ce moment très théâtral, retransmis à la télévision, montre une particularité britannique : le gouvernement est issu du Parlement et doit rendre des comptes en personne, face à ses adversaires.

## Pourquoi pas de constitution écrite ?
Le système britannique s'est construit peu à peu, sans révolution qui aurait obligé à tout réécrire. Ses partisans y voient une force : il est souple et peut s'adapter vite. Ses critiques y voient une faiblesse : un gouvernement disposant d'une large majorité peut changer des règles fondamentales par une simple loi. La **House of Lords** fait aussi débat : avec plusieurs centaines de membres non élus, c'est l'une des plus grandes assemblées parlementaires du monde, et beaucoup réclament sa réforme ou son remplacement par une chambre élue.
""",
"cu_empire": """
## Des pages sombres, une mémoire disputée
L'Empire a aussi été un système de violence, que les Britanniques regardent aujourd'hui plus en face.
- En **1919**, à **Amritsar**, en Inde, des soldats sous commandement britannique tirent sur une foule désarmée réunie dans un jardin clos, le Jallianwala Bagh : des centaines de morts. Le massacre renforce le mouvement pour l'indépendance mené par Gandhi.
- En **1943**, la **famine du Bengale** fait environ trois millions de morts, alors que les autorités coloniales donnent la priorité à l'effort de guerre ; le rôle du gouvernement de Churchill reste débattu par les historiens.
- Au **Kenya**, la répression de la révolte des Mau Mau s'accompagne de camps de détention et de tortures. En 2013, le gouvernement britannique exprime ses « regrets sincères » et indemnise plus de 5 000 victimes kényanes.
- De nombreux objets pris pendant la colonisation sont exposés dans les musées britanniques, comme les **bronzes du Bénin**, pillés en 1897 au Nigeria. Certains musées ont commencé à les restituer.

## Pourquoi en parler aujourd'hui ?
Les Britanniques sont divisés : pour certains, l'Empire a aussi apporté le chemin de fer, le droit ou la langue anglaise ; pour d'autres, ces arguments masquent l'exploitation et le racisme. Ce débat se retrouve dans les programmes scolaires, les musées et les statues, et il concerne directement des millions de Britanniques dont les familles viennent d'anciennes colonies.
""",
}
