#!/usr/bin/env bash
# Régénère le site, vérifie, et met à jour le cache hors connexion.
# Usage : bash outils/build.sh            (régénère + vérifie)
#         bash outils/build.sh cu_salem.html cu_titanic.html   (+ teste ces pages dans un navigateur)
set -e
cd "$(dirname "$0")/.."
O=outils

echo "1/5 Dossiers culture et pages récentes"
for f in 19 21 22 23 25 26 27 28 29 30 31 32 33 34 35 36 37 38; do python3 $O/content$f.py >/dev/null; done

echo "2/5 Serveur local"
python3 -m http.server 8765 >/dev/null 2>&1 & SRV=$!
trap 'kill $SRV 2>/dev/null' EXIT
sleep 1

echo "3/5 Accueil, catalogue, comptage des exercices"
python3 $O/index_gen2.py >/dev/null
python3 $O/mcount.py | tail -1
python3 $O/index_gen2.py >/dev/null

echo "4/5 Vérification des liens et des options"
python3 $O/smoke.py | tail -2

if [ $# -gt 0 ]; then
  echo "    Tests navigateur : $*"
  REPS=1 python3 $O/test.py "$@" | grep -c "errors: \[\]" | xargs -I{} echo "    {} / $# pages sans erreur"
fi

echo "5/5 Cache hors connexion (sw.js)"
python3 $O/sw_gen.py >/dev/null
echo "Terminé."
