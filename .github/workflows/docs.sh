#!/bin/bash

mkdir docs-temp/
mv docs/* docs-temp/
cd docs/
export VERSION=$(grep version ../setup.py | cut -f2 -d "'")
sphinx-quickstart --sep -p ufjc -l en -a 'Michael R. Buche, Scott J. Grutzik' -r ${VERSION} -v ${VERSION}
sphinx-apidoc -e -P -o source ../ ../*setup*
mv ../docs-temp/* source/
rm -r ../docs-temp/
echo "release = '${VERSION}'" >> source/conf.py
echo "version = '${VERSION}'" >> source/conf.py
for file in ../ufjc/*.py; do 
    export file_basename=$(basename ${file%.*})
    export rst_file=$(echo "source/*`basename ${file%.*}`.rst")
    if [ -f $rst_file ]; then 
        if grep -q :cite $file; then 
            echo "citations in $file"
            echo "" >> $rst_file
            echo "" >> $rst_file
            export OLD_CITE=$(echo cite:'`')
            export NEW_CITE=$(echo $OLD_CITE$file_basename'-')
            sed -i -e "s/${OLD_CITE}/${NEW_CITE}/g" $file
            echo ".. raw::" >> $rst_file
            echo " html" >> $rst_file
            echo "" >> $rst_file
            echo -n "   <hr>" >> $rst_file
            echo "" >> $rst_file
            echo "" >> $rst_file
            echo "**References**" >> $rst_file
            echo "" >> $rst_file
            echo ".. bibliography::" >> $rst_file
            echo -n "   :filter:" >> $rst_file
            echo " docname in docnames" >> $rst_file
            echo -n "   :keyprefix:" >> $rst_file
            echo " $file_basename-" >> $rst_file
        fi
    fi
done
