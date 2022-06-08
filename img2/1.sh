#!/bin/bash
#!/bin/bash
for file in *.kra
do
  krita "$file" --export --export-filename "$(basename $file .kra)".png ;
done
