#!/bin/bash

# langs=("tr" "pt" "de")
langs=("tr")

if ! command -v xgettext &> /dev/null
then
	echo "xgettext could not be found."
	echo "you can install the package with 'apt install gettext' command on debian."
	exit
fi


echo "updating pot file"
xgettext -o po/etap-session-operations.pot --files-from=po/files

for lang in ${langs[@]}; do
	if [[ -f po/$lang.po ]]; then
		echo "updating $lang.po"
		msgmerge -o po/$lang.po po/$lang.po po/etap-session-operations.pot
	else
		echo "creating $lang.po"
		cp po/etap-session-operations.pot po/$lang.po
	fi
done
