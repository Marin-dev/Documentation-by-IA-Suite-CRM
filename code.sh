#!/bin/bash

echo "=== Correction forcée de l'auteur Git ==="
echo "Ancien : determinator1232 <marin.lavigne@gmail.com>"
echo "Nouveau : Marin Lavigne <marin.lavigne.dev@gmail.com>"
echo ""

FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch -f --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "marin.lavigne@gmail.com" ]
then
    export GIT_AUTHOR_NAME="Marin Lavigne"
    export GIT_AUTHOR_EMAIL="marin.lavigne.dev@gmail.com"
    export GIT_COMMITTER_NAME="Marin Lavigne"
    export GIT_COMMITTER_EMAIL="marin.lavigne.dev@gmail.com"
fi
' --tag-name-filter cat -- --branches --tags

echo ""
echo "=== Vérification locale ==="
RESULT=$(git log --all --format="%H %an <%ae>" | grep "marin.lavigne@gmail.com")

if [ -z "$RESULT" ]
then
    echo "✅ Aucun commit avec l'ancien email trouvé !"
    echo ""
    echo "=== Push forcé sur GitHub ==="
    git push --force --all
    echo ""
    echo "=== Auteurs finaux ==="
    git log --all --format="%an <%ae>" | sort | uniq
    echo ""
    echo "✅ Terminé ! Vérifiez sur GitHub dans quelques minutes."
else
    echo "❌ Des commits avec l'ancien email existent encore :"
    echo "$RESULT"
    echo "Le push n'a pas été effectué. Contactez le support."
fi