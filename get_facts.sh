echo "<!DOCTYPE html>" > index.html 
echo "<html>" >> index.html 
echo "<head>" >> index.html 
echo "<style>" >> index.html 
echo "body {background-color: powderblue;}" >> index.html 
echo "h1   {color: blue;}" >> index.html 
echo "p    {color: red;}" >> index.html 
echo "</style>" >> index.html 
echo "</head>" >> index.html 
echo "<body>" >> index.html 

echo "<h1>Fun facts</h1>" >> index.html
echo "<ul>" >> index.html

for file in data/*.json; do 
echo "<li>" >> index.html
jq -r .text $file >> index.html 
echo "</li>" >> index.html 
done 


echo "</ul>" >> index.html

python3 myscript.py >> index.html 

echo "<img src='my_plot.png'>" >> index.html

echo "</body>" >> index.html 

echo "</html>" >> index.html 