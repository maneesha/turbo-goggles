

echo "<h1>Fun facts</h1>" > index.html
echo "<ul>" >> index.html

for file in data/*.json; do 
echo "<li>" >> index.html
jq -r .text $file >> index.html 
echo "</li>" >> index.html 
done 


echo "</ul>" >> index.html


